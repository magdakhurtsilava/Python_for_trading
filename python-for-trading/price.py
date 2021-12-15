import pandas 
import matplotlib.pyplot as.plt 

def main():
    df = pandas.read_csv('data/AAPL.csv') 
    print(df) 
    df['Adj Close'].plot ()
    matplotlib matplotlib.pyplot.savefig('graphs/aapl.png')
    

if __name__=="__main__":
    main():