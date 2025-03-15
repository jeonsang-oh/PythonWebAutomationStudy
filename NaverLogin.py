from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyperclip
import configparser

properties = configparser.ConfigParser()

properties.read('config.ini')

session = properties["SESSION"]

options = Options()
options.add_argument("--start-maximized") 
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(3)

naver_id = session["id"]
naver_pw = session["pw"]

#By.ID 로 element id입력하여 요소 찾기
query = driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW").click()
time.sleep(1)

id = driver.find_element(By.ID, "id")
id.click()
pyperclip.copy(naver_id)
actions = ActionChains(driver)
actions.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(1)

pw = driver.find_element(By.ID, "pw").click()
pyperclip.copy(naver_pw)
actions = ActionChains(driver)
actions.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(1)

driver.find_element(By.ID, "log.login").click()