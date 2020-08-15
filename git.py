""" Python File to access Github """

import sys
import os

from github import Github
from dotenv import load_dotenv

load_dotenv()

# Load GitHub Token from environment
GIT_AUTH_TOKEN = os.getenv("GIT_AUTH_TOKEN")

g = Github(GIT_AUTH_TOKEN)

# Get repository name from argument list
REPOSITORY_NAME = sys.argv[1]

USER = g.get_user()

# create a private repository
REPOSITORY = USER.create_repo(REPOSITORY_NAME, private=True)

# Add standard Readme.md
REPOSITORY.create_file("./Readme.md", "initial commit", REPOSITORY_NAME +
                       "\n [Git Automation created this repo and file]")
