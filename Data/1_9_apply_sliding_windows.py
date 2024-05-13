import csv

def concatenate_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)

    concatenated_lines = []
    for i in range(3, len(lines)):
        concatenated_line = []
        for j in range(len(lines[i]) - 2):
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
folders = ["Classification", "Regression", "Deep_Learning"]

input_csv_file = r'Data\Filtered\REPLACE\1_8_Grads_SJCU.csv'
output_csv_file = r'Data\Filtered\REPLACE\Final_Grads_SJCU.csv'

[concatenate_lines(input_csv_file.replace("REPLACE",value), output_csv_file.replace("REPLACE",value)) for value in folders]
