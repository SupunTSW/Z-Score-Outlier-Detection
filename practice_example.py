import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Dataset
Deposits = [2782, 2745, 3553, 3669, 3816, 3912, 3226, 3322, 10000, 2904, 2718, 2525]

#Plot Dataset as Scatterplot
x_values = range(len(Deposits))
plt.scatter(x_values, Deposits)
plt.title('Monthly Average Deposits of a Person')
plt.xlabel('Index')
plt.ylabel('Monthly Deposit Amount ')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.show()

#Step 1: Calculate the mean
mean = np.mean(Deposits)

#Step 2 : Calculate the Standard Deviation
std_dv = np.std(Deposits)

#Step 3: Calculate the Z-Score
z_scores = (Deposits - mean) / std_dv

#Plot z-Score distribution
plt.hist(z_scores, color = 'skyblue')
plt.title('Z-Score Distribution of Monthly Deposits')
plt.xlabel('Z-score')
plt.ylabel('Frequency')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.show()

#Step 4: Define the Z_Score threshold and Identify outliers (Z-score > 2 or < -2)
z_score_threshold = 2
Outliers = np.abs(z_scores) > z_score_threshold
print(Outliers)

#Scatter plot with outliers
x_values = range(len(Deposits))
plt.scatter(x_values, Deposits, color = np.where(Outliers, 'red', 'blue'))
plt.scatter([], [], color='red', label='Anomalies') 
plt.scatter([], [], color='blue', label='Normal')  
plt.legend(loc='best') 
plt.title('Outlier detection using Z-score')
plt.xlabel('Index')
plt.ylabel('Monthly Deposit Amount ')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.show()
