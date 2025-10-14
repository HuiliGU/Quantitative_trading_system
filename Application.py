import Backtester
import DataHandler
import Strategy
import Broker
import Analyzer

class Application:
    def __init__(self, data_file):
        self.data_handler = DataHandler.DataHandler(data_file)
        self.strategy = Strategy.MovingAverageCrossOver()
        self.broker = Broker.Broker()
        self.analyzer = Analyzer.Analyzer()
        self.backtester = Backtester.Backtester(
            self.data_handler, self.strategy, self.broker, self.analyzer
        )

    def run(self):
        self.backtester.run()


if __name__ == "__main__":
    app = Application('data/sample_data.csv')
    app.run()