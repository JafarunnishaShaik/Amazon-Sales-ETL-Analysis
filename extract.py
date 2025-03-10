import pandas as pd

def load_data(file_path):
    """Load data from an Excel file and display available sheets."""
    # Load the Excel file
    xls = pd.ExcelFile(file_path)

    # Display available sheets
    print("Available sheets:", xls.sheet_names)

    # Read all sheets into a dictionary of DataFrames
    return {sheet: pd.read_excel(file_path, sheet) for sheet in xls.sheet_names}

# Use the correct filename you uploaded
file_path = 'zomato-schema.xlsx'

# Call the function to load the dataset
dataframes = load_data(file_path)