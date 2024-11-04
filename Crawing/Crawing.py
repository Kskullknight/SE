from selenium.webdriver.common.by import By

from page import process_page
from util import link_page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def crawing() -> list:
    result = []

    # 웹 드라이버 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    page = 1

    while True:
        # 웹사이트 열기
        driver.get(link_page(page))
        try:
            driver.find_element(By.CLASS_NAME, "dataNone")
            break
        except:
            result += process_page(link_page(page), driver)
            page += 1

    # 브라우저 닫기
    driver.quit()

    return result