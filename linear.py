import numpy as np
import matplotlib.pyplot as plt

def linear_regression(X, y):
    # Calculate the number of samples
    n = len(X)
    
    # Calculate the mean of X and y
    mean_x = np.mean(X)
    mean_y = np.mean(y)
    
    # Calculate the slope (m) and the y-intercept (b) using the formulas
    numerator = np.dot(X - mean_x, y - mean_y)
    denominator = np.dot(X - mean_x, X - mean_x)
    m = numerator / denominator
    b = mean_y - m * mean_x
    
    return m, b

def predict(X, m, b):
    # Make predictions using the linear equation
    y_pred = m * X + b
    return y_pred

# Sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Perform linear regression
m, b = linear_regression(X, y)

# Make predictions
y_pred = predict(X, m, b)

# Plot the results
plt.scatter(X, y, color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()
