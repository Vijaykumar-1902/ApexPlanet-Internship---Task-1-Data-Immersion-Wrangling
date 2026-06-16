import pandas as pd

# Load Dataset
file_path = r"C:\Users\malla\Desktop\ApexPlanet\Task1\ApexPlanet_DataAnalytics_Dataset.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("TASK 1: DATA IMMERSION & WRANGLING")
print("=" * 50)

# First 5 rows
print("\nFIRST 5 ROWS")
print(df.head())

# Dataset Info
print("\nDATASET INFO")
df.info()

# Statistical Summary
print("\nSTATISTICAL SUMMARY")
print(df.describe(include='all'))

# Column Names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Duplicate Records
print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

# Data Cleaning (only if columns exist)
if 'Age' in df.columns:
    df['Age'] = df['Age'].fillna(df['Age'].mean())

if 'City' in df.columns:
    df['City'] = df['City'].fillna(df['City'].mode()[0])

# Convert Date Column
if 'Order_Date' in df.columns:
    df['Order_Date'] = pd.to_datetime(
    df['Order_Date'],
    format='%d-%m-%Y',
    errors='coerce'
)

    # Feature Engineering
    df['Year'] = df['Order_Date'].dt.year
    df['Month'] = df['Order_Date'].dt.month

# Remove Duplicates
df = df.drop_duplicates()

# Save Clean Dataset
output_file = r"C:\Users\malla\Desktop\ApexPlanet\Task1\cleaned_dataset.csv"
df.to_csv(output_file, index=False)

print("\nCLEANED DATASET SAVED SUCCESSFULLY")
