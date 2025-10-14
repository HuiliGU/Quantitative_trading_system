class Backtester:
    def __init__(self, data_handler, strategy, broker, analyzer):
        self.data_handler = data_handler
        self.strategy = strategy
        self.broker = broker
        self.analyzer = analyzer

    def run(self):
        for t, row in self.data_handler.stream_data():
            signal = self.strategy.generate_signal(row)
            self.broker.execute_signal(signal, row)
            self.analyzer.record(row, self.broker)

        self.analyzer.report()