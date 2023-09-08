# GitHub User Search

ghapi package - github_search retrieves all users for the following: 
* Users who has commited to atleast one of the repository in the organisation specified. 

## Installation

To use this submodule, install the requirements with 

```console
pip install -r requirements.txt
```

## Usage


This Python script fetches the list of members from a specified GitHub organization and saves their usernames into a CSV file. The CSV file contains three columns:
First, navigate to this folder. Then, execute the script with arguments. For example:

```console
python github_org_commit.py --org orgnisation_name
```
You can find the organisation names after executing [GitHub Search](methods/github_search) and filtering csv files with organiszation
The collected GitHub user identifiers are stored in the results folder. 

## License

See [LICENSE](../../LICENSE).

## Contact

See [here](../../README.md#contact).