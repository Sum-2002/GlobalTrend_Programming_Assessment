import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

def clean_and_preprocess(df):

    # Handle missing values
    df.fillna(df.mean(), inplace=True)  # Replace missing values with mean of each column

    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # Normalize numerical columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Encode categorical columns
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    return df




# Create a sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, np.nan, 50, 55, 60],
    'Country': ['USA', 'Canada', 'Mexico', 'USA', 'Canada', 'Mexico', 'USA', 'Canada', 'Mexico'],
    'Score': [90, 80, 70, 95, 85, 75, 92, 88, 78],
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Clean and preprocess the dataset
df_clean = clean_and_preprocess(df)

print("\nCleaned and Preprocessed DataFrame:")
print(df_clean)