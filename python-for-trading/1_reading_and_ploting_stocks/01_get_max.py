import . pandas.
def get_max_close (symbol):
""
returns company stock max close price 
""
df = pandas. read_csv(f"{symbol}.csv")
return df ['Close'].max()

def main(): 
    print("max close:")
    for symbol in ['AAPL' ,'GS']: 
        print(symbol + ":" , get_maxed_close (symbol))


 if __name__ =="__main__":
     main()