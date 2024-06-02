import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'Data\Filtered\Classification\Final_Grads_SJCU.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Specify the value of X
X = 0  # Replace with your desired value

# Specify the number of last columns to consider
K = 1  # Replace with the number of last columns to consider

# Compute absolute values for the last K columns
abs_last_K_columns = df.iloc[:,-K:].abs()

# Check if any of the absolute values of the last K columns exceed X
condition = (abs_last_K_columns > X).any(axis=1)
count_rows = condition.sum()

print(f"Number of rows with any absolute value of the last {K} columns greater than {X}: {count_rows}")