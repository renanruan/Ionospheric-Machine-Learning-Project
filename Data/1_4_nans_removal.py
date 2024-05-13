import pandas as pd

def remove_rows_with_nan(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file, header=None)

    # Check if the last four columns of each row contain NaN values
    nan_mask = df.iloc[:, -4:].isna().all(axis=1)

    # Remove rows where the last four columns have NaN values
    df_filtered = df[~nan_mask]

    # Replace NaN values in other columns with the mean of the respective column
    df_filtered = df_filtered.fillna(df_filtered.mean())

    print("NANS REMOVED OR REPLACED BY COLUMN MEAN")

    return df_filtered

print("1.4 ----------------------")
# Specify the path to your CSV file
csv_file_path = r'Data\Filtered\1_3_Grads_SJCU.csv'

# Call the function to remove rows with NaN values in the last four columns
filtered_df = remove_rows_with_nan(csv_file_path)

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(r'Data\Filtered\1_4_Grads_SJCU.csv', index=False)