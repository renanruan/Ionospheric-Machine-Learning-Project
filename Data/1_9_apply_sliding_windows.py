import csv
import pandas as pd

def concatenate_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)

    columns = ['Feature 1', 'Feature 2', 'Feature 3', 'Target']
    concatenated_lines = []
    first_line = []
    for k in range(len(lines[0]) - 1):
        first_line.append(columns[k] + ' Linha -2')
        first_line.append(columns[k] + ' Linha -1')
        first_line.append(columns[k] + ' Linha -0')
    first_line.append(lines[0][-1])
    concatenated_lines.append(first_line)
    for i in range(3, len(lines)):
        concatenated_line = []
        for j in range(len(lines[i]) - 1):
            concatenated_line.append(lines[i-2][j])
            concatenated_line.append(lines[i-1][j])
            concatenated_line.append(lines[i][j])
        concatenated_line.append(lines[i][-1])  # Add the last column of the current line
        concatenated_lines.append(concatenated_line)

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(concatenated_lines)
    print("LINES CONCATENATED")

print("1.9 ----------------------")
# Specify the path to your input and output CSV files
folders = ["Classification", "Regression"]

input_csv_file = r'Data\Filtered\REPLACE\1_8_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\REPLACE\Final_Grads_SJCU.csv'

[concatenate_lines(input_csv_file.replace("REPLACE",value), output_csv_file.replace("REPLACE",value)) for value in folders]

input_csv_file = r'Data\Filtered\Deep_Learning\1_8_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\Deep_Learning\Final_Grads_SJCU.csv'

df = pd.read_csv(input_csv_file)
df.to_csv(output_csv_file, index=False)