""" Python File to access Github """

import sys
import os

from github import Github
from github import Auth

from dotenv import load_dotenv

load_dotenv()

# Load GitHub Token from environment
GIT_AUTH_TOKEN = os.getenv("GIT_AUTH_TOKEN")
REPOSITORY_NAME = sys.argv[1]

# using an access token
auth = Auth.Token(GIT_AUTH_TOKEN)

# Public Web Github
g = Github(auth=auth)

# create new repository with supplied name and set visibility to private
repo = g.get_user().create_repo(REPOSITORY_NAME)
repo.edit(visibility='private')

# Add standard Readme.md
repo.create_file("./Readme.md", "initial commit", f"# {REPOSITORY_NAME} [Git Automation created this repo and file]")

# To close connections after use
g.close()