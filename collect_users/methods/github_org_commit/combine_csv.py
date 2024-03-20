"""
This module provides a function to combine CSV files from subfolders into a single CSV file.
"""

import os
import argparse
import pandas as pd


def combine_csv_files_from_subfolders(root_dir):
    """
    Combine CSV files from subfolders into a single CSV file.

    Parameters:
    root_dir (str): The root directory containing subfolders with CSV files.

    Returns:
    None
    """
    # Check if the provided directory exists
    if not os.path.exists(root_dir):
        print(f"The provided directory '{root_dir}' does not exist.")
        return
    if not os.path.isdir(root_dir):
        print(f"The provided path '{root_dir}' is not a directory.")
        return

    # List to store DataFrames from each CSV file
    all_dataframes = []

    # Walk through each directory and sub-directory in the root directory
    for subdir, _, files in os.walk(root_dir):
        print(f"Checking directory: {subdir}")
        for file in files:
            if file.endswith(".csv"):
                filepath = os.path.join(subdir, file)
                try:
                    data_frame = pd.read_csv(filepath)
                    data_frame["source_subfolder"] = os.path.basename(subdir)
                    all_dataframes.append(data_frame)
                    print(f"Combining '{file}' from folder '{subdir}'")
                except pd.errors.EmptyDataError:
                    print(f"Warning: The file '{file}' in folder '{subdir}'"
                          " is empty or has no valid CSV data. Skipping.")
                except FileNotFoundError:
                    print(f"Error:file: '{file}' in folder '{subdir}' not exist. Skipping.")

    if not all_dataframes:
        print("No CSV files found in the specified directory and its sub-directories.")
        return

    combined_df = pd.concat(all_dataframes, ignore_index=True)
    combined_csv_path = os.path.join(root_dir, "github_org_commit.csv")
    combined_df.to_csv(combined_csv_path, index=False)
    print(f"Finished combining. The combined CSV file is saved as '{combined_csv_path}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine CSV from subfolders into a single CSV.")
    parser.add_argument("directory", help="Path to the root directory containing subfolders.")
    args = parser.parse_args()
    combine_csv_files_from_subfolders(args.directory)
