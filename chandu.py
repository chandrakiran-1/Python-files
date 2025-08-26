import pandas as pd  

# Create a simple dataset (dictionary)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Paris", "London", "Tokyo"]
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(data)

# Show the DataFrame
print("DataFrame:\n", df)

# Show first 2 rows
print("\nFirst 2 rows:\n", df.head(2))

# Show basic information
print("\nInfo:")
print(df.info())

# Show basic statistics
print("\nStatistics:\n", df.describe())
