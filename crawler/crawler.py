from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()  # 크롬드라이버 경로 필요시 인자 추가

cars = []

for page in range(1, 6):  # 1~5페이지 예시
    url = f"https://car.encar.com/list/car?page={page}&search=%7B%22type%22%3A%22car%22%2C%22action%22%3A%22(And.Hidden.N._.CarType.A.)%22%2C%22title%22%3A%22%EA%B5%AD%EC%82%B0%C2%B7%EC%88%98%EC%9E%85%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22MobileModifiedDate%22%7D"
    driver.get(url)
    time.sleep(2)  # 페이지 로딩 대기

    items = driver.find_elements(By.CSS_SELECTOR, ".ListItem")  # 실제 클래스명 확인 필요
    for item in items:
        try:
            maker = item.find_element(By.CSS_SELECTOR, ".ListItemMaker").text  # 실제 클래스명 확인 필요
            model = item.find_element(By.CSS_SELECTOR, ".ListItemTitle").text  # 실제 클래스명 확인 필요
            year = item.find_element(By.CSS_SELECTOR, ".ListItemYear").text    # 실제 클래스명 확인 필요
            mileage = item.find_element(By.CSS_SELECTOR, ".ListItemMileage").text  # 실제 클래스명 확인 필요
            price = item.find_element(By.CSS_SELECTOR, ".ListItemPrice").text  # 실제 클래스명 확인 필요
            cars.append({
                "제조사": maker,
                "모델명": model,
                "연식": year,
                "주행거리": mileage,
                "가격": price
            })
        except Exception as e:
            print("Error:", e)

driver.quit()

df = pd.DataFrame(cars)
df.to_csv("encar_cars.csv", index=False)