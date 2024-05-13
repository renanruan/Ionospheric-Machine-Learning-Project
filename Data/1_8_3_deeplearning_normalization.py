import pandas as pd

def process_csv(input_file, output_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Calculate mean and standard deviation for each column
    means = df.mean()
    std_devs = df.std()

    # Normalize each column
    normalized_df = (df - means) / std_devs

    # You can save the normalized data back to a CSV file if needed
    normalized_df.to_csv(output_file, index=False)
    print("DATA NORMALIZED")

print("1.8.3 ----------------------")
# Specify the path to your input and output CSV files
folders = ["Deep_Learning"]

input_csv_file = r'Data\Filtered\REPLACE\1_7_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\REPLACE\1_8_Grads_SJCU.csv'

[process_csv(input_csv_file.replace("REPLACE",value), output_csv_file.replace("REPLACE",value)) for value in folders]
