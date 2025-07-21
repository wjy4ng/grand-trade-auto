from src.preprocessing import read_csv_and_preprocessing
from src.model import SpamHamModel

class App:
    def __init__(self):
        self.df = read_csv_and_preprocessing()
        self.model = SpamHamModel(self.df)

    def run(self):
        self.model.train()
        self.model.evaluate()
        
    def test(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
    app.test()