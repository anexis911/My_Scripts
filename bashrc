PS1="${VENV}\[\033[01;32m\]\n[\w]\n\u@\h\[\033[00m\]: $ "


PS1="${VENV}\[\033[01;32m\]\n[\w]\n\u@\h\[\033[00m\]: $ "

# Setting PATH for Python 3.5
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH

GIT_PROMPT_ONLY_IN_REPO=1
GIT_PROMPT_START="${VENV}\[\033[01;32m\]\n[\w]\n\u@\h\[\033[00m\]: $ "
source ~/.bash-git-prompt/gitprompt.sh
