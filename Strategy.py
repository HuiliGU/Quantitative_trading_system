class MovingAverageCrossOver:
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window
    
    def generate_signal(self, data):
        if 'SMA_short' not in data or 'SMA_long' not in data:
            return None 

        if data['SMA_short'] > data['SMA_long']:
            return 'BUY'
        elif data['SMA_short'] < data['SMA_long']:
            return 'SELL'
        
        return None 