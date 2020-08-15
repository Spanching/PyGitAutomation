#!/bin/bash

# make and go to directory with passed name
mkdir $1
cd $1

# load variables from .env
export $(egrep '^#' .env)

# init git repository
git init

# create repository
python $GIT_PY_PATH/git.py $1

# link local and online repositories
git remote add origin $GIT_URL/$1.git

git pull origin master

git push -u origin master