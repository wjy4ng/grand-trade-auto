from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def model_init(df):
    X = df.iloc[:, '메일제목']
    y = df.iloc[:, '메일종류']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def model_training(X_train, X_test, y_train, y_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def model_evaluation(X_test, y_test, model):
    model.score(X_test, y_test)