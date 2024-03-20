"""
This module provides a function to get contributors of a GitHub repository using the GitHub API.
"""

import os
import argparse
from datetime import datetime
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read GitHub token and username from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")


def make_request(url):
    """
    Make a request to the given URL with the global headers and timeout.

    Parameters:
    url (str): The URL to make the request to.

    Returns:
    Response: The response from the request.
    """
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "User-Agent": GITHUB_USER
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as request_err:
        print(f"HTTP Error: {request_err}")
        return None

    return response


def get_repository_contributors(repository_name):
    """
    Get contributors of a GitHub repository.

    Parameters:
    repository_name (str): The name of the GitHub repository.

    Returns:
    DataFrame: A DataFrame containing the contributor IDs, date, and service.
    """
    url = f"https://api.github.com/repos/{repository_name}/contributors"
    response = make_request(url)

    if response is None:
        return pd.DataFrame()

    contributors_data = response.json()
    if not contributors_data:
        print("No contributors found for the repository.")
        return pd.DataFrame()

    contributor_ids = [contributor['id'] for contributor in contributors_data]
    date = datetime.now().strftime("%Y-%m-%d")
    service = 'github'

    data_frame = pd.DataFrame({
        'contributor_id': contributor_ids,
        'date': [date] * len(contributor_ids),
        'service': [service] * len(contributor_ids)
    })

    return data_frame


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Fetch GitHub repository contributors and save to CSV.'
    )
    parser.add_argument('--repo', required=True, help='GitHub repository name')

    args = parser.parse_args()
    repo_name = args.repo

    contributors_df = get_repository_contributors(repo_name)

    if not contributors_df.empty:
        try:
            contributors_df.to_csv(
                f'results/{repo_name}_contributors.csv', 
            index=False,
                encoding='utf-8'
            )
            print(
                f"Saved contributors of repository {repo_name} "
                f"to results/{repo_name}_contributors.csv"
            )
        except IOError as io_err:
            print(f"Failed to save CSV: {io_err}")
    else:
        print(f"Failed to fetch contributors of repository {repo_name}")
