import pandas as pd

def process_csv(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    df.describe()

    print(df.describe())

    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    # Calculate upper and lower bounds
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR
    
    # Check for outliers in each numerical column
    outlier_mask = ((df < lower_bound) | (df > upper_bound)).any(axis=1)
    
    # Remove rows with outliers
    df_filtered = df[~outlier_mask]

    print(df_filtered.describe())
    
    # Save the processed DataFrame to a new CSV file
    df_filtered.to_csv(output_file, index=False)
    print("OUTLINES REMOVED")

print("1.6 ----------------------")
# Specify the path to your input and output CSV files
folders = ["Classification", "Regression", "Deep_Learning"]

input_csv_file = r'Data\Filtered\REPLACE\1_5_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\REPLACE\1_6_Grads_SJCU.csv'

[process_csv(input_csv_file.replace("REPLACE",value), output_csv_file.replace("REPLACE",value)) for value in folders]
