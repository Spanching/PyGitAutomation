# Simple Python Automation for Git Repository Creation

1. Install requirements:  

```shell
pip install -r requirements.txt
```

2. Set environment variables:  

```shell
cp .env_sample .env
```  

3. Set your variables:  

   * GIT_AUTH_TOKEN - your personal authentication for github api [learn more here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
   * GIT_PY_PATH - your path to this repository (no trailing backslash)
   * GIT_URL - the url to your github account (https://github.com/username)

4. Add command to .bash_profile:  

```shell
alias creategit='. C:/Users/AndreasK/Projects/gitAutomation/git.sh'
```

---

Now you can use the command `creategit` to create a repository and start working on it immediately. 