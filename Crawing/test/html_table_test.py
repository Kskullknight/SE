from util import html_table_to_markdown

def test_func(html_):
    print(html_table_to_markdown(html_))

full_html_data = """
<div>
    <p>- 데이터 구축 규모 및 분포</p>
    
    <table cellspacing="0">
    <caption>데이터 구축 규모 및 분포</caption>
    <thead>
            <tr>
                <th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">구분</span></span></th>
                <th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">규모</span></span></th>
                <th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">파일 형태</span></span></th>
            </tr>
    </thead>
        <tbody>
            <tr>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">CT</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">2D 이미지 18,750장</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG, JSON</span></span></td>
            </tr>
            <tr>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">MRI</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">2D 이미지 18,750장</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG, JSON</span></span></td>
            </tr>
            <tr>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">CTA</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">2D 이미지 18,750장</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG, JSON</span></span></td>
            </tr>
            <tr>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">MRA</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">2D 이미지 18,750장</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG, JSON</span></span></td>
            </tr>
        </tbody>
    </table>
    
    <p>&nbsp;</p>
    
    <p>- 클래스별 데이터 비율</p>
    
    <table cellspacing="0">
    <caption>클래스별 데이터 비율</caption>
    <thead>
            <tr>
                <th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">데이터명</span></span></th>
                <th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">세부 데이터명</span></span></th>
                <th colspan="2" style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:120pt"><span style="color:#4e5f70"><span style="font-size:16px">원천데이터 구분</span></span></th>
                <th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">구축 비율</span></span></th>
            </tr>
    </thead>
        <tbody>
            <tr>
                <td rowspan="10" style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">경동맥 혈관 CT 및 MRI 데이터</span></span></td>
                <td rowspan="10" style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">MRI/MRA/CT/CTA 데이터</span></span></td>
                <td rowspan="4" style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">중증도별</span></span></td>
                <td style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Normal<br>
                (정상)</span></span></td>
                <td style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">10.00%</span></span></td>
            </tr>
            <tr>
                <td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Mild Stenosis</span></span></td>
                <td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">35.00%</span></span></td>
            </tr>
            <tr>
                <td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Moderate Stenosis</span></span></td>
                <td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">30.00%</span></span></td>
            </tr>
            <tr>
                <td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Severe Stenosis</span></span></td>
                <td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">25.00%</span></span></td>
            </tr>
            <tr>
                <td rowspan="2" style="height:58.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">협착위치별</span></span></td>
                <td style="height:58.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Common Carotid Artery (CCA)</span></span></td>
                <td style="height:58.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">15.00%</span></span></td>
            </tr>
            <tr>
                <td style="height:43.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Internal Carotid Artery (ICA)</span></span></td>
                <td style="height:43.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">85.00%</span></span></td>
            </tr>
            <tr>
                <td rowspan="4" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">장비별</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Philips</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">5.00%</span></span></td>
            </tr>
            <tr>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Simens</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">40.00%</span></span></td>
            </tr>
            <tr>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">GE</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">50.00%</span></span></td>
            </tr>
            <tr>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">기타</span></span></td>
                <td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">5.00%</span></span></td>
            </tr>
        </tbody>
    </table>
</div>
"""

table_html_1 = """
<table cellspacing="0">
<caption>데이터 구축 규모 및 분포</caption>
<thead>
		<tr>
			<th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">구분</span></span></th>
			<th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">규모</span></span></th>
			<th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">파일 형태</span></span></th>
		</tr>
</thead>
	<tbody>
		<tr>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">CT</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">2D 이미지 18,750장</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG, JSON</span></span></td>
		</tr>
		<tr>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">MRI</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">2D 이미지 18,750장</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG, JSON</span></span></td>
		</tr>
		<tr>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">CTA</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">2D 이미지 18,750장</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG, JSON</span></span></td>
		</tr>
		<tr>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">MRA</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">2D 이미지 18,750장</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG, JSON</span></span></td>
		</tr>
	</tbody>
</table>
"""
table_html_2 = """
<table cellspacing="0">
<caption>클래스별 데이터 비율</caption>
<thead>
		<tr>
			<th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">데이터명</span></span></th>
			<th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">세부 데이터명</span></span></th>
			<th colspan="2" style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:120pt"><span style="color:#4e5f70"><span style="font-size:16px">원천데이터 구분</span></span></th>
			<th style="background-color:#ddebf7; height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">구축 비율</span></span></th>
		</tr>
</thead>
	<tbody>
		<tr>
			<td rowspan="10" style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">경동맥 혈관 CT 및 MRI 데이터</span></span></td>
			<td rowspan="10" style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:114pt"><span style="color:#4e5f70"><span style="font-size:16px">MRI/MRA/CT/CTA 데이터</span></span></td>
			<td rowspan="4" style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">중증도별</span></span></td>
			<td style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Normal<br>
			(정상)</span></span></td>
			<td style="height:34.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">10.00%</span></span></td>
		</tr>
		<tr>
			<td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Mild Stenosis</span></span></td>
			<td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">35.00%</span></span></td>
		</tr>
		<tr>
			<td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Moderate Stenosis</span></span></td>
			<td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">30.00%</span></span></td>
		</tr>
		<tr>
			<td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Severe Stenosis</span></span></td>
			<td style="height:29.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">25.00%</span></span></td>
		</tr>
		<tr>
			<td rowspan="2" style="height:58.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">협착위치별</span></span></td>
			<td style="height:58.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Common Carotid Artery (CCA)</span></span></td>
			<td style="height:58.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">15.00%</span></span></td>
		</tr>
		<tr>
			<td style="height:43.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Internal Carotid Artery (ICA)</span></span></td>
			<td style="height:43.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">85.00%</span></span></td>
		</tr>
		<tr>
			<td rowspan="4" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">장비별</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Philips</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">5.00%</span></span></td>
		</tr>
		<tr>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Simens</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">40.00%</span></span></td>
		</tr>
		<tr>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">GE</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">50.00%</span></span></td>
		</tr>
		<tr>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">기타</span></span></td>
			<td style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">5.00%</span></span></td>
		</tr>
	</tbody>
</table>
"""
table_html_3 = """
<table cellspacing="0">
<caption>데이터 구성</caption>
<thead>
		<tr>
			<th style="background-color:#ddebf7; height:23.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">데이터명</span></span></th>
			<th style="background-color:#ddebf7; height:23.0pt; text-align:center; vertical-align:middle; white-space:normal; width:53pt"><span style="color:#4e5f70"><span style="font-size:16px">세부 데이터명</span></span></th>
			<th style="background-color:#ddebf7; height:23.0pt; text-align:center; vertical-align:middle; white-space:normal; width:110pt"><span style="color:#4e5f70"><span style="font-size:16px">AI 모델 Task</span></span></th>
			<th style="background-color:#ddebf7; height:23.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">어노테이션 방법</span></span></th>
			<th style="background-color:#ddebf7; height:23.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">주요 어노테이션 속성&nbsp;</span></span></th>
			<th style="background-color:#ddebf7; height:23.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">속성 설명</span></span></th>
			<th style="background-color:#ddebf7; height:23.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">라벨링 데이터 포맷</span></span></th>
		</tr>
</thead>
	<tbody>
		<tr>
			<td rowspan="8" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">경동맥 혈관 CT 및 MRI 데이터</span></span></td>
			<td rowspan="4" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:53pt"><span style="color:#4e5f70"><span style="font-size:16px">MRI 데이터</span></span></td>
			<td rowspan="4" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:110pt"><span style="color:#4e5f70"><span style="font-size:16px">Object Detection, Segmentation, Classification</span></span></td>
			<td rowspan="4" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">BBox, Polygon</span></span></td>
			<td rowspan="2" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">bbox</span></span></td>
			<td rowspan="2" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">협착부위 바운딩박스 정보<br>
			(좌표,라벨값)</span></span></td>
			<td rowspan="4" style="height:17.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">JSON</span></span></td>
		</tr>
		<tr>
		</tr>
		<tr>
			<td rowspan="2" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">polygon</span></span></td>
			<td rowspan="2" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">협착부위 바운딩박스 정보<br>
			(좌표,라벨값)</span></span></td>
		</tr>
		<tr>
		</tr>
		<tr>
			<td rowspan="4" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:53pt"><span style="color:#4e5f70"><span style="font-size:16px">CT 데이터</span></span></td>
			<td rowspan="4" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:110pt"><span style="color:#4e5f70"><span style="font-size:16px">Object Detection, Segmentation, Classification</span></span></td>
			<td rowspan="4" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">BBox, Polygon</span></span></td>
			<td rowspan="2" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">bbox</span></span></td>
			<td rowspan="2" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">협착부위 바운딩박스 정보<br>
			(좌표,라벨값)</span></span></td>
			<td rowspan="4" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">JSON</span></span></td>
		</tr>
		<tr>
		</tr>
		<tr>
			<td rowspan="2" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">polygon</span></span></td>
			<td rowspan="2" style="height:16.5pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">협착부위 바운딩박스 정보<br>
			(좌표,라벨값)</span></span></td>
		</tr>
		<tr>
		</tr>
	</tbody>
</table>"""
table_html_4 = """
<table cellspacing="0">
<caption>데이터 구성2</caption>
<thead>
		<tr>
			<th colspan="3" style="background-color:#ddebf7; height:34.0pt; text-align:center; vertical-align:middle; white-space:normal; width:215pt"><span style="color:#4e5f70"><span style="font-size:16px"><strong>번호</strong></span></span></th>
			<th style="background-color:#ddebf7; height:34.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px"><strong>속성명</strong></span></span></th>
			<th style="background-color:#ddebf7; height:34.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px"><strong>속성설명</strong></span></span></th>
			<th style="background-color:#ddebf7; height:34.0pt; text-align:center; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px"><strong>타입</strong></span></span></th>
			<th style="background-color:#ddebf7; height:34.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px"><strong>형식/범위</strong></span></span></th>
			<th style="background-color:#ddebf7; height:34.0pt; text-align:center; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px"><strong>예시</strong></span></span></th>
		</tr>
</thead>
	<tbody>
		<tr>
			<td colspan="3" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:215pt"><span style="color:#4e5f70"><span style="font-size:16px">1</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">image_info</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">이미지정보</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">Object</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="6" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
			<td colspan="2" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">1_1</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">filename</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">파일명</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">[파일명]</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">20230504_123</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">1_2</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">hospital</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">수집병원</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">삼성서울병원</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">1_3</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">file_format</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">파일포맷</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">JPG</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">1_4</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">image_size</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">이미지크기</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">6400KB</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">1_5</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">device</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">촬영장비정보</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">SS900N</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">1_6</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">resolution</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">해상도</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">1920x1080</span></span></td>
		</tr>
		<tr>
			<td colspan="3" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:215pt"><span style="color:#4e5f70"><span style="font-size:16px">2</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">annotation_info</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">어노테이션정보</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">List</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="5" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
			<td colspan="2" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">2_1</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">id</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">어노테이션 ID</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">A_1234567</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">2_2</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">label</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">라벨명</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">plaque</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">2_3</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">bbox_info</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">바운딩박스 정보</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">Objcet</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="2" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:53pt">&nbsp;</td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:110pt"><span style="color:#4e5f70"><span style="font-size:16px">2_3_1</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">id</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">바운딩박스 ID</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:110pt"><span style="color:#4e5f70"><span style="font-size:16px">2_3_2</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">points</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">바운딩박스 좌표</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">List</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="3" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
			<td colspan="2" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">2_4</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">polygon_info</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">폴리곤 정보</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">Object</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:53pt">&nbsp;</td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:110pt"><span style="color:#4e5f70"><span style="font-size:16px">2_4_1</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">id</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">폴리곤 ID</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:110pt"><span style="color:#4e5f70"><span style="font-size:16px">2_4_2</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">points</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">폴리곤 좌표정보</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">List</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td colspan="3" style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:215pt"><span style="color:#4e5f70"><span style="font-size:16px">3</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">patient_info</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">환자 메타정보</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">Object</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:29.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="4" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt">&nbsp;</td>
			<td colspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">3_1</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">code</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">환자번호</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">SS000001</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">3_2</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">age</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">연령대</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">30대</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">3_3</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">sex</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">성별</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">M</span></span></td>
		</tr>
		<tr>
			<td colspan="2" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:163pt"><span style="color:#4e5f70"><span style="font-size:16px">3_4</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">c_date</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">검사연월</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">YYYYMM</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">202305</span></span></td>
		</tr>
		<tr>
			<td colspan="3" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:215pt"><span style="color:#4e5f70"><span style="font-size:16px">4</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">severity</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">중증도</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">Moderate</span></span></td>
		</tr>
		<tr>
			<td colspan="3" style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:215pt"><span style="color:#4e5f70"><span style="font-size:16px">5</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">location</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">협착위치</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:68pt"><span style="color:#4e5f70"><span style="font-size:16px">String</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">-</span></span></td>
			<td style="height:17.0pt; text-align:justify; vertical-align:middle; white-space:normal; width:52pt"><span style="color:#4e5f70"><span style="font-size:16px">ICA, CCA</span></span></td>
		</tr>
	</tbody>
</table>"""

test_func(table_html_4)