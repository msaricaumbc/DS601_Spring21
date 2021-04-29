#!/usr/bin/env bash
cd /home/ec2-user
su ec2-user

sudo yum update -y

aws s3 cp s3://com.msarica.ds/server.txt ./server.py
aws s3 cp s3://com.msarica.ds/model.pickle ./model.pickle

sudo pip3 install nltk
sudo pip3 install scikit-learn=='0.21.3'
sudo pip3 install flask
sudo pip3 install flask_cors
sudo pip3 install waitress

sudo python3 server.py