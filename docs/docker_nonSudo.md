```zsh
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


# Install lazydocker
mkdir -p $HOME/bin
wget https://github.com/jesseduffield/lazydocker/releases/download/v0.23.1/lazydocker_0.23.1_Linux_x86_64.tar.gz
tar xzvf lazydocker_0.23.1_Linux_x86_64.tar.gz
mv lazydocker ~/bin
find / -name lazydocker 2>/dev/null

# Add $HOME/bin to your PATH if not already added
echo 'export PATH=$HOME/bin:$PATH' >> ~/.zshrc
source ~/.zshrc

# docker images are stored in this directory
~/.local/share/docker

# Pull the Image:
docker pull <image-name>

# Running docker image, name and remove immediately
docker run --name <name> --rm -it <IMAGE_NAME>

# To see all containers (including stopped ones):
docker ps -a

# To check images
docker images

# Interact with the Container:
docker exec -it <container-name-or-id> /bin/sh

# Stop the Container:
docker stop <container-name-or-id>

# Remove the Container:
docker rm <container-name-or-id>

# For example, to run Nginx:
docker run -d -p 8080:80 --name nginx-container nginx


## When docker is run with an image like python:latest, it starts a container with that image and runs the default
# command associated with the image. For the python:latest image, the default command is python3. Since there's no
# script or interactive shell attached to it, the Python interpreter exits immediately after being started, which
# results in the container also exiting immediately.
# To run a Python container interactively, use the -it flags and attach a shell, like bash:

docker run --name py3 -it python:latest bash

# To control docker.service, run: 

# basic commands
	  docker info
	  docker status
	  docker ps
	  ps aux | grep dockerd


# Testing docker
  	systemctl (start|stop|restart|status) docker.service
	ps aux | grep dockerd #check docker process running
		
# docker logs
	sudo journalctl -xeu docker.service
	sudo journalctl -u docker.service

Run local docker:
docker run --rm --name pyContainer -v ./:/work --network=host -it python:3.11.6-slim-bullseye /bin/bash
