import csv
import pandas as pd

# select the relevant columns from de .csv and saves them in the filtered folder
def select_columns(input_file, output_file, columns):
    try:
        with open(input_file, 'r', newline='') as infile, \
             open(output_file, 'w', newline='') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                # Check if the conditions for column 7 and column 70 are met
                if float(row[7]) > 12 and 18 <= float(row[69]) <= 27 and float(row[9]) > 0.3:
                    selected_row = [row[i] for i in columns]
                    writer.writerow(selected_row)

        print("NEW .CSV FILE CREATED WITH SELECTED ROWS AND COLUMNS.")

    except Exception as e:
        print("Error:", e)

columns = [76, 77, 15, 93, 94, 95, 96]

print("1.3 ----------------------")
select_columns(r"Data\Filtered\1_2_Grads_SJCU.csv", r"Data\Filtered\1_3_Grads_SJCU.csv", columns)