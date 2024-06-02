import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Load data from .mat file
data = loadmat('Data\Raw\Grads_SJCU.mat')['x']  # Assuming Grads_SJCU.mat contains the data

# Find indices where the conditions are met
i = np.where((data[:, 69] > 18) & (data[:, 69] <= 27) & (data[:, 7] > 12))[0]
i = np.where((data[:, 69] > 18) & (data[:, 69] <= 27) & (data[:, 7] > 12) & (data[:, 9] > 0.3))[0]

# Filter x based on the indices found
x = data[i, :]


num_rows = x.shape[0]

print(f'Number of rows in the matrix: {num_rows}')

# Extract columns 94, 95, 96, and 97
columns_to_check = x[:, [93, 94, 95, 96]]

# Compute absolute values
abs_values = np.abs(columns_to_check)

# 27mil linhas

# Count rows where any absolute value is greater than 400
count_greater_than_400 = np.sum(np.any(abs_values > 400, axis=1))

count = np.sum(np.abs(columns_to_check) > 400)

print(f"Number of rows with absolute value greater than 400: {count_greater_than_400}")
print(f"Number of cells with absolute value greater than 400: {count}")

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the .mat file
data = scipy.io.loadmat('Data\Raw\Grads_SJCU.mat')

# Assuming 'x' is a key in the loaded .mat file
x = data['x']

# Filter the data as per the given conditions
i = np.where((x[:, 69] > 18) & (x[:, 69] <= 27) & (x[:, 7] > 12))
x = x[i]

ANGULO = 15

i1 = np.where((x[:, 9] > 0.3) & (np.abs(x[:, 76]) <= ANGULO) & (np.abs(x[:, 77]) <= ANGULO))
temp1 = x[i1]

i2 = np.where((x[:, 9] > 0.3) & ((np.abs(x[:, 76]) > ANGULO) | (np.abs(x[:, 77]) > ANGULO)))
temp2 = x[i2]

i3 = np.where(x[:, 9] < 0.3)
temp3 = x[i3]

# Extract the required columns and transpose for plotting
Algn = np.abs(np.vstack((temp1[:, 93], temp1[:, 94], temp1[:, 95], temp1[:, 96]))).T
NAlgn = np.abs(np.vstack((temp2[:, 93], temp2[:, 94], temp2[:, 95], temp2[:, 96]))).T
Nepb = np.abs(np.vstack((temp3[:, 93], temp3[:, 94], temp3[:, 95], temp3[:, 96]))).T

# Plot the data
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(Algn)
plt.title('Algn')

plt.subplot(3, 1, 2)
plt.plot(NAlgn)
plt.title('NAlgn')

plt.subplot(3, 1, 3)
plt.plot(Nepb)
plt.title('Nepb')

plt.tight_layout()
plt.show()
