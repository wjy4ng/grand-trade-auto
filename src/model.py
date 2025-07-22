from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

class UsedCarPredictModel:
    def __init__(self, df):
        print("\n--- 2. 모델링 시작 ---")

        # 2-1. 변수 정의
        X = df.drop('가격', axis=1)
        y = df['가격']

        # 2-2. 학습, 검증, 테스트 데이터셋 분리
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
        print(f"\n학습 데이터셋 크기: {X_train.shape}")
        print(f"검증 데이터셋 크기: {X_val.shape}")
        print(f"테스트 데이터셋 크기: {X_test.shape}")

    def train(self):
        self.model = LogisticRegression()
        self.model.fit(self.X_train_vec, self.y_train)

    def evaluate(self):
        if self.model is not None:
            from sklearn.metrics import confusion_matrix, classification_report
            print(confusion_matrix(self.y_test, self.model.predict(self.X_test_vec))) # 정답/오답 개수 표
            print(self.model.score(self.X_test_vec, self.y_test)) # 정확도
            print(classification_report(self.y_test, self.model.predict(self.X_test_vec))) # 정밀도, 재현율 등 상세 성능지표
        else:
            print("모델이 아직 학습되지 않았습니다.")

    def predict(self):
        pass