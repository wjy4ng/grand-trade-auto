from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

class UsedCarPredictModel:
    def __init__(self, df):
        print("\n--- 2. 모델링 시작 ---")

        # 2-1. 변수 정의
        X = df[['제조사', '모델명', '주행거리', '차량나이']]
        y = df['가격']

        # 2-2. 학습, 검증, 테스트 데이터셋 분리
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train(self):
        self.model = XGBRegressor()
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        if self.model is not None:
            from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
            import numpy as np
            y_pred = self.model.predict(self.X_test)
            print("MSE:", mean_squared_error(self.y_test, y_pred))
            print("RMSE:", np.sqrt(mean_squared_error(self.y_test, y_pred)))
            print("MAE:", mean_absolute_error(self.y_test, y_pred))
            print("R2 Score:", r2_score(self.y_test, y_pred))
        else:
            print("모델이 아직 학습되지 않았습니다.")

    def predict(self, input_df):
        """
        input_df: '제조사', '모델명', '주행거리', '차량나이' 컬럼을 가진 DataFrame
        return: 예측된 가격(np.ndarray)
        """
        if not hasattr(self, 'model') or self.model is None:
            print("모델이 아직 학습되지 않았습니다. 먼저 train()을 실행하세요.")
            return None
        # 입력 데이터에서 필요한 컬럼만 추출
        X_input = input_df[['제조사', '모델명', '주행거리', '차량나이']]
        return self.model.predict(X_input)