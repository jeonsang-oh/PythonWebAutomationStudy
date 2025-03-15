from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(3)

#By.ID 로 element id입력하여 요소 찾기
query = driver.find_element(By.ID, "query")
query.send_keys("파이썬으로 웹 자동화")
time.sleep(2)

#By.CSS_SELECTOR 로 요소 찾기
#코드 한줄로 액션까지 가능
search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn").click()

#엔터키 이벤트 
#query = driver.find_element(By.ID, "query").send_keys(Keys.ENTER)

