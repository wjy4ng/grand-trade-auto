from src.preprocessing import read_csv_and_preprocessing
from src.model import UsedCarPredictModel

class App:
    def __init__(self):
        self.df = read_csv_and_preprocessing()
        self.model = UsedCarPredictModel(self.df)

    def run(self):
        #self.model.train()
        #self.model.evaluate()
        #self.model.predict()
        pass
        
    def test(self):
        user_input = input("메일 제목을 입력하세요: ")
        input_vec = self.model.vectorizer.transform([user_input])
        pred = self.model.model.predict(input_vec)[0]
        if pred == 1:
            print("스팸")
        else:
            print("햄")


if __name__ == "__main__":
    app = App()
    app.run()
    #app.test()