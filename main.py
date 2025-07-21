from src.read_csv import read_csv_file
from src.preprocessing import data_preprocessing
from src.model import model_init, model_training, model_evaluation

class App:
    def __init__(self):
        model_init()

    def run(self):
        read_csv_file()
        data_preprocessing()
        model_training()
        model_evaluation()
        
    def test(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
    app.test()