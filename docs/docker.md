```zsh
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
