# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:29:42 2024

@author: rbaia
"""

import itertools
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset and assign it a name (e.g., 'data')
# This script is made in Spyder, so in the Files pane the local folder where I stored the Excel file with survey results is open
# If you use another IDE, please adapt the script to read the data
data = pd.read_excel("C:/Users/rbaia/OneDrive - HAN/Onderwijs/3DMiB Mathematics & Statistics/24-25 sem1/Class material/minor_survey.xlsx")

# Drop missing values
data = data.dropna()

# Plot histogram of FMSR student length
plt.hist(data["length"], bins=6, color='green', edgecolor='black')
plt.title('Histogram of FMSR student height')
plt.xlabel('Student height')
plt.ylabel('Frequenty')
plt.show()

# Determine sample size and the number of samples to generate
sample_size = 3
num_samples = 5

# Generate all unique combinations of 3 observations
all_samples_with_replacement  = list(itertools.product(data["length"], repeat=sample_size))
print('Number of samples possible:', len(all_samples_with_replacement))
print('Check if number of samples is correct:', len(data)**sample_size)

# Randomly select 'num_samples' samples from 'all_samples_with_replacement'
samples_with_replacement = random.sample(all_samples_with_replacement, num_samples)
print('Number of samples selected:', len(samples_with_replacement))

# Compute the mean of every sample in the set 'samples_with_replacement'
sample_means = [np.mean(sample) for sample in samples_with_replacement]

# Compute the mean of every sample in the set 'all_samples_with_replacement'
all_sample_means = [np.mean(sample) for sample in all_samples_with_replacement]

# Plot histogram of the sampling distribution of the mean
plt.hist(sample_means, bins=6, edgecolor='black')
plt.title(f'Sampling Distribution of the mean ({num_samples} samples of size {sample_size})')
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.show()

# Compute the mean of the randomly selected samples
mean_of_sample_means = np.mean(sample_means)
print('Mean of sample means:', round(mean_of_sample_means, 2))

# Compute the mean length of FMSR students
data_mean = np.mean(data["length"])
print('Mean of data:', round(data_mean, 2))




# Compute the mean of all possible samples, see that it is equal to the mean length of FMSR students
mean_of_all_sample_means = np.mean(all_sample_means)
print('Mean of sample means:', round(mean_of_all_sample_means, 2))