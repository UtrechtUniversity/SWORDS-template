import os
import pandas as pd
from collections import defaultdict


def merge_csv_files(root_directory):
    # Dictionary to store file names and their paths
    csv_files = defaultdict(list)

    print(f"Starting to scan from root directory: {root_directory}")

    # Step 1: Traverse each folder to find CSV files
    for dirpath, dirnames, filenames in os.walk(root_directory):
        print(f"Scanning directory: {dirpath}")

        for filename in filenames:
            if filename.endswith('.csv'):
                full_path = os.path.join(dirpath, filename)
                print(f"Found CSV file: {full_path}")
                csv_files[filename].append(full_path)

    # Step 2 and 3: Group the CSV files with the same name and merge them
    for filename, filepaths in csv_files.items():
        if len(filepaths) > 1:  # Check if there are multiple files with the same name
            print(f"Merging files for: {filename}")
            dfs = [pd.read_csv(filepath) for filepath in filepaths]
            merged_df = pd.concat(dfs, ignore_index=True)

            # Step 4: Save the merged CSV files in the root directory
            merged_file_path = os.path.join(root_directory, f"merged_{filename}")
            merged_df.to_csv(merged_file_path, index=False)
            print(f"Merged {filename} and saved as merged_{filename} in the root directory.")
        else:
            print(f"Only one file found for {filename}. No merging required.")

# Example usage
# merge_csv_files("/path/to/root/directory")
