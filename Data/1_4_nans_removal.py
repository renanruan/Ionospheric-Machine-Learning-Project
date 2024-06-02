import pandas as pd
import numpy as np

def remove_rows_with_nan(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file, header=None)

    # Extract features and target attributes
    features = df.iloc[:, :-4]
    targets = df.iloc[:, -4:]

    # Prepare a list to hold the processed rows
    processed_rows = []

    # Process each row
    for i in range(len(df)):
        feature_row = features.iloc[i].tolist()
        target_row = targets.iloc[i].tolist()
        
        collapsed_targets = []
        temp_group = []
        
        for target in target_row:
            if pd.isna(target):
                continue  # Skip NaN values
            
            if abs(target) < 400:
                temp_group.append(abs(target))
            else:
                if temp_group:
                    collapsed_targets.append(max(temp_group))
                    temp_group = []
                collapsed_targets.append(abs(target))
        
        if temp_group:
            collapsed_targets.append(max(temp_group))
        
        for collapsed_target in collapsed_targets:
            processed_rows.append(feature_row + [collapsed_target])

    # Convert the processed rows back to a DataFrame
    processed_df = pd.DataFrame(processed_rows, columns=['Feature1', 'Feature2', 'Feature3', 'Target'])

    # Iterate through each row
    for i in range(1, len(processed_df)):
        # Iterate through each feature column
        for col in processed_df.columns[:-1]:  # Exclude the last column (target)
            # Check if the current value is NaN
            if pd.isna(processed_df.at[i, col]):
                processed_df.at[i, col] = processed_df.at[i-1, col]

    print("TARGET DISTRIBUTED IN ROWS AND NANS REMOVED ")

    return processed_df

print("1.4 ----------------------")
# Specify the path to your CSV file
csv_file_path = r'Data\Filtered\1_3_Grads_SJCU.csv'

# Call the function to remove rows with NaN values in the last four columns
filtered_df = remove_rows_with_nan(csv_file_path)

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(r'Data\Filtered\1_4_Grads_SJCU.csv', index=False)