""" Python File to access Github """
import os 

from github import Github
from github import Auth

from dotenv import load_dotenv

load_dotenv()

GIT_AUTH_TOKEN = os.getenv("GIT_AUTH_TOKEN")
# using an access token
auth = Auth.Token(GIT_AUTH_TOKEN)

# Public Web Github
g = Github(auth=auth)

# create new repository with supplied name and set visibility to private
repo = g.get_user().get_repo("test")
repo.delete()

# To close connections after use
g.close()