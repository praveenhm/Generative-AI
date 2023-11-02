```zsh
# Install lazydocker
mkdir -p $HOME/bin
wget https://github.com/jesseduffield/lazydocker/releases/download/v0.16/lazydocker_0.16_Linux_x86_64.tar.gz
tar xzvf lazydocker_0.16_Linux_x86_64.tar.gz lazydocker -C $HOME/bin
rm lazydocker_0.16_Linux_x86_64.tar.gz

# Add $HOME/bin to your PATH if not already added
echo 'export PATH=$HOME/bin:$PATH' >> ~/.zshrc
source ~/.zshrc

# Running docker image
docker run --rm -it <IMAGE_NAME>


# Pull the Image:
docker pull <image-name>

# Run the Image:
docker run <options> <image-name>

# For example, to run Nginx:
docker run -d -p 8080:80 --name nginx-container nginx

# Check Running Containers:
docker ps

# To see all containers (including stopped ones):
docker ps -a

# Interact with the Container:
docker exec -it <container-name-or-id> /bin/sh

# Stop the Container:
docker stop <container-name-or-id>

# Remove the Container:
docker rm <container-name-or-id>


## When docker is run with an image like python:latest, it starts a container with that image and runs the default command associated with the image. For the python:latest image, the default command is python3. Since there's no script or interactive shell attached to it, the Python interpreter exits immediately after being started, which results in the container also exiting immediately.

# To run a Python container interactively, use the -it flags and attach a shell, like bash:

docker run -it python:latest bash

