import os
import scipy.io
import numpy as np
import csv

# converts tbe .mat file to .csv
def iterate_mat_files():
    current_dir = os.path.join(os.path.dirname(__file__),"Raw")

    files_in_dir = os.listdir(current_dir)

    mat_files = [f for f in files_in_dir if f.endswith('.mat')]

    for mat_file in mat_files:
        file_path = os.path.join(current_dir, mat_file)
        data = scipy.io.loadmat(file_path)
        print("LOADED DATA FROM:", mat_file)
        process_file(data, data.keys(), "Filtered/1_2_Grads_SJCU.csv")

def process_file(data, keys, file_name):
    new_file_name = os.path.join(os.path.dirname(__file__),file_name)
    for key in keys:
        if(key != '__header__' and key != '__version__' and key != '__globals__'):
            save_file_in_csv(data[key], key, new_file_name)

def save_file_in_csv(data, key, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("DATA CONVERTED TO .CSV")

print("1.2 ----------------------")
iterate_mat_files()