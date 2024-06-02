import pandas as pd
import matplotlib.pyplot as plt

def process_csv(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Replace values in the last column based on the condition
    df.iloc[:, -1] = (df.iloc[:, -1] > 400).astype(int)

    # Save the processed DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print("CLASSIFICATION HANS REPLACED")


print("1.5.1 ----------------------")
# Specify the path to your input and output CSV files
input_csv_file = r'Data\Filtered\1_4_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\Classification\1_5_Grads_SJCU.csv'

# Call the function to process the CSV file
process_csv(input_csv_file, output_csv_file)