from src.preprocessing import read_csv_and_preprocessing
from src.model import model_init, model_training, model_evaluation

class App:
    def __init__(self):
        self.df = read_csv_and_preprocessing()
        self.X_train, self.X_test, self.y_train, self.y_test = model_init(self.df)

    def run(self):
        self.model = model_training(self.X_train, self.X_test, self.y_train, self.y_test)
        model_evaluation(self.X_test, self.y_test, self.model)
        
    def test(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
    app.test()