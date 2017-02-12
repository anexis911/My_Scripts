
Сначала установить pip и несколько пакетов:
```
apt-get install python-pip python-dev sshpass
```
Потом обновить pip:
```
pip install --upgrade pip
```

Поставить пакет для работы с виртуальными окружениями:
```
pip install virtualenvwrapper
```

После установки, в .bashrc нужно добавить несколько строк
```
export WORKON_HOME=~/venv

. /usr/local/bin/virtualenvwrapper.sh
```

Выполнить команду, чтобы перезапустить bash:
```
exec bash
```

Создать виртуальное окружение:
```
mkvirtualenv pyneng
```

Внутри виртуального окружения:
```
pip install -r requirements.txt
```

Содержимое requirements.txt:
```
ansible==2.2.0.0
appdirs==1.4.0
backports.shutil-get-terminal-size==1.0.0
cffi==1.9.1
cryptography==1.7.2
decorator==4.0.11
enum34==1.1.6
gtextfsm==0.2.1
idna==2.2
ipaddress==1.0.18
ipython==5.2.2
ipython-genutils==0.1.0
Jinja2==2.9.5
MarkupSafe==0.23
netmiko==1.2.7
packaging==16.8
paramiko==2.1.1
pathlib2==2.2.1
pexpect==4.2.1
pickleshare==0.7.4
prompt-toolkit==1.0.13
ptyprocess==0.5.1
pyasn1==0.2.2
pycparser==2.17
pycrypto==2.6.1
Pygments==2.2.0
pyparsing==2.1.10
PyYAML==3.12
scandir==1.4
scp==0.10.2
simplegeneric==0.8.1
six==1.10.0
traitlets==4.3.1
wcwidth==0.1.7
```


```
set nocompatible
set undofile
filetype plugin indent on


set ignorecase
set smartcase
set gdefault

set encoding=utf-8
set t_Co=256

let python_highlight_all=1
set fileformat=unix
set ruler

set sts=4
set ts=4
set sw=4
set expandtab
set autoindent
syn on
filetype indent on
colorscheme desert

```
