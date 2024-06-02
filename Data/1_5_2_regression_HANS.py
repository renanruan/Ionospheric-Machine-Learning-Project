import pandas as pd
import matplotlib.pyplot as plt

def process_csv(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Save the processed DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print("REGRESSION HANS ALREADY DONE")

    # if 'HANS' in df.columns:
    #     plt.figure()
    #     df['HANS'].plot(kind='line')
    #     plt.title('Plot')
    #     plt.xlabel('Index')
    #     plt.ylabel('Value')
    #     plt.grid(True)
    #     plt.show()

print("1.5.2 ----------------------")
# Specify the path to your input and output CSV files
input_csv_file = r'Data\Filtered\1_4_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\Regression\1_5_Grads_SJCU.csv'

# Call the function to process the CSV file
process_csv(input_csv_file, output_csv_file)