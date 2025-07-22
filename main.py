from src.preprocessing import read_csv_and_preprocessing
from src.model import UsedCarPredictModel
import pandas as pd


class App:
    def __init__(self):
        self.df = read_csv_and_preprocessing()
        self.model = UsedCarPredictModel(self.df)

    def run(self):
        self.model.train()
        self.model.evaluate()

    def test(self):
        input_df = pd.DataFrame([{
            '제조사': "기아",
            '모델명': "쏘렌토 하이브리드(MQ4) 1.6 HEV 4WD",
            '주행거리': 37091,
            '연식': 2023
        }])
        pred = self.model.predict(input_df)
        print("예측 결과:", pred)
        

if __name__ == "__main__":
    app = App()
    app.run()
    app.test()