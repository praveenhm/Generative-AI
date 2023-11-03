```zsh
## install Zsh locally
# Get Zsh source (you can find the latest version from the Zsh website)
wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download
tar -xf zsh.tar.xz

# Download ncurses source
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

### Zsh
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

=========docker==========

# To control docker.service, run: 
 systemctl --user (start|stop|restart) docker.service

# To run docker.service on system startup, run: 
 sudo loginctl enable-linger praveen


uname -r
whoami
grep ^$(whoami): /etc/subuid
grep ^$(whoami): /etc/subgid
id -u
curl -o docker-rootless.sh https://get.docker.com/rootless
chmod +x docker-rootless.sh
SKIP_IPTABLES=1 ./docker-rootless.sh

docker info
docker status
docker ps
ps aux | grep dockerd\n


==============ncdu================

wget https://dev.yorhel.nl/download/ncdu-2.3-linux-x86_64.tar.gz
tar -xzvf ncdu-1.16.tar.gz
mv ncdu $HOME/local/bin/

# below steps are not required
ln -s $HOME/local/include/ncurses/curses.h $HOME/local/include/
ln -s $HOME/local/include/ncurses/ncurses.h $HOME/local/include/

./configure --prefix=$HOME/local CPPFLAGS="-I$HOME/local/include" LDFLAGS="-L$HOME/local/lib" LIBS="-lncurses"

make
make install

