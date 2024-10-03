import matplotlib.pyplot as plt
import pandas as pd 
# Load the cleaned dataset
data = pd.read_csv('cleaned_nike_data.csv')

'''
You have been provided with the Nike_Dataset Clean the Dataset By removing redudant columns 
These are the only columns we need = [name,	sub_title,	brand,	model,	color,	price,	currency, availability, avg_rating]
'''

'''
After removal of reduant columns these are the metrics we need :
-> Avaliable Unique Colours
-> Top 10 products by average rating 
-> Total review count 
-> Average Price 
-> Use Pandas to analyze the availability_counts variable, displaying the number of 'In Stock' and 'Out of Stock' products.
'''


availability_counts = None

if not availability_counts.empty:
    plt.figure(figsize=(8, 5))
    plt.bar(availability_counts.index, availability_counts.values, color='salmon')
    plt.title("Product Availability (In Stock vs Out Of Stock)")
    plt.xlabel("Availability")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()