import csv
import sys

def select_columns(input_file, output_file, columns):
    try:
        with open(input_file, 'r', newline='') as infile, \
             open(output_file, 'w', newline='') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                selected_row = [row[i] for i in columns]
                writer.writerow(selected_row)

        print("New CSV file created with selected columns.")
    except Exception as e:
        print("Error:", e)

columns = [78, 79, 17, 11, 95, 96, 97, 98]

select_columns(r"C:\Users\Renan\Documents\Mestrado\PO-233\Raw Data\Grads_SJCU.csv", r"C:\Users\Renan\Documents\Mestrado\PO-233\Filtered Data\Grads_SJCU_Filtered.csv", columns)