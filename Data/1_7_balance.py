import pandas as pd

def process_csv(input_file, output_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    df.to_csv(output_file, index=False)
    print("BALANCE NOT IMPLEMENTED")

print("1.7 ----------------------")
# Specify the path to your input and output CSV files
folders = ["Classification", "Regression", "Deep_Learning"]

input_csv_file = r'Data\Filtered\REPLACE\1_6_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\REPLACE\1_7_Grads_SJCU.csv'

[process_csv(input_csv_file.replace("REPLACE",value), output_csv_file.replace("REPLACE",value)) for value in folders]
