import subprocess

#************************************************************
# ALGORITMO PARA RODAR TODOS OS FILTROS NA SEQUENCIA
#************************************************************

print("1 ------------------------")
print("STARTED FILTER ROUTINE")

# List of Python files to run in sequence
python_files = [r'Data\1_1_data_relevants.py', r'Data\1_2_data_converter.py', R'Data\1_3_data_column_selector.py', r'Data\1_4_nans_removal.py', r'Data\1_5_1_classification_HANS.py', r'Data\1_5_2_regression_HANS.py', r'Data\1_5_3_deeplearning_HANS.py', r'Data\1_6_remove_outliners.py', r'Data\1_7_balance.py',r'Data\1_8_normalization.py',r'Data\1_9_apply_sliding_windows.py']

# Iterate over the list and run each Python file
for file in python_files:
    # Run the Python file using subprocess
    subprocess.run(['python', file])