# #!/usr/bin/env bash
# this will also work but installing anaconda is too much for the task

# # ++++++++++++++++++++ START ANACONDA INSTALL +++++++++++++++++++++
# cd /home/ec2-user
# su ec2-user

# # Download the Linux Anaconda Distribution
# # wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O /tmp/anaconda3.sh

# # Run the installer (installing without -p should automatically install into '/' (root dir)
# # bash /tmp/anaconda3.sh -b -p /home/ec2-user/anaconda3
# # rm /tmp/anaconda3.sh

# ### Run the conda init script to setup the shell
# # echo ". /home/ec2-user/anaconda3/etc/profile.d/conda.sh" >> /home/ec2-user/.bashrc
# # . /home/ec2-user/anaconda3/etc/profile.d/conda.sh
# # source /home/ec2-user/.bashrc

# # Create a base Python3 environment separate from the base env
# conda create -y --name python3

# # +++++++++++++++++++++ END ANACONDA INSTALL ++++++++++++++++++++++


# # ++++++++++++++ SETUP ENV +++++++++++++++

# # Install necessary Python packages
# # Note that 'source' is deprecated, so now we should be using 'conda' to activate/deactivate envs
# conda activate python3 
# conda install nltk -y
# conda install scikit-learn=='0.21.3' -y
# conda install Flask -y
# conda install flask_cors -y

# aws s3 cp s3://com.msarica.ds/server.txt ./server.py
# aws s3 cp s3://com.msarica.ds/model.pickle ./model.pickle

# export FLASK_APP=server.py
# flask run --host=0.0.0.0