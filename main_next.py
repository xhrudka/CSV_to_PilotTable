import pandas as pd
import argparse

def create_pivot_table(file, index, columns, values, aggfunc):
    try:
        # Load CSV
        df = pd.read_csv(file)
        
        # Create Pivot Table
        pivot = pd.pivot_table(df, 
                               index=index, 
                               columns=columns, 
                               values=values, 
                               aggfunc=aggfunc)
        
        print("Generated Pivot Table:")
        print(pivot)

        # Save to CSV
        output_file = "pivot_table_output.csv"
        pivot.to_csv(output_file)
        print(f"Pivot table saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Pivot Table from a CSV file.")
    parser.add_argument("file", help="Path to the CSV file")
    parser.add_argument("--index", nargs='+', required=True, help="Columns to use as rows")
    parser.add_argument("--columns", nargs='*', help="Columns to use as columns", default=None)
    parser.add_argument("--values", nargs='+', required=True, help="Columns to aggregate")
    parser.add_argument("--aggfunc", default="sum", help="Aggregation function (e.g., sum, mean, count)")

    args = parser.parse_args()

    create_pivot_table(args.file, args.index, args.columns, args.values, args.aggfunc)