import requests
import pandas as pd
import argparse
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read GitHub token and username from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")


def get_organization_members(org_name):
    url = f"https://api.github.com/orgs/{org_name}/members"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "User-Agent": GITHUB_USER
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"HTTP Error: {e}")
        return pd.DataFrame()

    members_data = response.json()
    if not members_data:
        print("No members found for the organization.")
        return pd.DataFrame()

    user_ids = [member['login'] for member in members_data]
    date = datetime.now().strftime("%Y-%m-%d")
    service = 'github'

    df = pd.DataFrame({
        'user_id': user_ids,
        'date': [date] * len(user_ids),
        'service': [service] * len(user_ids)
    })

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch GitHub organization members and save to CSV.')
    parser.add_argument('--org', required=True, help='GitHub organization name')

    args = parser.parse_args()
    org_name = args.org

    members_df = get_organization_members(org_name)

    if not members_df.empty:
        try:
            members_df.to_csv(f'results/{org_name}_members.csv', index=False, encoding='utf-8')
            print(f"Saved members of organization {org_name} to results/{org_name}_members.csv")
        except Exception as e:
            print(f"Failed to save CSV: {e}")
    else:
        print(f"Failed to fetch members of organization {org_name}")
