from page import process_page
from util import link_page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 웹 드라이버 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

data_page = link_page(1)

# 웹사이트 열기
driver.get(data_page)

print(process_page(link_page(1), driver)[0])

# 브라우저 닫기
driver.quit()
