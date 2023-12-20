#!/bin/bash

export GIT_PY_PATH=" C:/Users/andre/Projects/Python/PyGitAutomation"

# load variables from .env
source $GIT_PY_PATH/.env

# make and go to directory with passed name
mkdir $1
cd $1

# init git repository
git init

# create repository
python $GIT_PY_PATH/git.py $1

# link local and online repositories
git remote add origin $GIT_URL/$1.git

git pull origin main

git push -u origin main