import pandas as pd

df = pd.read_csv('/content/netflix_titles.csv')

print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Fill missing values
df = df.fillna('Unknown')

# Save cleaned dataset
df.to_csv('cleaned_netflix.csv', index=False)

print("Cleaning completed!")
