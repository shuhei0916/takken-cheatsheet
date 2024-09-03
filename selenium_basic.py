# seleniumの必要なライブラリをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By

# tkinter（メッセージボックス表示）の必要なライブラリをインポート
import tkinter
from tkinter import messagebox 

# Chrome Webドライバー の インスタンスを生成
driver = webdriver.Chrome() 

print(type(driver))

driver.get('https://www.selenium.dev/selenium/web/web-form.html')

title = driver.title
print(title) 

text_box = driver.find_element(by=By.NAME, value= 'my-text')
submit_button = driver.find_element(by=By.CSS_SELECTOR, value='button')

text_box.send_keys('Selenium')
driver.implicitly_wait(1)
submit_button.click()
driver.implicitly_wait(10)

message = driver.find_element(by=By.ID, value='message')
text = message.text
print(text)

driver.quit()