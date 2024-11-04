from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from util import html_table_to_markdown

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from langchain.schema import Document

ignore_chapter = ["교육활용 동영상", "저작도구"]

def wait_for_page_to_load(driver, timeout=10) -> None:
    """
    페이지의 요소가 로딩될 때 까지 기다려주는 함수

    :param driver: 대기할 드라이버
    :param timeout: 시간초과 값 기본값 = 10sec
    :return: None
    """
    wait = WebDriverWait(driver, timeout)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

def get_section_data(driver) -> list:
    """
    데이터셋 페이지에 있는 데이터를 Document 리스트로 반환

    :param driver: 페이지가 열려있는 드라이버
    :return: Document_List
    """
    dataset_info_docs = []

    content = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "dataContent"))
    )

    content = content.find_elements(By.TAG_NAME, "li")
    for section in content:
        section.click()
        result = str()

        chapter = section.find_element(By.TAG_NAME, 'h3').text
        if chapter in ignore_chapter:
            continue

        detail = section.find_element(By.TAG_NAME, "div")

        child_elements = detail.find_elements(By.XPATH, "./*")
        for child in child_elements:
            if child.tag_name == "table":
                result += html_table_to_markdown(child.get_attribute('outerHTML')) + "\n"
            else:
                result += child.text + "\n"

        doc = Document(
            page_content=result,
            metadata={
                "source": driver.current_url,
            }
        )

        dataset_info_docs.append(doc)

    return dataset_info_docs

def process_page(url: str, driver_) -> list:
    """
    데이터 찾기 페이지를 처리하는 함수

    :param url: 페이지 링크
    :param driver_:페이지가 열린 드라이버
    :return: 페이지에 있는 데이터 셋의 Document_List의 List
    """
    result = []

    # 웹 드라이버 설정
    service = Service(ChromeDriverManager().install())
    driver_func = webdriver.Chrome(service=service)

    # 페이지의 주소를 받음
    driver_.get(url)
    wait_for_page_to_load(driver_, timeout=10)

    # 페이지 내의 모든 데이터 셋을 원소를 선택
    elements = driver_.find_element(By.CLASS_NAME, "dataList").find_elements(By.TAG_NAME, "li")

    for element in elements:
        driver_func.get(element.find_element(By.TAG_NAME, "a").get_attribute("href"))
        wait_for_page_to_load(driver_, timeout=10)

        result.append(get_section_data(driver_func))

    return result