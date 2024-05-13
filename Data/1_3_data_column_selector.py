import csv
import sys

# select the relevant columns from de .csv and saves them in the filtered folder
def select_columns(input_file, output_file, columns):
    try:
        with open(input_file, 'r', newline='') as infile, \
             open(output_file, 'w', newline='') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                selected_row = [row[i] for i in columns]
                writer.writerow(selected_row)

        print("NEW .CSV FILE CREATED WITH SELECTED COLUMNS.")
    except Exception as e:
        print("Error:", e)

columns = [77, 78, 16, 10, 94, 95, 96, 97]

print("1.3 ----------------------")
select_columns(r"Data\Filtered\1_2_Grads_SJCU.csv", r"Data\Filtered\1_3_Grads_SJCU.csv", columns)