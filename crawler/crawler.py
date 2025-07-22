from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

driver = webdriver.Chrome()  # 크롬드라이버 경로 필요시 인자 추가

# 크롬드라이버 타임아웃 설정
try:
    driver.set_page_load_timeout(15)  # 페이지 로딩 최대 15초
except Exception as e:
    print("set_page_load_timeout 지원 안함:", e)

cars = []

for page in range(1, 601):  # 1~600페이지
    url = f"https://car.encar.com/list/car?page={page}&search=%7B%22type%22%3A%22car%22%2C%22action%22%3A%22(And.Hidden.N._.CarType.A.)%22%2C%22title%22%3A%22%EA%B5%AD%EC%82%B0%C2%B7%EC%88%98%EC%9E%85%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22MobileModifiedDate%22%7D"
    try:
        driver.get(url)
        time.sleep(2 + random.uniform(0, 1.5))  # 2~3.5초 랜덤 대기

        # 각 차량 아이템의 HTML 추출
        items = driver.find_elements(By.CSS_SELECTOR, ".ItemBigImage_item__6bPnX")
        for item in items:
            html = item.get_attribute('outerHTML')
            soup = BeautifulSoup(html, "html.parser")
            try:
                # 차량명에서 제조사, 모델명 분리
                car_name = soup.select_one("strong.ItemBigImage_name__h0biK").text.strip()
                maker = car_name.split()[0]
                model = car_name[len(maker):].strip()

                info_list = soup.select("ul.ItemBigImage_info__YMI5y li")
                year = info_list[0].text.strip()      # 21/06식
                mileage = info_list[1].text.strip()   # 85,408km

                price = soup.select_one("span.ItemBigImage_num__Fu15_").text.strip() + "만원"

                cars.append({
                    "제조사": maker,
                    "모델명": model,
                    "연식": year,
                    "주행거리": mileage,
                    "가격": price
                })
            except Exception as e:
                print(f"차량 정보 파싱 에러: {e}")
    except Exception as e:
        print(f"{page}페이지에서 에러 발생: {e}")
        continue

driver.quit()

df = pd.DataFrame(cars)
df.to_csv("encar_cars.csv", index=True, index_label="번호")