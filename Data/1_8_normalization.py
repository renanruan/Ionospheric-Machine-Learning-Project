import pandas as pd

def process_csv(input_file, output_file, not_normalized_columns):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Select all columns except the target ones for normalization
    columns_to_normalize = df.columns[:-not_normalized_columns]

    # Calculate mean and standard deviation for each column
    means = df[columns_to_normalize].mean()
    std_devs = df[columns_to_normalize].std()

    normalized_df = df.copy()  # Make a copy to preserve the original DataFrame
    normalized_df[columns_to_normalize] = (df[columns_to_normalize] - means) / std_devs

    # You can save the normalized data back to a CSV file if needed
    normalized_df.to_csv(output_file, index=False)
    print("DATA NORMALIZED")

print("1.8.1 ----------------------")
# Specify the path to your input and output CSV files
folders = ["Classification", "Regression", "Deep_Learning"]
not_normalized_columns = [1, 1, 1]

input_csv_file = r'Data\Filtered\REPLACE\1_7_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\REPLACE\1_8_Grads_SJCU.csv'

[process_csv(input_csv_file.replace("REPLACE",value), output_csv_file.replace("REPLACE",value), columns) for value, columns in zip(folders, not_normalized_columns)]
