import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
df = pd.read_csv("data.csv")

# Display first 5 rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values with the column mean
df = df.fillna(df.mean(numeric_only=True))

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nData cleaned successfully!")
# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())
# Create Salary Bar Chart
df["Salary"].plot(kind="bar")

plt.title("Salary Report")
plt.xlabel("Employee")
plt.ylabel("Salary")

plt.savefig("salary_chart.png")
plt.show()