import numpy as np
import pandas as pd


# Gradient Descent Function
def gradient_descent(X, y, beta, learning_rate, iterations):
    m = len(y)  # Number of training examples
    cost_history = np.zeros(iterations)

    for it in range(iterations):
        # Prediction for all training examples
        y_pred = X.dot(beta)

        # Calculate the gradient
        gradient = (1 / m) * X.T.dot(y_pred - y)

        # Update parameters
        beta -= learning_rate * gradient

        # Calculate and store the cost
        cost_history[it] = (1 / (2 * m)) * np.sum(np.square(y_pred - y))

    return beta, cost_history


# Load data from CSV
df = pd.read_csv("players_21.csv")

# Extract the target variable (Y) and features (X)
y = df["value_eur"].values  # Target variable
X = df[["wage_eur", "overall", "potential"]].values  # Feature matrix

# Normalize the features to improve performance (optional, but common)
# You can comment out this section if you don't want normalization
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Add intercept term (bias) to X (column of 1s)
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add a column of ones for the intercept

# Initialize beta (coefficients) with zeros
beta = np.zeros(X_b.shape[1])

# Set hyperparameters
learning_rate = 0.00000001
iterations = 30000

# Run Gradient Descent
beta_optimal, cost_history = gradient_descent(X_b, y, beta, learning_rate, iterations)

# Results
print("Optimal coefficients (beta):", beta_optimal)
print("Cost history (first 10):", cost_history[:10])
