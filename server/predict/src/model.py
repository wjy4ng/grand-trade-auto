from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy.sparse import hstack
import numpy as np

class UsedCarPredictModel:
    def __init__(self, df):
        print("\n--- 2. 모델링 시작 ---")

        # 문자열로 변환 (오류 방지)
        df['제조사'] = df['제조사'].astype(str)
        df['모델명'] = df['모델명'].astype(str)

        # 벡터화 준비
        self.manufacturer_vec = CountVectorizer()
        self.model_vec = CountVectorizer()

        # 벡터화 수행 (fit_transform은 학습할 때만 사용)
        manufacturer_features = self.manufacturer_vec.fit_transform(df['제조사'])
        model_features = self.model_vec.fit_transform(df['모델명'])

        # 수치형 데이터
        numeric_features = df[['주행거리', '연식']].reset_index(drop=True)

        # 최종 입력 X 구성
        X = hstack([manufacturer_features, model_features, numeric_features])
        y = df['가격']

        # 학습/테스트 분리
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = None

    def train(self):
        self.model = XGBRegressor()
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        if self.model is not None:
            y_pred = self.model.predict(self.X_test)
            print("MSE:", mean_squared_error(self.y_test, y_pred))
            print("RMSE:", np.sqrt(mean_squared_error(self.y_test, y_pred)))
            print("MAE:", mean_absolute_error(self.y_test, y_pred))
            print("R2 Score:", r2_score(self.y_test, y_pred))
        else:
            print("모델이 아직 학습되지 않았습니다.")

    def predict(self, input_df):
        """
        input_df: '제조사', '모델명', '주행거리', '연식' 컬럼을 가진 DataFrame
        return: 예측된 가격(np.ndarray)
        """
        if not hasattr(self, 'model') or self.model is None:
            print("모델이 아직 학습되지 않았습니다. 먼저 train()을 실행하세요.")
            return None

        # 벡터화
        manufacturer_features = self.manufacturer_vec.transform(input_df['제조사'])
        model_features = self.model_vec.transform(input_df['모델명'])
        numeric_features = input_df[['주행거리', '연식']].reset_index(drop=True)
        X_input = hstack([manufacturer_features, model_features, numeric_features])
        
        return self.model.predict(X_input)