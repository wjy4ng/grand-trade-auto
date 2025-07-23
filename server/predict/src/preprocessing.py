import pandas as pd
import numpy as np


def read_csv_and_preprocessing():
    # --- 데이터 준비 ---
    try:
        df = pd.read_csv('./predict/dataset/encar_cars.csv', index_col=0)
    except Exception as e:
        print(f'error: {e}')
        exit()
    print('--- 데이터 샘플 ---')
    print(df.head())

    # --- 데이터 정체 및 전처리 ---
    print('\n--- 1. 데이터 정제 및 전처리 시작 ---')

    # 연식, 주행거리, 가격 형식 포맷
    print("\n--- 1-1. 데이터 형식 포맷 전 샘플 ---")
    print(df[['연식', '주행거리', '가격']].head(3))
    df['연식'] = df['연식'].str.extract(r'(\d{2}/)')[0].str.replace('/', '')
    df['주행거리'] = df['주행거리'].str.replace(r'[^0-9]', '', regex=True)
    df['가격'] = df['가격'].str.replace(r'[^0-9]', '', regex=True)
    df.replace('', np.nan, inplace=True)

    # 결측치 제거
    print("\n--- 1-3. 결측치 제거 ---")
    print(f'결측치 제거 전 데이터 수: {len(df)}')
    df.dropna(inplace=True)
    print(f'결측치 제거 후 데이터 수: {len(df)}')

    # 데이터 타입 변환
    df['연식'] = df['연식'].astype(int)
    df['주행거리'] = df['주행거리'].astype(int)
    df['가격'] = df['가격'].astype(int)
    print("\n--- 1-2. 데이터 형식 포맷 후 샘플 ---")
    print(df[['연식', '주행거리', '가격']].head(3))

    return df