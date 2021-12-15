import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir='data'):
    """Return CSV file path to given ticker symbol."""
    return os.path.join(base_dir, f'{symbol}.csv')

def get_data(symbols, dates):
    """Read stock data (Adj Close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')