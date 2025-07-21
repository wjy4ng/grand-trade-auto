import pandas as pd

def read_csv_file():
    df = pd.read_csv('./ham_spam_list.csv')
    return df