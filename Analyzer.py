import numpy as np

class Analyzer:
    def __init__(self):
        self.equity_curve = []
    
    def record(self, data, broker):
        returns = np.diff(self.equity_curve)
        sharpe = (
            np.mean(returns) / np.std(returns) * np.sqrt(252)
            if np.std(returns) > 0 else 0
        )
        print(f"最终余额: {self.equity_curve[-1]:.2f}, 夏普比率: {sharpe:.2f}")
