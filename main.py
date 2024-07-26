import sys
import os
import clipboard
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from view_ui import Ui_MainWindow
from common import fn_alert, fn_confirm 
from crawler import fn_crawling

#progressBar 표시하기 위해 thread 분리
class Worker(QThread):
    progress_update = Signal(int)
    
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui
        
    def run(self):
        obj = {
            "keyword" : self.ui.ibx_keyword.text(),
            "path" : self.ui.ibx_path.text(),
            "scrollNum" : self.ui.ibx_scrollNum.text(),
        }
        fn_crawling(obj, self.log_with_step)
    
    def log_with_step(self, logMsg, step):
        self.ui.console.append(logMsg)
        self.progress_update.emit(step)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.worker = Worker(self.ui)
        
        self.setWindowTitle("Image Crawler")
        
        #==================  Default Setting  ====================
        
        #==================  Signal  ====================
        self.ui.btn_search.clicked.connect(self.fn_execute)
        #self.ui.btn_folder.clicked.connect(self.fn_editList)
        
    #==================  Slot ====================
    # 리스트 행 추가
    def fn_execute(self) :
        self.worker.start()
        self.worker.progress_update.connect(self.fn_progressBar)
    
    # 진행바 컨트롤
    def fn_progressBar(self, value):
        if (value == -1 or value == 100) :
            if value == 100:
                fn_alert("complete")
            elif value == -1:
                fn_alert("Exit")
                
            self.ui.progressBar.setValue(0)
            self.ui.progressBar.setVisible(False) 
            self.worker.quit()
            self.worker.wait()  # 스레드 종료를 기다림
            self.worker.deleteLater()  # 스레드 객체 삭제 요청
        else :
            self.ui.progressBar.setValue(value)
            
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()        
    window.show()                 
    sys.exit(app.exec())         
