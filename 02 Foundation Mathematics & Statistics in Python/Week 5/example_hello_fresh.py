# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:59:41 2024

@author: rbaia
"""

# Example Hello Fresh hypothesis testing

import numpy as np
from scipy.stats import ttest_1samp, t
import matplotlib.pyplot as plt

# Specify the data
data = np.array([15.50, 15.60, 15.40, 15.70, 15.00, 14.80, 15.30, 14.85, 15.40, 15.10])

# Compute mean and std
print(np.mean(data))
print(np.std(data, ddof=1))     # ddof=1 ensures that the correction is made for the degrees of freedom under sample data (which should be n-1)

# Specify assumed mean
assumed_mean = 15.00

# Compute p-value
result = ttest_1samp(data, assumed_mean, alternative='greater')     # alternative='greater' because one-tailed test
print(result)

# Compute T-test statistic to compare with critical t-value
n = 10                                       # Define sample size
critical_t_value = t.ppf(q=0.95, df=n-1)
print(critical_t_value)








# To make the plot of the t-distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Set degrees of freedom and parameters for t-distribution
critical_value = 1.83
test_statistic = 2.68

# Generate values for the t-distribution
x = np.linspace(-5, 5, 500)
t_distribution = t.pdf(x, df=n-1)

# Plot the t-distribution
plt.plot(x, t_distribution, color='blue', label='t-distribution')

# Shade the critical region (right-tailed test in this case)
plt.fill_between(x, 0, t_distribution, where=(x >= critical_value), color='gray', alpha=0.5, label='Critical region')

# Add critical t-value as a vertical line
plt.axvline(x=critical_value, color='green', linestyle='--', label=f'Critical t-value = {critical_value}')

# Add test statistic as a vertical line
plt.axvline(x=test_statistic, color='red', linestyle='--', label=f'Test statistic = {test_statistic}')

# Add labels, title, and legend
plt.xlabel('t')
plt.ylabel('Probability Density')
plt.title('t-distribution under H0 (mean=15, df=9)')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()