from src.preprocessing import read_csv_and_preprocessing
from src.model import UsedCarPredictModel
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class App:
    def __init__(self):
        self.df = read_csv_and_preprocessing()
        self.model = UsedCarPredictModel(self.df)

    def run(self):
        self.model.train()
        self.model.evaluate()
        # 예측용 데이터프레임 예시 (실제 예측하려는 값으로 수정 필요)
        import pandas as pd
        input_df = pd.DataFrame([{
            '제조사': 0,      # LabelEncoder로 변환된 값이어야 함
            '모델명': 1,      # LabelEncoder로 변환된 값이어야 함
            '주행거리': 50000,
            '차량나이': 3
        }])
        pred = self.model.predict(input_df)
        print("예측 결과:", pred)
        pass
        

if __name__ == "__main__":
    app = App()
    app.run()