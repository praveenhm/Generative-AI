### This is basic setting up on rockyLinux as a nonSudo user

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

# Now back to Zsh
cd /home/praveen/zsh-*

# Clean up any previous build artifacts
make clean

# Configure and compile again
./configure --prefix=/home/praveen/local CPPFLAGS="-I/home/praveen/local/include" LDFLAGS="-L/home/praveen/local/lib"
make
make install

# Install ohmyzsh
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

#start new shell
/home/praveen/local/bin/zsh
source ~/.zshrc

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

===============Anaconda python 3.11 & pytorch 2.1 + Cuda 12.1==========================
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh

# Add it to .Zshrc
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('apps/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "apps/anaconda3/etc/profile.d/conda.sh" ]; then
        . "apps/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="apps/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# If you want to activate a specific environment by default when opening a terminal
# conda activate your_environment_name

conda create --name llama --clone base

# pytorch 2.1 with cuda 12.1
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121




========otheres, not really required============

# below steps are not required, use this as template for ncurses
ln -s $HOME/local/include/ncurses/curses.h $HOME/local/include/
ln -s $HOME/local/include/ncurses/ncurses.h $HOME/local/include/

./configure --prefix=$HOME/local CPPFLAGS="-I$HOME/local/include" LDFLAGS="-L$HOME/local/lib" LIBS="-lncurses"

make
make install

==================================END======================
