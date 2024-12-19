import pandas as pd
import chardet
# Load CSV into a DataFrame
# Simple CSV file
# df = pd.read_csv(r'C:\Users\Operator\Documents\GIT_Personal\CSV_to_PilotTable-main\CSV_new.csv')

# Complex CSV file
# Error handler during the opening and decoding of the file
try:
    df = pd.read_csv(r'C:\Users\Operator\Documents\GIT_Personal\CSV_to_PilotTable-main\csv_import.csv', encoding='utf-8')
    print(df.head())
except Exception as e:
    print(f"Error: {e}")

# Display the first 5 rows
# print(df.head())
