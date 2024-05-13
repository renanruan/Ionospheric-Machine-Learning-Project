import pandas as pd

def process_csv(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Check if at least one of the last four columns has a value equal or greater than 400
    df['HANS'] = (df.iloc[:, -4:] >= 400).any(axis=1).astype(int)

    # Replace the last four columns with the new column
    df.drop(df.columns[-5:-1], axis=1, inplace=True)
    
    # Save the processed DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print("CLASSIFICATION HANS REPLACED")

print("1.5.1 ----------------------")
# Specify the path to your input and output CSV files
input_csv_file = r'Data\Filtered\1_4_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\Classification\1_5_Grads_SJCU.csv'

# Call the function to process the CSV file
process_csv(input_csv_file, output_csv_file)