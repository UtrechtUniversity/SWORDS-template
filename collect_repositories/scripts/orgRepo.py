# This file retrieves repositories of organisation.
import argparse
import requests
import csv

def get_repos(args):
    """ Fetch JSON data from https://api.github.com/orgs/{args.orgName}/repos
    Arguments:
        url {args.orgName} -- The API url

    Returns:
        dict of orgName metadata -- JSON data then converted to csvfiles.
       """
    print(f'Organization name, {args.orgName}')  # Press ⌘F8 to toggle the breakpoint.

    url = f"https://api.github.com/orgs/{args.orgName}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()

        # write data to csv file.
        with open(f'{args.orgName}.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'full_name', 'size','contributors_url', 'has_projects', 'collaborators_url', 'keys_url', 'permissions', 'default_branch', 'issues_url', 'git_commits_url', 'releases_url', 'git_url', 'git_tags_url', 'has_wiki', 'is_template', 'node_id', 'updated_at', 'open_issues', 'comments_url', 'events_url', 'trees_url', 'ssh_url', 'milestones_url', 'web_commit_signoff_required', 'watchers', 'forks_url', 'branches_url', 'has_issues', 'mirror_url', 'notifications_url', 'stargazers_count', 'created_at', 'pushed_at', 'hooks_url', 'has_downloads', 'issue_events_url', 'teams_url', 'html_url', 'language', 'commits_url', 'visibility', 'disabled', 'topics', 'blobs_url', 'fork', 'svn_url', 'homepage', 'owner', 'git_refs_url', 'description', 'issue_comment_url', 'open_issues_count', 'labels_url', 'tags_url', 'contents_url', 'archived', 'watchers_count', 'private', 'compare_url', 'deployments_url', 'has_discussions', 'subscription_url', 'forks', 'id', 'clone_url', 'statuses_url', 'subscribers_url', 'license', 'languages_url', 'stargazers_url', 'url', 'merges_url', 'forks_count', 'allow_forking', 'pulls_url', 'assignees_url', 'archive_url', 'downloads_url', 'has_pages']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in json_data:
                writer.writerow(row)
        return json_data
    else:
        print(f"Failed to get members for organization {args.orgName}.")
        return []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    USAGE = 'For generating pdf you can '
    parser = argparse.ArgumentParser(description=USAGE)
    parser.add_argument('orgName', type=str, help='Provide organization name of github.')
    args = parser.parse_args()
    get_repos(args)

