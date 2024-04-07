import os
import scipy.io
import numpy as np
import csv

def show_files_keys():
    current_dir = os.path.dirname(__file__)

    files_in_dir = os.listdir(current_dir)

    mat_files = [f for f in files_in_dir if f.endswith('.mat')]

    for mat_file in mat_files:
        file_path = os.path.join(current_dir, mat_file)
        data = scipy.io.loadmat(file_path)
        print("Loaded data from:", mat_file)
        print_keys(data, data.keys(), mat_file.replace(".mat", ""))

def print_keys(data, keys, file_name):
    result = ""
    folder_name = os.path.join(os.path.dirname(__file__),file_name)
    os.makedirs(folder_name, exist_ok=True)
    for key in keys:
        if(key != '__header__' and key != '__version__' and key != '__globals__'):
            result+= key + '   '
            structure_files(data[key], key, folder_name)
    #(result)

#Grad_tempo  = dados["Grad_tempo"];
#Grad_data  = dados["Grad_data"];

def structure_files(data, key, path):

    # if isinstance(data, np.ndarray):
    #     test1 = data[0]
    #     if len(test1) == 1:
    #         test1 = test1[0]
    #     if isinstance(test1, np.ndarray):
    #         test2 = test1[0] 
    #         if len(test2) == 1:
    #             test2 = test2[0]
    #             if isinstance(test2, np.ndarray):
    #                 folder_name = os.path.join(path,key)
    #             os.makedirs(folder_name, exist_ok=True)
    #             for idx, elem in enumerate(data):
    #                 structure_files(elem, 'atr '+ str(idx), folder_name)
    #         else:
    #             file_name = os.path.join(path,key + ".csv")
    #             with open(file_name, 'w', newline='') as csvfile:
    #                 writer = csv.writer(csvfile)
    #                 writer.writerows(data)


    if isinstance(data, np.ndarray) and isinstance(data[0], np.ndarray) and isinstance(data[0][0], np.ndarray):
        folder_name = os.path.join(path,key)
        os.makedirs(folder_name, exist_ok=True)
        for idx, elem in enumerate(data):
            structure_files(elem, 'atr '+ str(idx), folder_name)
    elif isinstance(data, np.ndarray) and isinstance(data[0], np.ndarray):
        file_name = os.path.join(path,key + ".csv")
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    else:
        file_name = os.path.join(path,key + ".csv")
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)


show_files_keys()