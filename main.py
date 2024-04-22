import os
import pandas as pd
import matplotlib.pyplot as plt


folder_path_visualisation = 'C:/Users/japit/projects/staiml/datasets'
folder_path_correlation = 'C:/Users/japit/projects/staiml/datasets/correlation'


# Get a list of all CSV files in the folder
csv_files_visualisation = [file for file in os.listdir(folder_path_visualisation) if file.endswith('.csv')]
csv_files_correlation = [file for file in os.listdir(folder_path_correlation) if file.endswith('.csv')]


# Loop through each CSV file
for csv_file in csv_files_visualisation:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(os.path.join(folder_path_visualisation, csv_file))

    # Convert the first column to DateTime if needed
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

    # Plot the time series data
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df.index, df['Value'], color='blue', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Time Series Plot - {}'.format(csv_file))
    plt.grid(True)
    plt.show()


# Loop through each CSV file
for csv_file in csv_files_correlation:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(os.path.join(folder_path_correlation, csv_file))

    # Plot Date vs Value1 and Date vs Value2 on the same graph
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df['Date'], df['Value1'], label='Value1', color='blue', linestyle='-')
    plt.plot(df['Date'], df['Value2'], label='Value2', color='red', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Time Series Plot')
    plt.legend()  # Show legend with line labels
    plt.grid(True)
    plt.show()

    # Convert "<1" strings to NaN and then convert the column to numeric
    df['Value1'] = pd.to_numeric(df['Value1'], errors='coerce')
    df['Value2'] = pd.to_numeric(df['Value2'], errors='coerce')

    # Calculate the correlation coefficient
    correlation_coefficient = df['Value1'].corr(df['Value2'])
    print("Correlation coefficient between Value1 and Value2:", correlation_coefficient)


# Example exploratory data analysis
# Read the CSV file into a DataFrame
df = pd.read_csv('datasets/exploratory_data_analysis/geoMap.csv')
# Sort the DataFrame by Sore Throat Score in descending order
sorted_df = df.sort_values(by='Sore Throat Score', ascending=False)
# Filter out rows with missing scores
sorted_df = sorted_df.dropna(subset=['Sore Throat Score'])
# Get the top 10 countries
top_10_countries = sorted_df.head(10)
# Print the top 10 countries
print("Top 10 countries for sore throat:")
print(top_10_countries[['Country', 'Sore Throat Score']])