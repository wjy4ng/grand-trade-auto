import pandas as pd


def read_csv_and_preprocessing():
    df = pd.read_csv('./ham_spam_list.csv')
    df = df[['메일종류', '메일제목']]
    return df