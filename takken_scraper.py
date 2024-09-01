
import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome() 

    # WebドライバーでQiitaログインページを起動
    driver.get('https://www.selenium.dev/selenium/web/web-form.html')
        

if __name__ == "__main__":
    main()