import pandas as pd

def clean_data(df):
    """Clean data by handling missing values, duplicates, and incorrect data types."""

    # 1. Remove duplicate rows
    print(f"Duplicates before removal: {df.duplicated().sum()}")
    df.drop_duplicates(inplace=True)

    # 2. Handle missing values (fill with 0 for numeric columns)
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # 3. Convert date columns to datetime format
    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Drop rows with invalid dates
    df.dropna(subset=[col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])], inplace=True)

    print("✅ Data cleaned successfully!")
    return df

# Apply cleaning to all sheets
cleaned_data = {sheet: clean_data(df) for sheet, df in dataframes.items()}

# Verify cleaned sheets
for sheet, df in cleaned_data.items():
    print(f"\n✅ {sheet} - Cleaned Shape: {df.shape}")