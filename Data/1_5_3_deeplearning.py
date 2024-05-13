import pandas as pd

def process_csv(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Find the maximum value among the last four columns
    df['HANS'] = df.iloc[:, -4:].max(axis=1)

    # Replace the last four columns with the new column
    df.drop(df.columns[-5:-1], axis=1, inplace=True)
    
    # Save the processed DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print("DEEP LEARNING HANS REPLACED")

print("1.5.3 ----------------------")
# Specify the path to your input and output CSV files
input_csv_file = r'Data\Filtered\1_4_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\Deep_Learning\1_5_Grads_SJCU.csv'

# Call the function to process the CSV file
process_csv(input_csv_file, output_csv_file)