# Save all cleaned sheets to CSV files
for sheet, df in cleaned_data.items():
    file_name = f"cleaned_{sheet}.csv"
    df.to_csv(file_name, index=False)
    print(f"✅ Saved: {file_name}")
