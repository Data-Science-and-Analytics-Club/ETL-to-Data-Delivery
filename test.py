import pandas as pd
import numpy as np

df = pd.read_csv('stock_data2.csv')
print(df.isna().sum())
columns_to_fill = df.columns[df.isna().any()].tolist()
def FillMissingValues(df):

    # columns_to_fill = df.columns[df.isna().any()].tolist()

    for column in columns_to_fill:
        
        for i in range(1, len(df) - 1):

            if pd.isna(df.loc[i, column]):  
                value_above = df.loc[i - 1, column] 
                value_below = df.loc[i + 1, column]  
                
                if pd.notna(value_above) and pd.notna(value_below):
                    df.loc[i, column] = (value_above + value_below) / 2
                elif pd.notna(value_above):
                    df.loc[i, column] = value_above

                elif pd.notna(value_below):
                    df.loc[i, column] = value_below
    
    return df


df_filled = FillMissingValues(df)


print(df_filled.isna().sum())




def nike_dataset(data):
    top_10_by_avg_rating = data.groupby('name')['avg_rating'].mean().sort_values(ascending=False).head(10)
    print(top_10_by_avg_rating)
    availability_counts = data['availability'].value_counts()
    print(availability_counts)
    top_10_by_num_reviews = data['review_count'].value_counts().head(10)
    print(top_10_by_num_reviews)