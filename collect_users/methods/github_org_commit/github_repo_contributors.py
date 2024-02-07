import argparse
from datetime import datetime
from pathlib import Path
import os
import pandas as pd
from ghapi.all import GhApi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def fetch_contributors(repository, owner, api):
    contributors = api.repos.list_contributors(owner, repository)
    return contributors


def save_to_csv(data, filepath):
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)


if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser(description='Fetch GitHub repository contributors.')
    parser.add_argument('--repo', required=True, help='GitHub repository name')
    parser.add_argument('--owner', required=True, help='GitHub repository owner')

    args = parser.parse_args()
    repo = args.repo
    owner = args.owner

    # Initialize GitHub API
    api = GhApi(token=os.getenv('GITHUB_TOKEN'))

    # Create 'results' directory if it doesn't exist
    results_dir = Path("results")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Create directory for organization within 'results' if it doesn't exist
    org_dir = results_dir / owner
    org_dir.mkdir(parents=True, exist_ok=True)

    # Fetch contributors
    contributors = fetch_contributors(repo, owner, api)

    # Prepare data
    data = []
    current_date = datetime.today().strftime('%Y-%m-%d')
    for contributor in contributors:
        data.append({
            'user_id': contributor.login,
            'date': current_date,
            'service': 'GitHub.com'
        })

    # Save to CSV
    csv_path = org_dir / f"{repo}_contributors.csv"
    save_to_csv(data, csv_path)
    print(f"Contributor data saved to {csv_path}")
