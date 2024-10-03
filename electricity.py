import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
def load_data(file_path):
    '''
    Load the dataset and remove rows with empty years.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Cleaned dataset without empty year rows.
    '''
    df = pd.read_csv(file_path)
    # Remove rows where year data is missing
    df_cleaned = df.dropna(subset=[col for col in df.columns if col.isdigit()])  # Drop rows with missing year data
    return df_cleaned

# Get the country data based on country code
def get_country_data(df, country_code):
    '''
    Extract the data for the specified country code.
    
    Parameters:
    df (pd.DataFrame): The cleaned DataFrame.
    country_code (str): The Country Code inputted by the user.
    
    Returns:
    pd.Series: The time series data for the selected country.
    '''
    country_data = df[df['Country Code'] == country_code]
    if country_data.empty:
        print("Country Code not found in the dataset.")
        return None
    return country_data

# Plot the time series graph
def plot_electricity_access(country_data, country_name):
    '''
    Plot the time series graph of electricity access over years for the given country.
    
    Parameters:
    country_data (pd.Series): Time series data for the country.
    country_name (str): The name of the country to display in the title.
    '''
    years = [col for col in country_data.columns if col.isdigit()]  # Select year columns
    values = country_data[years].values.flatten()  # Flatten the values
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)
    plt.title(f"Electricity Access Over Time for {country_name}")
    plt.xlabel("Years")
    plt.ylabel("% of Electricity Access")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main CLI function
def main():
    # Load dataset
    df = load_data('electricity_access_percent.csv')

    # Get user input for country code
    country_code = input("Enter the Country Code: ")

    # Extract data for the selected country
    country_data = get_country_data(df, country_code)
    
    if country_data is not None:
        country_name = country_data['Country Name'].values[0]  # Get the country name
        print(f"This is the time series graph for {country_name}")
        
        # Plot the time series graph
        plot_electricity_access(country_data, country_name)

if __name__ == "__main__":
    main()
