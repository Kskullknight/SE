from bs4 import BeautifulSoup

def link_page(page_num: int) -> str:
    # return f"https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex={page_num}&currMenu=115&topMenu=100&dataSetSn=&srchdataClCode=DATACL001&searchKeyword=&srchDetailCnd=DETAILCND001&srchOrder=ORDER001&srchPagePer=20"
    return f"https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex={page_num}&currMenu=115&topMenu=100&dataSetSn=&srchdataClCode=DATACL001&srchDataRealmCode=REALM015&searchKeyword=&srchDetailCnd=DETAILCND001&srchOrder=ORDER001&srchPagePer=20"

from bs4 import BeautifulSoup


def html_table_to_markdown(html: str) -> str:
    """
    HTML Table구조를 markdown 형식을 표로 바꾸는 함수

    :param html: 변환할 HTML 태그
    :return: markdown 표 문자열
    """
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    if not table:
        return "No table found in the HTML."

    # 표의 행 추출
    rows = table.find_all('tr')

    # 헤더 처리
    headers = rows[0].find_all(['th', 'td'])
    header_text = [header.get_text(strip=True) for header in headers]
    markdown_table = "| " + " | ".join(header_text) + " |\n"
    markdown_table += "| " + " | ".join(['---'] * len(header_text)) + " |\n"

    # rowspan 처리를 위한 빈 리스트
    num_columns = len(header_text)
    rowspan_map = [None] * num_columns  # rowspan 정보를 열별로 관리하는 리스트

    # 데이터 행 처리
    for row in rows[1:]:
        cells = row.find_all(['th', 'td'])
        cell_text = []
        cell_index = 0

        for cell in cells:
            # 빈 자리 채우기: rowspan이 있는 셀이 있으면 해당 자리 값을 추가
            while cell_index < num_columns and rowspan_map[cell_index] is not None:
                cell_text.append(rowspan_map[cell_index])
                rowspan_map[cell_index] = None
                cell_index += 1

            # 셀 값 추가
            cell_text.append(cell.get_text(strip=True))

            # rowspan 처리
            rowspan = int(cell.get('rowspan', 1))
            if rowspan > 1:
                for i in range(rowspan - 1):
                    if cell_index + i < len(rowspan_map):
                        rowspan_map[cell_index] = cell.get_text(strip=True)

            cell_index += 1

        # 나머지 빈 자리 채우기
        while cell_index < num_columns and rowspan_map[cell_index] is not None:
            cell_text.append(rowspan_map[cell_index])
            rowspan_map[cell_index] = None
            cell_index += 1

        markdown_table += "| " + " | ".join(cell_text) + " |\n"

    return markdown_table

