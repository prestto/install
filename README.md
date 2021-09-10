# install

A generalist's guide to ubuntu

## apt

```bash
sudo apt update
sudo apt upgrade -y
```

## VSCode

```bash
sudo apt-get install -y curl
curl -o visual_studio_code-latest_stable.deb -L "https://update.code.visualstudio.com/latest/linux-deb-x64/stable"
sudo dpkg -i visual_studio_code-latest_stable.deb
rm visual_studio_code-latest_stable.deb

# global settings
mkdir -p ~/.config/Code/User/
cat > ~/.config/Code/User/settings.json <<EOL
{
    "editor.fontSize": 12,
    "editor.insertSpaces": true,
    "editor.dragAndDrop": false,
    "editor.tabSize": 4,
    "editor.detectIndentation": false
}
EOL
```

## Sublime

```bash
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install -y apt-transport-https

echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install -y sublime-text

mkdir -p ~/.config/sublime-text-3/Installed\ Packages/
wget -o ~/.config/sublime-text-3/Installed\ Packages/Package\ Control.sublime-package "https://packagecontrol.io/Package Control.sublime-package"
```

## Git

[Docs](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04)

```bash
sudo apt install -y git

# MAKE SURE TO UPDATE THESE
git config --global user.name "your name"
git config --global user.email "your email"
git config --global rebase.autoStash true
git config --global pull.rebase true
```

## SSH for git

```bash
ssh-keygen -N "" -f ~/.ssh/id_rsa_git
cat ~/.ssh/id_rsa_git.pub
```

## Git prompt

[Docs](https://github.com/magicmonty/bash-git-prompt)

```bash
cd ~
mkdir bin
git clone https://github.com/magicmonty/bash-git-prompt.git bin/bash-git-prompt
cat >> ~/.bashrc <<EOL

# Git prompt
GIT_PROMPT_ONLY_IN_REPO=1
GIT_PROMPT_FETCH_REMOTE_STATUS=0
GIT_PROMPT_SHOW_UNTRACKED_FILES=normal
GIT_PROMPT_START=\${PS1}
source \$HOME/bin/bash-git-prompt/gitprompt.sh

EOL
```

## Docker & docker compose

[Docs](https://docs.docker.com/engine/install/ubuntu/)

```bash
# uninstall preexisting
sudo apt remove -y docker docker-engine docker.io docker-compose golang-docker-credential-helpers containerd runc
sudo apt autoremove -y
sudo rm -rf ~/.docker

# install dependancies
sudo apt install -y apt-transport-https ca-certificates curl gnupg gnupg-agent software-properties-common lsb-release

# install docker-ce
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# groups
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

## Python

```bash
# for installing past pythons
sudo add-apt-repository --yes ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y curl python3-dev python3.8-dev build-essential python3-testresources

# pipenv
curl -o - https://bootstrap.pypa.io/get-pip.py | sudo -H python3 -
sudo -H pip3 install pipenv
sudo -H pip3 install virtualenvwrapper
cat >> ~/.bashrc <<EOL

# Python Virtual Environments
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=~/.python_virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
EOL
```

## Node

[Docs](https://github.com/nodesource/distributions/blob/master/README.md#debinstall)

```bash
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs build-essential gcc g++ make

## To install the Yarn package manager, run:
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarnkey.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn
```

## Brave

[Docs](https://brave.com/linux/#debian-9-ubuntu-1604-and-mint-18)

```bash
sudo apt install apt-transport-https gnupg
curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser
```

## anydesk

[Docs](https://computingforgeeks.com/how-to-install-anydesk-on-ubuntu/)

```bash
wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo apt-key add -
echo "deb http://deb.anydesk.com/ all main" | sudo tee /etc/apt/sources.list.d/anydesk-stable.list
sudo apt-get update && sudo apt-get install anydesk
```

## htop

[Docs](https://htop.dev/)

```bash
sudo apt-get install -y htop
```
