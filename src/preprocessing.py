import pandas as pd


def read_csv_and_preprocessing():
    ham = pd.read_csv('./CSV/ham_list.csv')
    spam = pd.read_csv('./CSV/spam_list.csv')
    spam = spam[['메일종류', '메일제목']]

    df = pd.concat([ham, spam], ignore_index=True)
    df.to_csv('./CSV/ham_spam_list.csv', index=False)
    return df