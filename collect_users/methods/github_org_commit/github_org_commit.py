import requests
import csv
import argparse
from datetime import date


def get_organization_members(organization):
    url = f"https://api.github.com/orgs/{organization}/members"
    response = requests.get(url)
    if response.status_code == 200:
        members = [member["login"] for member in response.json()]
        print("Collecting organisation members....")
        return members
    else:
        print(f"Failed to get members for organization {organization}.")
        return []


def get_organization_repositories(organization):
    url = f"https://api.github.com/orgs/{organization}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = [repo["name"] for repo in response.json()]
        print("Collecting organisation repos")
        return repositories
    else:
        print(f"Failed to get repositories for organization {organization}.")
        return []


def get_users_with_commits(organization):
    members = get_organization_members(organization)
    repositories = get_organization_repositories(organization)
    users_with_commits = set()

    for repository in repositories:
        url = f"https://api.github.com/repos/{organization}/{repository}/commits"
        response = requests.get(url)
        if response.status_code == 200:
            commits = response.json()
            for commit in commits:
                author = commit["author"]
                if author and author["login"] in members:
                    users_with_commits.add(author["login"])
        else:
            print(f"Failed to get commits for repository {repository}.")
    print("Getting user_id's of users who had comitted to repos...")
    return list(users_with_commits)


def save_to_csv(data, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["user_id", "source", "service", "date"])
        for item in data:
            writer.writerow([item, "github_org_commit", "github.com", date.today()])
    print("Saving data to csv file")


# Parse command-line arguments
parser = argparse.ArgumentParser(description="Get users who have committed to repositories in a GitHub organization.")
parser.add_argument("organization", help="Name of the GitHub organization")
args = parser.parse_args()

# Example usage
organization = args.organization
users_with_commits = get_users_with_commits(organization)
save_to_csv(users_with_commits, "results/users_with_commits.csv")
