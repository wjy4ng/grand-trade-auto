from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

class SpamHamModel:
    def __init__(self, df):
        X = df['메일제목']  # 컬럼명으로 직접 선택
        y = df['메일종류'].map({'햄': 0, '스팸': 1})  # 컬럼명으로 직접 선택
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.vectorizer = CountVectorizer()
        self.X_train_vec = self.vectorizer.fit_transform(X_train)
        self.X_test_vec = self.vectorizer.transform(X_test)
        self.y_train = y_train
        self.y_test = y_test
        self.model = None

    def train(self):
        self.model = LogisticRegression()
        self.model.fit(self.X_train_vec, self.y_train)

    def evaluate(self):
        if self.model is not None:
            from sklearn.metrics import confusion_matrix, classification_report
            print(confusion_matrix(self.y_test, self.model.predict(self.X_test_vec)))
            print(self.model.score(self.X_test_vec, self.y_test))
            print(classification_report(self.y_test, self.model.predict(self.X_test_vec)))
        else:
            print("모델이 아직 학습되지 않았습니다.")