class Broker:
    def __init__(self, initial_balance=100000):
        self.balance = initial_balance
        self.position = 0
        self.entry_price = None 
    
    def execute(self, signal, data):
        # 后续加入滑点 slippage 和手续费 commission 和做空 short selling
        price = data['Close']
        if signal == 'BUY' and self.position == 0:
            self.position = 1
            self.entry_price = price
        elif signal == 'SELL' and self.position == 1:
            profit = price - self.entry_price
            self.balance += profit
            self.position = 0
            self.entry_price = None

    
        