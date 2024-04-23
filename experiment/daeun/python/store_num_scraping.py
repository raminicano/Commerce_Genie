#!/usr/bin/env python

import time
import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# linux 환경에서 필요한 option
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# excutable_path는 chromdriver가 위치한 경로를 적어주면 된다. 
# code와 동일한 경로일 경우 아래처럼 'chromdriver' 만 적어주거나 아예 excutable_path 자체가 없어도 된다. 이해를 위해 써놓았을 뿐. 
# ex) driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome(excutable_path =‘/usr/local/chromedriver', options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)


print('Go Google~!!')
url = 'https://golmok.seoul.go.kr/stateArea.do'
driver.get(url)

driver.find_element(By.XPATH,'//*[@id="stateArea"]/div[2]/div[1]/div/div[2]/button').click()

wait =10
print(str(wait) + '동안 기다립니다.')
time.sleep(wait)

driver.find_element(By.XPATH,'//*[@id="presentSearchMobile"]').click()

wait =10
print(str(wait) + '동안 기다립니다.')
time.sleep(wait)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# body_tag_district = soup.find_all('tr', {'data-tt-id': '27-1'})
# print(body_tag_district)
#
# region_list = []
# region_name = []
# for tr_tag in body_tag_district:
#     td_tags = tr_tag.find_all('td')  # <tr> 태그 내의 모든 <td> 태그 찾기
#     td_texts = [td.text.strip() for td in td_tags]  # 각 <td> 태그의 텍스트 추출하여 리스트에 저장
#     region_list.append(td_texts)
#
# for i in range(len(region_list)):
#     region_name.append(region_list[i][0])
# print(region_name)

option= input("구의 정보 확인과 동의 정보 확인중 선택해주세요: ")
def select(option):
    if option == '구':
        return 0
    else:
        return 1

def select_region_name(num):
    body_tag_district = soup.find_all('tr', {'data-tt-id': f'{num}'})
    print(body_tag_district)

    region_list = []
    region_name = []
    for tr_tag in body_tag_district:
        td_tags = tr_tag.find_all('td')  # <tr> 태그 내의 모든 <td> 태그 찾기
        td_texts = [td.text.strip() for td in td_tags]  # 각 <td> 태그의 텍스트 추출하여 리스트에 저장
        region_list.append(td_texts)

    for i in range(len(region_list)):
        region_name.append(region_list[i][0])
    print(region_name)

def get_district(district_name):
    district_name = district_name.strip()  # 입력된 문자열의 양쪽 공백 제거

    if district_name == "종로구":
        return 2
    elif district_name == "중구":
        return 3
    elif district_name == "용산구":
        return 4
    elif district_name == "성동구":
        return 5
    elif district_name == "광진구":
        return 6
    elif district_name == "동대문구":
        return 7
    elif district_name == "중량구":
        return 8
    elif district_name == "성북구":
        return 9
    elif district_name == "강북구":
        return 10
    elif district_name == "도봉구":
        return 11
    elif district_name == "노원구":
        return 12
    elif district_name == "은평구":
        return 13
    elif district_name == "서대문구":
        return 14
    elif district_name == "마포구":
        return 15
    elif district_name == "양천구":
        return 16
    elif district_name == "강서구":
        return 17
    elif district_name == "구로구":
        return 18
    elif district_name == "금천구":
        return 19
    elif district_name == "영등포구":
        return 20
    elif district_name == "동작구":
        return 21
    elif district_name == "관악구":
        return 22
    elif district_name == "서초구":
        return 23
    elif district_name == "강남구":
        return 24
    elif district_name == "송파구":
        return 25
    elif district_name == "강동구":
        return 26
    else:
        return None  #입력된 구가 없는 경우 None 반환


def get_region(region_name):
    region_name = region_name.strip()
    list1= ["청운효자동", "사직동", "삼천동", "부암동", "평창동", "무악동", "교남동", "가회동","종로1,2,3,4가동", "종로5,6동", "이화동", "혜화동", "창신1동", "창신2동", "창신3동","숭인1동", "숭인2동"]
    list2 = ["소공동", "회현동", "명동", "필동", "장충동", "광희동", "을지로동", "신당동","다산동", "약수동", "청구동", "신당5동", "동화동", "화학동", "중림동"]
    list3 = ['후암동', '용산2가동', '남영동', '청파동', '원효로1동', '원효로2동', '효창동', '용문동', '한강로동', '이촌1동', '이촌2동', '이태원1동', '이태원2동', '한남동', '서빙고동', '보광동', '후암동', '용산2가동', '남영동', '청파동', '원효로1동', '원효로2동', '효창동', '용문동', '한강로동', '이촌1동', '이촌2동', '이태원1동', '이태원2동', '한남동', '서빙고동', '보광동']
    list4 = ['왕십리2동', '왕십리도선동', '마장동', '사근동', '행당1동', '행당2동', '응봉동', '금호1가동', '금호2·3가동', '금호4가동', '옥수동', '성수1가1동', '성수1가2동', '성수2가1동', '성수2가3동', '송정동', '용답동', '왕십리2동', '왕십리도선동', '마장동', '사근동', '행당1동', '행당2동', '응봉동', '금호1가동', '금호2·3가동', '금호4가동', '옥수동', '성수1가1동', '성수1가2동', '성수2가1동', '성수2가3동', '송정동', '용답동']
    list5 = ['화양동', '군자동', '중곡1동', '중곡2동', '중곡3동', '중곡4동', '능동', '광장동', '자양1동', '자양2동', '자양3동', '자양4동', '구의1동', '구의2동', '구의3동', '화양동', '군자동', '중곡1동', '중곡2동', '중곡3동', '중곡4동', '능동', '광장동', '자양1동', '자양2동', '자양3동', '자양4동', '구의1동', '구의2동', '구의3동']
    list6 = ['용신동', '제기동', '전농1동', '전농2동', '답십리1동', '답십리2동', '장안1동', '장안2동', '청량리동', '회기동', '휘경1동', '휘경2동', '이문1동', '이문2동', '용신동', '제기동', '전농1동', '전농2동', '답십리1동', '답십리2동', '장안1동', '장안2동', '청량리동', '회기동', '휘경1동', '휘경2동', '이문1동', '이문2동']
    list7 = ['면목2동', '면목4동', '면목5동', '면목본동', '면목7동', '면목3·8동', '상봉1동', '상봉2동', '중화1동', '중화2동', '묵1동', '묵2동', '망우본동', '망우3동', '신내1동', '신내2동', '면목2동', '면목4동', '면목5동', '면목본동', '면목7동', '면목3·8동', '상봉1동', '상봉2동', '중화1동', '중화2동', '묵1동', '묵2동', '망우본동', '망우3동', '신내1동', '신내2동']
    list8 = ['성북동', '삼선동', '동선동', '돈암1동', '돈암2동', '안암동', '보문동', '정릉1동', '정릉2동', '정릉3동', '정릉4동', '길음1동', '길음2동', '종암동', '월곡1동', '월곡2동', '장위1동', '장위2동', '장위3동', '석관동', '성북동', '삼선동', '동선동', '돈암1동', '돈암2동', '안암동', '보문동', '정릉1동', '정릉2동', '정릉3동', '정릉4동', '길음1동', '길음2동', '종암동', '월곡1동', '월곡2동', '장위1동', '장위2동', '장위3동', '석관동']
    list9 = ['삼양동', '미아동', '송중동', '송천동', '삼각산동', '번1동', '번2동', '번3동', '수유1동', '수유2동', '수유3동', '우이동', '인수동', '삼양동', '미아동', '송중동', '송천동', '삼각산동', '번1동', '번2동', '번3동', '수유1동', '수유2동', '수유3동', '우이동', '인수동']
    list10 = ['창1동', '창2동', '창3동', '창4동', '창5동', '도봉1동', '도봉2동', '쌍문1동', '쌍문2동', '쌍문3동', '쌍문4동', '방학1동', '방학2동', '방학3동', '창1동', '창2동', '창3동', '창4동', '창5동', '도봉1동', '도봉2동', '쌍문1동', '쌍문2동', '쌍문3동', '쌍문4동', '방학1동', '방학2동', '방학3동']
    list11 =['월계1동', '월계2동', '월계3동', '공릉1동', '공릉2동', '하계1동', '하계2동', '중계본동', '중계1동', '중계4동', '중계2·3동', '상계1동', '상계2동', '상계3·4동', '상계5동', '상계6·7동', '상계8동', '상계9동', '상계10동', '월계1동', '월계2동', '월계3동', '공릉1동', '공릉2동', '하계1동', '하계2동', '중계본동', '중계1동', '중계4동', '중계2·3동', '상계1동', '상계2동', '상계3·4동', '상계5동', '상계6·7동', '상계8동', '상계9동', '상계10동']
    list12 = ['녹번동', '불광1동', '불광2동', '갈현1동', '갈현2동', '구산동', '대조동', '응암1동', '응암2동', '응암3동', '역촌동', '신사1동', '신사2동', '증산동', '수색동', '진관동', '녹번동', '불광1동', '불광2동', '갈현1동', '갈현2동', '구산동', '대조동', '응암1동', '응암2동', '응암3동', '역촌동', '신사1동', '신사2동', '증산동', '수색동', '진관동']
    list13 = ['천연동', '북아현동', '충현동', '신촌동', '연희동', '홍제1동', '홍제3동', '홍제2동', '홍은1동', '홍은2동', '남가좌1동', '남가좌2동', '북가좌1동', '북가좌2동', '천연동', '북아현동', '충현동', '신촌동', '연희동', '홍제1동', '홍제3동', '홍제2동', '홍은1동', '홍은2동', '남가좌1동', '남가좌2동', '북가좌1동', '북가좌2동']
    list14 = ['아현동', '공덕동', '도화동', '용강동', '대흥동', '염리동', '신수동', '서강동', '서교동', '합정동', '망원1동', '망원2동', '연남동', '성산1동', '성산2동', '상암동', '아현동', '공덕동', '도화동', '용강동', '대흥동', '염리동', '신수동', '서강동', '서교동', '합정동', '망원1동', '망원2동', '연남동', '성산1동', '성산2동', '상암동']
    list15 = ['목1동', '목2동', '목3동', '목4동', '목5동', '신월1동', '신월2동', '신월3동', '신월4동', '신월5동', '신월6동', '신월7동', '신정1동', '신정2동', '신정3동', '신정4동', '신정6동', '신정7동', '목1동', '목2동', '목3동', '목4동', '목5동', '신월1동', '신월2동', '신월3동', '신월4동', '신월5동', '신월6동', '신월7동', '신정1동', '신정2동', '신정3동', '신정4동', '신정6동', '신정7동']
    list16 = ['염창동', '등촌1동', '등촌2동', '등촌3동', '화곡1동', '화곡2동', '화곡3동', '화곡4동', '화곡본동', '화곡6동', '화곡8동', '가양1동', '가양2동', '가양3동', '발산1동', '우장산동', '공항동', '방화1동', '방화2동', '방화3동', '염창동', '등촌1동', '등촌2동', '등촌3동', '화곡1동', '화곡2동', '화곡3동', '화곡4동', '화곡본동', '화곡6동', '화곡8동', '가양1동', '가양2동', '가양3동', '발산1동', '우장산동', '공항동', '방화1동', '방화2동', '방화3동']
    list17 = ['신도림동', '구로1동', '구로2동', '구로3동', '구로4동', '구로5동', '가리봉동', '고척1동', '고척2동', '개봉1동', '개봉2동', '개봉3동', '오류1동', '오류2동', '수궁동', '항동', '신도림동', '구로1동', '구로2동', '구로3동', '구로4동', '구로5동', '가리봉동', '고척1동', '고척2동', '개봉1동', '개봉2동', '개봉3동', '오류1동', '오류2동', '수궁동', '항동']
    list18=['가산동', '독산1동', '독산2동', '독산3동', '독산4동', '시흥1동', '시흥2동', '시흥3동', '시흥4동', '시흥5동', '가산동', '독산1동', '독산2동', '독산3동', '독산4동', '시흥1동', '시흥2동', '시흥3동', '시흥4동', '시흥5동']
    list19=['영등포본동', '영등포동', '여의동', '당산1동', '당산2동', '도림동', '문래동', '양평1동', '양평2동', '신길1동', '신길3동', '신길4동', '신길5동', '신길6동', '신길7동', '대림1동', '대림2동', '대림3동', '영등포본동', '영등포동', '여의동', '당산1동', '당산2동', '도림동', '문래동', '양평1동', '양평2동', '신길1동', '신길3동', '신길4동', '신길5동', '신길6동', '신길7동', '대림1동', '대림2동', '대림3동']
    list20=['노량진1동', '노량진2동', '상도1동', '상도2동', '상도3동', '상도4동', '흑석동', '사당1동', '사당2동', '사당3동', '사당4동', '사당5동', '대방동', '신대방1동', '신대방2동', '노량진1동', '노량진2동', '상도1동', '상도2동', '상도3동', '상도4동', '흑석동', '사당1동', '사당2동', '사당3동', '사당4동', '사당5동', '대방동', '신대방1동', '신대방2동']
    list21=['보라매동', '청림동', '성현동', '행운동', '낙성대동', '청룡동', '은천동', '중앙동', '인헌동', '남현동', '서원동', '신원동', '서림동', '신사동', '신림동', '난향동', '조원동', '대학동', '삼성동', '미성동', '난곡동', '보라매동', '청림동', '성현동', '행운동', '낙성대동', '청룡동', '은천동', '중앙동', '인헌동', '남현동', '서원동', '신원동', '서림동', '신사동', '신림동', '난향동', '조원동', '대학동', '삼성동', '미성동', '난곡동']
    list22=['서초1동', '서초2동', '서초3동', '서초4동', '잠원동', '반포본동', '반포1동', '반포2동', '반포3동', '반포4동', '방배본동', '방배1동', '방배2동', '방배3동', '방배4동', '양재1동', '양재2동', '내곡동', '서초1동', '서초2동', '서초3동', '서초4동', '잠원동', '반포본동', '반포1동', '반포2동', '반포3동', '반포4동', '방배본동', '방배1동', '방배2동', '방배3동', '방배4동', '양재1동', '양재2동', '내곡동']
    list23=['신사동', '논현1동', '논현2동', '압구정동', '청담동', '삼성1동', '삼성2동', '대치1동', '대치2동', '대치4동', '역삼1동', '역삼2동', '도곡1동', '도곡2동', '개포1동', '개포2동', '개포4동', '세곡동', '일원본동', '일원1동', '일원2동', '수서동', '신사동', '논현1동', '논현2동', '압구정동', '청담동', '삼성1동', '삼성2동', '대치1동', '대치2동', '대치4동', '역삼1동', '역삼2동', '도곡1동', '도곡2동', '개포1동', '개포2동', '개포4동', '세곡동', '일원본동', '일원1동', '일원2동', '수서동']
    list24=['풍납1동', '풍납2동', '거여1동', '거여2동', '마천1동', '마천2동', '방이1동', '방이2동', '오륜동', '오금동', '송파1동', '송파2동', '석촌동', '삼전동', '가락본동', '가락1동', '가락2동', '문정1동', '문정2동', '장지동', '위례동', '잠실본동', '잠실2동', '잠실3동', '잠실4동', '잠실6동', '잠실7동', '풍납1동', '풍납2동', '거여1동', '거여2동', '마천1동', '마천2동', '방이1동', '방이2동', '오륜동', '오금동', '송파1동', '송파2동', '석촌동', '삼전동', '가락본동', '가락1동', '가락2동', '문정1동', '문정2동', '장지동', '위례동', '잠실본동', '잠실2동', '잠실3동', '잠실4동', '잠실6동', '잠실7동']
    list25=['강일동', '상일동', '명일1동', '명일2동', '고덕1동', '고덕2동', '암사1동', '암사2동', '암사3동', '천호1동', '천호2동', '천호3동', '성내1동', '성내2동', '성내3동', '길동', '둔촌1동', '둔촌2동', '강일동', '상일동', '명일1동', '명일2동', '고덕1동', '고덕2동', '암사1동', '암사2동', '암사3동', '천호1동', '천호2동', '천호3동', '성내1동', '성내2동', '성내3동', '길동', '둔촌1동', '둔촌2동']

    if region_name in list1:
        num = "2-1"
        count = list1.index(region_name)
        return num, count
    elif region_name in list2:
        num = "3-1"
        count = list2.index(region_name)
        return num, count
    elif region_name in list3:
        num = "4-1"
        count = list3.index(region_name)
        return num, count
    elif region_name in list4:
        num = "5-1"
        count = list4.index(region_name)
        return num, count
    elif region_name in list5:
        num = "6-1"
        count = list5.index(region_name)
        return num, count
    elif region_name in list6:
        num = "7-1"
        count = list6.index(region_name)
        return num, count
    elif region_name in list7:
        num = "8-1"
        count = list7.index(region_name)
        return num, count
    elif region_name in list8:
        num = "9-1"
        count = list8.index(region_name)
        return num, count
    elif region_name in list9:
        num = "10-1"
        count = list9.index(region_name)
        return num, count
    elif region_name in list10:
        num = "11-1"
        count = list10.index(region_name)
        return num, count
    elif region_name in list11:
        num = "12-1"
        count = list11.index(region_name)
        return num, count
    elif region_name in list12:
        num = "13-1"
        count = list12.index(region_name)
        return num, count
    elif region_name in list13:
        num = "14-1"
        count = list13.index(region_name)
        return num, count
    elif region_name in list14:
        num = "15-1"
        count = list14.index(region_name)
        return num, count
    elif region_name in list15:
        num = "16-1"
        count = list15.index(region_name)
        return num, count
    elif region_name in list16:
        num = "17-1"
        count = list16.index(region_name)
        return num, count
    elif region_name in list17:
        num = "18-1"
        count = list17.index(region_name)
        return num, count
    elif region_name in list18:
        num = "19-1"
        count = list18.index(region_name)
        return num, count
    elif region_name in list19:
        num = "20-1"
        count = list19.index(region_name)
        return num, count
    elif region_name in list20:
        num = "21-1"
        count = list20.index(region_name)
        return num, count
    elif region_name in list21:
        num = "22-1"
        count = list21.index(region_name)
        return num, count
    elif region_name in list22:
        num = "23-1"
        count = list22.index(region_name)
        return num, count
    elif region_name in list23:
        num = "24-1"
        count = list23.index(region_name)
        return num, count
    elif region_name in list24:
        num = "25-1"
        count = list24.index(region_name)
        return num, count
    elif region_name in list25:
        num = "26-1"
        count = list25.index(region_name)
        return num, count

def district_print(body_tag_district):
    district = []
    if body_tag_district:
        td_element_district = body_tag_district.find_all('td')

        for td in td_element_district:
            district.append(td.text)
    else:
        print("no tr")
    print(f"검색한 구의 이름은 {district[0]} 입니다.")
    print('-' * 50)

    wait = 3
    print(f"잠시만 기다려주세요. {district[0]} 의 2021년 4분기 데이터를 불러오고 있습니다...")
    time.sleep(wait)
    print("2021년 4분기 데이터 입니다.")
    print(f"검색한 구의 전체 점포수는  {district[2]} 입니다.")
    print(f"검색한 구의 프랜차이즈 점포수는 {district[3]} 입니다.")
    print(f"검색한 구의 일반 점포수는 {district[4]} 입니다.")

    print('-' * 50)
    print(f"잠시만 기다려주세요. {district[0]} 의 2022년 4분기 데이터를 불러오고 있습니다...")
    time.sleep(wait)
    print("2022년 4분기 데이터 입니다.")
    print(f"검색한 구의 전체 점포수는  {district[5]} 입니다.")
    print(f"검색한 구의 프랜차이즈 점포수는 {district[6]} 입니다.")
    print(f"검색한 구의 일반 점포수는 {district[7]} 입니다.")

    print('-' * 50)
    print(f"잠시만 기다려주세요. {district[0]} 의 2023년 4분기 데이터를 불러오고 있습니다...")
    time.sleep(wait)
    print("2021년 4분기 데이터 입니다.")
    print(f"검색한 구의 전체 점포수는  {district[8]} 입니다.")
    print(f"검색한 구의 프랜차이즈 점포수는 {district[9]} 입니다.")
    print(f"검색한 구의 일반 점포수는 {district[10]} 입니다.")
def region_print(body_tag_region):
    b = get_region(region_name)
    refine= body_tag_region[b[1]]

    region = []
    if refine:
        td_element_region = refine.find_all('td')

        for td in td_element_region:
            region.append(td.text)
    else:
        print("no tr")
    print(f"검색한 동의 이름은 {region[0]} 입니다.")
    print('-' * 50)

    wait = 3
    print(f"잠시만 기다려주세요. {region[0]} 의 2021년 4분기 데이터를 불러오고 있습니다...")
    time.sleep(wait)
    print("2021년 4분기 데이터 입니다.")
    print(f"검색한 동의 전체 점포수는  {region[2]} 입니다.")
    print(f"검색한 동의 프랜차이즈 점포수는 {region[3]} 입니다.")
    print(f"검색한 동의 일반 점포수는 {region[4]} 입니다.")

    print('-' * 50)
    print(f"잠시만 기다려주세요. {region[0]} 의 2022년 4분기 데이터를 불러오고 있습니다...")
    time.sleep(wait)
    print("2022년 4분기 데이터 입니다.")
    print(f"검색한 동의 전체 점포수는  {region[5]} 입니다.")
    print(f"검색한 동의 프랜차이즈 점포수는 {region[6]} 입니다.")
    print(f"검색한 동의 일반 점포수는 {region[7]} 입니다.")

    print('-' * 50)
    print(f"잠시만 기다려주세요. {region[0]} 의 2023년 4분기 데이터를 불러오고 있습니다...")
    time.sleep(wait)
    print("2021년 4분기 데이터 입니다.")
    print(f"검색한 동의 전체 점포수는  {region[8]} 입니다.")
    print(f"검색한 동의 프랜차이즈 점포수는 {region[9]} 입니다.")
    print(f"검색한 동의 일반 점포수는 {region[10]} 입니다.")

selectop = select(option)

if selectop == 0:
    district_input = input("구 이름을 입력하세요: ")
    a = get_district(district_input)
    body_tag_district = soup.find('tr', {'data-tt-id': f'{a}'})
    district_print(body_tag_district)



elif selectop == 1:
    region_name = input("동 이름을 입력하세요: ")
    b = get_region(region_name)
    body_tag_region = soup.find_all('tr', {'data-tt-id': f'{b[0]}'})
    region_print(body_tag_region)

else:
    print("다시 입력을 해주세요 프로그램을 종료합니다")


wait =5
print('프로그램이 종료중입니다')
time.sleep(wait)


driver.quit()
print('Browser Exit~!!')