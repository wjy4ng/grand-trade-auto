import pandas as pd

def read_csv_and_preprocessing():
    # csv 파일 읽기
    df = pd.read_csv('./ham_spam_list.csv')

    # 필요한 열만 추출
    df = df[['메일종류', '메일제목']]

    return df