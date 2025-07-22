import pandas as pd
import numpy as np

def read_csv_and_preprocessing():
    # --- 데이터 준비 ---
    try:
        print('예제용 더미 데이터를 생성합니다.')
        data = {
            '제조사': ['현대', '기아', '현대', 'BMw', '벤츠', '기아', 'BMW', '현대'],
            '모델명': ['소나타', 'K5', '아반떼', '3시리즈', 'E클래스', 'K7', '5시리즈', '그랜저'],
            '연식': [2018, 2019, 2020, 2017, 2021, 2018, 2020, 2022],
            '주행거리': [80000, 60000, 30000, 90000, 15000, 75000, 40000, 10000],
            '가격': [1800, 2200, 2100, 2800, 6500, 2500, 5500, 4500]
        }
        df = pd.DataFrame(data)
    except Exception as e:
        print(f'error: {e}')
        exit()
    print('--- 데이터 샘플 ---')
    print(df.head())

    # --- 1. 데이터 정체 및 전처리 ---
    print('\n--- 1. 데이터 정제 및 전처리 시작 ---')

    # 1-1. 결측치 제거
    print(f'\n결측치 제거 전 데이터 수: {len(df)}')
    df.dropna(inplace=True)
    print(f'결측치 제거 후 데이터 수: {len(df)}')

    # 1-2. 오탈자 제거
    df['제조사'] = df['제조사'].replace('BMw', 'BMW')
    print('\n오탈자 수정 확인:')
    print(df['제조사'].value_counts())

    # 1-3. 데이터 정제
    Q1 = df['주행거리'].quantile(0.25)
    Q3 = df['주행거리'].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    print(f'\n주행거리 이상치 상한 기준: {upper_bound}')
    df['주행거리'] = np.where(df['주행거리'] > upper_bound, upper_bound, df['주행거리'])
    print(f'이상치 처리 후 주행거리 최대값: {df['주행거리'].max()}')

    # 1-4. 파생변수 생성
    current_year = 2025
    df['차량나이'] = current_year - df['연식']
    df.drop('연식', axis=1, inplace=True)
    print("\n'차량나이' 파생변수 생성 확인:")
    print(df.head())

    # 1-5. XGBoost 사용을 위한 데이터 변환 (범주형 -> 숫자형)
    df_encoded = pd.get_dummies(df, columns=['제조사', '모델명'], drop_first=False)
    print("\n--- 최종 전처리 완료된 데이터 ---")
    print(df_encoded.head())

    return df_encoded