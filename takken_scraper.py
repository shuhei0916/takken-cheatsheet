
import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_question(driver): 
    driver.implicitly_wait(0.5)
    question_elements = driver.find_elements(By.CSS_SELECTOR, "section.content")
    return question_elements

def main():
    driver = webdriver.Chrome() 

    driver.get('https://takken-siken.com/marubatu.php')
    
    question_elements = scrape_question(driver)
    for element in question_elements:
        print(element.text)
        

if __name__ == "__main__":
    main()