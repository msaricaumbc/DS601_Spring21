aws s3 cp s3://com.msarica.ds/server.txt ./server.py
aws s3 cp s3://com.msarica.ds/model.pickle ./model.pickle
docker build -t msarica/docker-601-demo .

# docker push msarica/docker-601-demo

# docker run --publish 80:80 msarica/docker-601-demo