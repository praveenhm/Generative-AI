```zsh
# with Sudo access, Docker Installation on Rocky Linux 9 Oct 2023 

#Docker:

	find lazydocker
	find / -name lazydocker 2>/dev/null
	which lazydocker

	Often, user-specific binaries might be installed to 
	~/.local/bin or ~/bin
	echo 'export PATH=$PATH:/home/andes/.local/bin' >> ~/.zshrc
	echo "alias ld='lazydocker'" >> ~/.zshrc


# System Clean-up 
	df -Th # storage space
	sudo ncdu /
	sudo du -sh /* 2>/dev/null
	sudo du -sh /* | sort -h

	sudo dnf clean all
	sudo dnf remove $(dnf repoquery --installonly --latest-limit=-2 -q)
	sudo find / -name core -print

	check /var/log and /tmp, /usr, /lib, /bin, 
	Docker, the images and containers by default reside in /var/lib/docker,


# Docker clean-UP
	docker container prune
	docker image prune -a
	docker volume prune
	docker network prune
	docker system prune -a


# Change default docker home from /var/lib/docker:
	Stop docker service:
	sudo systemctl stop docker
	backup
	sudo cp -au /var/lib/docker /path/to/your/backup

	Do not directly edit /lib/systemd/system/docker.service Instead, you should create an override file. The reason for this is that the primary service files in /lib/systemd/system/ can get overwritten when the package is updated, and you might lose your customizations. Using an override in /etc/systemd/system/ ensures your changes persist across package updates.

	sudo systemctl edit docker.service will create below file
	/etc/systemd/system/docker.service.d/override.conf
	or create the directory
	sudo mkdir -p /etc/systemd/system/docker.service.d/ and create override.conf

	Add this

	[Service]
	ExecStart=
	ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --data-root /home/andes/docker

	sudo systemctl daemon-reload
	sudo systemctl restart docker	

# Testing docker
	sudo systemctl status docker.service
	ps aux | grep dockerd #check docker process running
	sudo systemctl start docker 
	sudo dockerd --data-root /home/andes/docker # start manually 


# docker logs
	sudo journalctl -xeu docker.service
	sudo journalctl -u docker.service

# create docker directory 
	sudo mkdir -p /home/andes/docker
	sudo chown -R root:root /home/andes/docker
	sudo chmod -R 0700 /home/andes/docker


Run local docker:
docker run --rm --name pyContainer -v ./:/work --network=host -it python:3.11.6-slim-bullseye /bin/bash




