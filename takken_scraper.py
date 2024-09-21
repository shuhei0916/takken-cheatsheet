import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
import logging
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException  # StaleElementReferenceExceptionをインポート(必要か？)


logging.basicConfig(filename='log_takken_scraper.txt', filemode='w', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def click_start_button(driver): # WARNING: click_start_button()は副作用があることに注意。button.clickによりページが遷移している。
    try: 
        button = driver.find_element(By.CSS_SELECTOR, "button.submit.sendConfigform.hover[name='start']")
        button.click()
    except Exception as e:
        print(f"エラーが発生しました:{e}")

def click_next_button(driver):
    try: 
        # logging.debug('next_button.text: %s', next_button.text) # NOTE: これでいいの？
        next_button = driver.find_element(By.CSS_SELECTOR, "button.submit.sendConfigform.hover[data-text='NEXT']")
        if next_button.text == '次の問題':
            next_button.click()
            # print('next_button clicked!')

    except Exception as e:
        print(f"エラーが発生しました:{e}")

def click_pass_button(driver):
    try:
        # パスボタンがクリック可能になるまで最大10秒待機
        pass_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.hover'))
        )
        
        # 要素のテキストが "パス" か確認
        if pass_button.text == 'パス':
            pass_button.click()
    except StaleElementReferenceException:
        # 要素がステールになった場合、再取得してリトライ
        pass_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.hover'))
        )
        if pass_button.text == 'パス':
            pass_button.click()


def get_question_elements(driver): 
    question_elements = driver.find_elements(By.CSS_SELECTOR, "section.content")
    return question_elements

def scrape_question_info(driver):
    gray_text = driver.find_element(By.CSS_SELECTOR, ".grayText")
    full_text = gray_text.get_attribute("innerHTML")
    info, ques_num = full_text.split("<br>")
    
    year, ques_num, opt_num = info.split(" ")
    return year, ques_num, opt_num

def scrape_correct_answer(driver):
    kaisetsu_element = driver.find_element(By.CLASS_NAME, "kaisetsu")
    answer_char_element = kaisetsu_element.find_element(By.CLASS_NAME, "answerChar")    
    result = answer_char_element.get_attribute("innerHTML")
    
    if "batu" in result:
        return "誤"
    elif "maru" in result:
        return "正"

def scrape_explanation(driver):
    kaisetsu_element = driver.find_element(By.CLASS_NAME, "kaisetsu")
    kaisetsu = kaisetsu_element.find_element(By.CSS_SELECTOR, "div")
    kaisetsu_text = kaisetsu.get_attribute("innerText") # NOTE: kaisetsu.textでは取得できない(is_displayed() == Falseのため)
    return kaisetsu_text

def scrape_option_text(driver):
    option_element = driver.find_element(By.XPATH, "//section[@class='content']/div/b")
    option_text = option_element.text
    return option_text

def scrape_question_text(driver):
    question_element = driver.find_element(By.XPATH, "//section[@class='content']/div")
    option_text = scrape_option_text(driver)
    question_text = question_element.text.strip(option_text).strip()
    return question_text

def collect_question_data(driver):
    year, ques_num, opt_num = scrape_question_info(driver)
    question_text = scrape_question_text(driver)
    option_text = scrape_option_text(driver)
    answer = scrape_correct_answer(driver)
    kaisetsu = scrape_explanation(driver)
    
    question_data = {
        "year": year,
        "question_number": ques_num,
        "option_number": opt_num,
        "question_text": question_text,
        "option_text": option_text,
        "answer": answer,
        "kaisetsu": kaisetsu
    }
    return question_data

def write_data_to_csv(driver, num_questions, filename='takken_questions.csv'):
    fieldnames = ["year", "question_number", "option_number", "question_text", "option_text", "answer", "kaisetsu"]
    
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file: # windows環境ではnewline=''としておくと安全らしい
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(num_questions):
            logging.debug(f'{i = }, {driver.title = }')
            # print(driver.title)
            # print(check_title(driver))

            data_dic = collect_question_data(driver)
            writer.writerow(data_dic) 
            
            click_next_button(driver)

def check_title(driver):
    if driver.title == '宅建士 一問一答道場🥋｜宅建試験ドットコム':
        return True
    else:
        return False
    # print(driver.title)

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://takken-siken.com/marubatu.php')
    
    # # 広告を削除するためのJavaScriptを実行
    # remove_ads_script = """
    #     var ads = document.querySelectorAll('ins.adsbygoogle, iframe, .ads_content');
    #     ads.forEach(function(ad) {
    #         ad.remove();
    #     });
    # """
    # driver.execute_script(remove_ads_script)
        
    click_start_button(driver)
    
    sfile = driver.get_screenshot_as_file('data/screenshot.png')
    
    for _ in range(50):
        if not check_title:
            print(f'{check_title = }')
            driver.back()


        click_pass_button(driver)
        time.sleep(0.5)

        click_next_button(driver)
        # time.sleep(1)

    # write_data_to_csv(driver, num_questions=20, filename="./data/sample.csv")
    
    driver.quit()
    
        
if __name__ == "__main__":
    main()