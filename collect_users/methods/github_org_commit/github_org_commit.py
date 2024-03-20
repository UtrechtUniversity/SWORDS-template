"""
This module provides a function to get commits of a GitHub organization using the GitHub API.
"""

import os
import argparse
from datetime import datetime
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read GitHub token and username from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")


def get_organization_commits(organization_name):
    """
    Get commits of a GitHub organization.

    Parameters:
    organization_name (str): The name of the GitHub organization.

    Returns:
    DataFrame: A DataFrame containing the commit IDs, date, and service.
    """
    url = f"https://api.github.com/orgs/{organization_name}/events"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "User-Agent": GITHUB_USER
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as request_err:
        print(f"HTTP Error: {request_err}")
        return pd.DataFrame()

    commits_data = response.json()
    if not commits_data:
        print("No commits found for the organization.")
        return pd.DataFrame()

    commit_ids = [commit['id'] for commit in commits_data]
    date = datetime.now().strftime("%Y-%m-%d")
    service = 'github'

    data_frame = pd.DataFrame({
        'commit_id': commit_ids,
        'date': [date] * len(commit_ids),
        'service': [service] * len(commit_ids)
    })

    return data_frame


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch and save to CSV.')
    parser.add_argument('--org', required=True, help='GitHub organization name')

    args = parser.parse_args()
    org_name = args.org

    commits_df = get_organization_commits(org_name)

    if not commits_df.empty:
        try:
            commits_df.to_csv(f'results/{org_name}_commits.csv', index=False, encoding='utf-8')
            print(f"Saved commits of organization {org_name} to results/{org_name}_commits.csv")
        except IOError as io_err:
            print(f"Failed to save CSV: {io_err}")
    else:
        print(f"Failed to fetch commits of organization {org_name}\n")
