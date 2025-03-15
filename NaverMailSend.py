from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip
import random
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
old_url = driver.current_url

time.sleep(random.randint(1, 2))

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
time.sleep(2)

print("네이버 url -> " + driver.current_url)
# 네이버 메인 메일 클릭
driver.find_element(By.XPATH, '//*[@id="account"]/div[2]/div/div/ul/li[1]/a/span[1]').click()
time.sleep(1)
# 메일 클릭시 메일 홈으로 들어갈 수 있는 버튼
driver.find_element(By.XPATH, '//*[@id="account"]/div[3]/div[2]/div[1]/a').click()
time.sleep(3)

new_window = driver.window_handles[-1]  # 마지막으로 열린 창 선택
driver.switch_to.window(new_window)
print("메일 url -> " + driver.current_url)
# 메일 쓰기

driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div[1]/div[2]/a[1]').click()
time.sleep(2)

recipient = driver.find_element(By.ID, "recipient_input_element")
recipient.send_keys("fags4634@naver.com")
time.sleep(2)

# 이메일 제목 작성
driver.find_element(By.ID, "subject_title").send_keys("양파쿵야 보고가세요!")
time.sleep(2)

file_input = driver.find_element(By.XPATH, "//input[@type='file']")

file_paths = [
    '/Users/sangoh/Downloads/양파쿵야1.jpg',
    '/Users/sangoh/Downloads/양파쿵야2.jpg'
]

file_input.send_keys("\n".join(file_paths))

time.sleep(2)

# 본문 작성 (iframe 안으로 들어가기)
iframe = driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-content").send_keys("귀여운 야채쿵야")
time.sleep(2)

# iframe 밖으로 나오기
driver.switch_to.default_content()

# 보내기
driver.find_element(By.CSS_SELECTOR, "button.button_write_task").click()
time.sleep(50)