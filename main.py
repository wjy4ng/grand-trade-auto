from src.preprocessing import read_csv_and_preprocessing
from src.model import model_init, model_training, model_evaluation

class App:
    def __init__(self):
        model_init()

    def run(self):
        read_csv_and_preprocessing()
        model_training()
        model_evaluation()
        
    def test(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
    app.test()