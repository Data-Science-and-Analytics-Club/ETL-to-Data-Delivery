import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock_data.csv")

df['Date'] = pd.to_datetime(df['Date'])
'''
----------->Start Coding from Here<-----------
'''
#Check if missing Values Exists
# Hint : df.isna().sum()
#identify the columns that have missing values and store it in the list :  column_to_be_filled = []
columns_to_fill = ['Open','High','Low','Close','Volume']
def FillMissingValues(df):
    pass
    '''
    Fill this Function to fill the missing Values. 

    TO fill the missing values : 
        iterate over the column_to_be filled : 
            iterate over the rows (use len(df)) :
                location of a cell --> df.loc[i, col]
                where i is the row and col in the column 

                if cell is empty (Check using pd.isna()): 
                    if cell above and cell below the empty cell are not empty then (check using pd.notna()):
                            Fill the empty cell with Average of above and below cell.
                    else :
                        if only above cell is not empty  (check using pd.notna()):
                            fill the empty cell with the value that of above cell 
                        if only the below cell is not empty (check using pd.notna()):
                            fill the empty cell with the value that of the below cell
    '''

#--------->do not edit this part-----------
if not df.isna().values.any() :
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['High'], label='High Price', color='b', marker='o')


    plt.title('Stock High Price Over Time', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Closing Price (USD)', fontsize=12)


    plt.xticks(rotation=45)


    plt.grid(True)
    plt.legend()

    plt.tight_layout()  
    plt.show()
else :
    print("Error : Missing Values in the DataFrame")