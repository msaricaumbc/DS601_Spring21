#!/usr/bin/env bash
cd /home/ec2-user
su ec2-user

sudo yum update -y

# install docker
sudo yum install -y docker

# start docker service
sudo service docker start

# In order to user docker command without root privileges (sudo), we need to add ec2-user to the docker group
sudo usermod -aG docker ec2-user

sudo docker run --publish 80:80 msarica/docker-601-demo