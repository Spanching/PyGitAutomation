# Simple Python Automation for Git Repository Creation

1. Install requirements:  

```shell
pip install -r requirements.txt
```

2. Create environment file:  

```shell
cp .env_sample .env
```  

3. Set your variables:  

   * GIT_AUTH_TOKEN - your personal access token for github [learn more here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
   * GIT_URL - the url to your github account (https://github.com/username)
   * GIT_PY_PATH - your path to this repository (no trailing backslash, set this inside your git.py)

4. Add command to .bash_profile if desired:

```shell
alias creategit='[path to your repository]/git.sh'
```

---

Now you can use the command `creategit` to create a repository and start working on it immediately. 