import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\malla\Desktop\ApexPlanet\Task1\customer dataset csv.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Display first rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nDATASET INFO")
df.info()

# Statistical summary
print("\nSUMMARY")
print(df.describe())

# Column names
print("\nCOLUMNS")
print(df.columns.tolist())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Duplicate rows
print("\nDUPLICATES")
print(df.duplicated().sum())

# Fill missing values (only if columns exist)
if 'minimum_payments' in df.columns:
    df['minimum_payments'] = df['minimum_payments'].fillna(
        df['minimum_payments'].mean()
    )

if 'credit_limit' in df.columns:
    df['credit_limit'] = df['credit_limit'].fillna(
        df['credit_limit'].mean()
    )

# Remove duplicates
df = df.drop_duplicates()

# Create new columns
if 'balance' in df.columns and 'credit_limit' in df.columns:
    df['credit_utilization'] = df['balance'] / df['credit_limit']

if 'payments' in df.columns and 'minimum_payments' in df.columns:
    df['payment_ratio'] = df['payments'] / df['minimum_payments']

# Save cleaned dataset
df.to_csv(
    r"C:\Users\malla\Desktop\ApexPlanet\Task1\cleaned_customer_dataset.csv",
    index=False
)

print("\nCLEANED DATASET SAVED SUCCESSFULLY")

# Boxplot for outlier detection
if 'balance' in df.columns:
    plt.boxplot(df['balance'].dropna())
    plt.title("Balance Outliers")
    plt.show()