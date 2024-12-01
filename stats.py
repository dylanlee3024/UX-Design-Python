import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Simulated usability data for the app evaluation
data = {
    "Participant": [1, 2, 3, 4, 5],
    "Task_Completion_Time": [45, 50, 40, 65, 55],  # Time in seconds
    "Errors": [1, 2, 0, 3, 1],  # Number of errors per participant
    "Satisfaction_Rating": [8, 7, 9, 6, 8],  # Rating out of 10
    "App_Familiarity_Score": [3, 2, 4, 1, 3],  # Familiarity with fitness apps (1-5 scale)
}

# Convert to DataFrame for analysis
df = pd.DataFrame(data)

# Calculate statistical findings
mean_time = df["Task_Completion_Time"].mean()
mean_errors = df["Errors"].mean()
mean_satisfaction = df["Satisfaction_Rating"].mean()

# Create bar chart for Task Completion Time
plt.figure(figsize=(8, 5))
plt.bar(df["Participant"], df["Task_Completion_Time"], color='blue', alpha=0.7)
plt.axhline(mean_time, color='red', linestyle='--', label=f'Mean Time: {mean_time:.2f}s')
plt.title("Task Completion Time by Participant")
plt.xlabel("Participant")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()

# Create scatter plot for Errors vs Satisfaction
plt.figure(figsize=(8, 5))
plt.scatter(df["Errors"], df["Satisfaction_Rating"], color='green', alpha=0.7)
plt.title("Errors vs. Satisfaction Rating")
plt.xlabel("Number of Errors")
plt.ylabel("Satisfaction Rating (out of 10)")
plt.show()

# Create correlation matrix heatmap
correlation_matrix = df[["Task_Completion_Time", "Errors", "Satisfaction_Rating", "App_Familiarity_Score"]].corr()

# Heatmap of correlations
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none', aspect='auto')
plt.colorbar(label="Correlation Coefficient")
plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=45, ha='right')
plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.title("Correlation Matrix of Usability Metrics")
plt.show()

# Display correlation matrix for user
correlation_matrix
