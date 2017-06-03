# virtualenv
function virtualenv_info(){
    # Get Virtual Env
    if [[ -n "$VIRTUAL_ENV" ]]; then
        # Strip out the path and just leave the env name
        venv="${VIRTUAL_ENV##*/}"
    else
        # In case you don't have one activated
        venv=''
    fi
    [[ -n "$venv" ]] && echo "(venv:$venv) "
}

# disable the default virtualenv prompt change
export VIRTUAL_ENV_DISABLE_PROMPT=1

VENV="\$(virtualenv_info)";

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh


PS1="${VENV}\[\033[01;32m\]\n[\w]\n\u@\h\[\033[00m\]: $ "

# Setting PATH for Python 3.5
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH

GIT_PROMPT_ONLY_IN_REPO=1
GIT_PROMPT_START="${VENV}\[\033[01;32m\]\n[\w]\n\u@\h\[\033[00m\]: $ "
source ~/.bash-git-prompt/gitprompt.sh
