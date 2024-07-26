import os
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 이미지 다운로드
from urllib.request import urlretrieve  

# 화면 텍스트
from PySide6.QtWidgets import QTextEdit

# 크롬 옵션 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")    
    
def fn_crawling (obj, log_with_step) :
    step = 0
    
    def qConsole(msg):
        nonlocal step
        log_with_step(msg, step)
        step += 1
    
    def f_Quit():
        nonlocal step, driver
        driver.quit() 
        step = -1
        qConsole("-------- Crawling End --------\n")
        
    # 브라우저 열기
    driver = webdriver.Chrome(options=chrome_options)
    qConsole("-------- Crawling Starting [%s] --------" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))
    
    # 파라미터 셋팅
    qConsole("Parameter Setting...")
    
    keyword = obj.get('keyword')
    scrollNum = int(obj.get('scrollNum'))
    path = obj.get('path') 
    
    if not keyword:
        qConsole("Keyword does not exist. Please enter a keyword.")
        f_Quit()
        return
    
    if scrollNum <= 0:
        scrollNum = 1  
        
    if path == '' : 
        path = os.path.expandvars(r'%USERPROFILE%\Documents\crawling')
        qConsole("No folder selected. Setting to the default folder path")

    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        qConsole("The folder does not exist. Creating a new folder at the specified path.")
        
        
    qConsole("Keyword: %s, Scroll Count: %d, Download Path: %s" % (keyword, scrollNum, path))
    
    # 구글 이미지 url
    url_google = f"https://www.google.com/search?q={keyword}&tbm=isch"
    driver.get(url_google)
    
    # 이미지 로드
    for _ in range(scrollNum) :
        driver.execute_script("window.scrollBy(0, 1000);")  # vertical scroll 1000px
        time.sleep(2)
        
    image_elements = driver.find_elements(By.CSS_SELECTOR, 'img Q4LuWd')
    
    qConsole("Image loading completed...  Total %d items." % (len(image_elements)))
    
    # 이미지 다운로드
    imageNum = 0
    for img in image_elements:
        try:
            imageUrl = path + f'/{keyword}_{imageNum}.jpg'
            link = img.get_attribute("src")
            urlretrieve(link, imageUrl)
            qConsole("Image[%d] download completed..." % (imageNum))
        except Exception as e:
            qConsole("Image[%d] download error! Skip... : %s" % (imageNum, e))
            continue
        imageNum += 1
    
    f_Quit()
    return
    