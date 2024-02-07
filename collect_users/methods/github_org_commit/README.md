# GitHub User Search

With the github_org_commit. We aim to collect organisation members and the contributors to resarch repositoires.
This can be done in 3 steps. 
1. Collect github organisation accounts.
2. Collect the members of organisations.
3. Collect the contributors to research repositories of organisation. 

## Installation

To use this submodule, install the requirements with 

```console
pip install -r requirements.txt
```

## Usage
1. **Step 1** : Collect Organisation names

    To collect GitHub organization names with research repositories. Execute the [GitHub Search](methods/github_search) method.Filter the results to include CSV files with organization names. Or find out the resarch organisation names manually. Save it somewhere accessible. You will need them to for executing the next scripts. 

2. **Step: 2** : Collect research organisation members

    This Python script fetches the list of members from a specified GitHub organization and saves their usernames into a CSV file in the results directory with <organisation_name>.csv . And save The CSV file contains three columns:
    First, navigate to this folder. Then, execute the script with arguments. For example:
    
    ```console
    python github_org_commit.py --org orgnisation_name
    ```

2. **Step: 3** :
    This command will create a directory folder with name ``<orgnisation_name>`` and also create a csv file with ``<repo_name>`` in results folder. 
    Repeat this for all research repositories of organisation.
    ```console
    python github_repo_contributors.py --repo <repo_nam> --owner <org_name>
    ```

Combine the collected csv file into single csv file called github_org_commit.csv 

```console
python combine_csv.py results/
```


## License

See [LICENSE](../../LICENSE).

## Contact

See [here](../../README.md#contact).