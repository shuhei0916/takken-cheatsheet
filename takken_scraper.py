
import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_question(driver): 
    # driver.implicitly_wait(10)
    # question_elements = driver.find_elements(By.CSS_SELECTOR, "section.content")
    
    return "答えよ、答えよ。"

def button_click(driver): # WARNING: button_click()は副作用があることに注意。button.clickによりページが遷移している。
    try: 
        button = driver.find_element(By.CSS_SELECTOR, "button.submit.sendConfigform.hover[name='start']")
        button.click()
    except Exception as e:
        print(f"エラーが発生しました:{e}")
        

def main():
    driver = webdriver.Chrome() 
    driver.get('https://takken-siken.com/marubatu.php')
        
    button_click(driver)
    
    question_elements = scrape_question(driver)
    if not question_elements:
        print("question_element not found")
    for element in question_elements:
        print(element.text)
        
    driver.quit()
        

if __name__ == "__main__":
    main()