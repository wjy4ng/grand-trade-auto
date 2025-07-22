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
            '제조사': "포르쉐",
            '모델명': "카이엔 (PO536) 3.0",
            '주행거리': 68473,
            '연식': 2020
            # 실제 올라온 중고가: 4,390만원
        }])
        pred = self.model.predict(input_df)
        print("예측 결과:", pred)
        

if __name__ == "__main__":
    app = App()
    app.run()
    app.test()