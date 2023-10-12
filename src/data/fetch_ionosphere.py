import numpy as np


# fetch dataset
ionosphere_data = np.loadtxt("../data/ionosphere/ionosphere.data", delimiter=',', dtype='str')
arr = np.array(ionosphere_data)

# remove rows with missing values
arr = arr[~np.any(arr == " ?", axis=1)]

# remove duplicate rows
arr = np.unique(arr, axis=0)

# convert labels to binary
arr[arr == "b"] = 0
arr[arr == "g"] = 1

# make all values floats
arr = arr.astype(float)