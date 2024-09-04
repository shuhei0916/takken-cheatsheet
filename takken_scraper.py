
import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_question(driver): 
    driver.implicitly_wait(10)
    question_elements = driver.find_elements(By.CSS_SELECTOR, "section.content")
    return question_elements

def button_click(driver):
    try: 
        button = driver.find_element(By.CSS_SELECTOR, "button.submit.sendConfigform.hover[name='start']")
        button.click()
    except Exception as e:
        print(f"エラーが発生しました:{e}")
        

def main():
    driver = webdriver.Chrome() 
    driver.get('https://takken-siken.com/marubatu.php')
        
    button_click(driver)
    driver.quit()
        

if __name__ == "__main__":
    main()