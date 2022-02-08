#!/bin/bash
echo "Fetching users..."
cd methods/github_search
pip install -r requirements.txt
python github_search.py --topic {INSERT ARGUMENT} --search {INSERT ARGUMENT}
cd ../papers_with_code
pip install -r requirements.txt
python papers_with_code.py --query {INSERT ARGUMENT}
echo "Merging users..."

cd ../../
pip install -r requirements.txt
python scripts/merge_users.py
echo "Enriching users..."
python scripts/enrich_users.py
echo "Preparing user filtering..."
python scripts/prepare_filtering.py
echo "Pipeline run succeeded."