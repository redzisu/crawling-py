from PySide6.QtWidgets import QMessageBox

"""
Alert창 
@param pStr {String} 메시지
"""
def fn_alert(pStr): 
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Alert")
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setText(pStr)
    msgBox.exec() 
    
"""
Confirm창 
@param pStr {String} 메시지
@param pCallback_yes {Callable} 확인버튼 눌렀을때 실행할 함수
@param pCallback_no {Callable} 취소버튼 눌렀을때 실행할 함수
"""
def fn_confirm(pStr, pCallback_yes, pCallback_no): 
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Confirm")
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setText(pStr)
    msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
    msgBox.button(QMessageBox.Save).setText("확인")
    msgBox.button(QMessageBox.Cancel).setText("취소")
    ret = msgBox.exec() 
    
    if ret == QMessageBox.Save:
        pCallback_yes()
    else:
        pCallback_no()