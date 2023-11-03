```zsh
# install Zsh locally by getting latest from Zsh website
wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download
tar -xf zsh.tar.xz

# Zsh requires ncurses source
wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.2.tar.gz
tar -xzvf ncurses-6.2.tar.gz
cd ncurses-6.2

# Clean up any previous build artifacts
make distclean

# Configure with -fPIC
CPPFLAGS="-fPIC" ./configure --prefix=/home/praveen/local

# Compile and install
make
make install

### Now back to Zsh
cd /home/praveen/zsh-*

### Clean up any previous build artifacts
make clean

# Configure and compile again
./configure --prefix=/home/praveen/local CPPFLAGS="-I/home/praveen/local/include" LDFLAGS="-L/home/praveen/local/lib"
make
make install


### Install ohmyzsh
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

##start new shell
/home/praveen/local/bin/zsh

source ~/.zshrc

======Install docker as rootless==========

# Follow instructions on docker site, prerequisite
uname -r
whoami
grep ^$(whoami): /etc/subuid
grep ^$(whoami): /etc/subgid
id -u

curl -o docker-rootless.sh https://get.docker.com/rootless
chmod +x docker-rootless.sh
SKIP_IPTABLES=1 ./docker-rootless.sh

# To control docker.service, run: 
systemctl --user (start|stop|restart) docker.service

docker info
docker status
docker ps
ps aux | grep dockerd

==============ncdu================

wget https://dev.yorhel.nl/download/ncdu-2.3-linux-x86_64.tar.gz
tar -xzvf ncdu-1.16.tar.gz
mv ncdu $HOME/local/bin/

===========vs code cli================
# install vsc code cli for remote ssh
curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz
tar -xf vscode_cli.tar.gz
mv code ~/bin
code tunnel

