# BigData_Project

1. Raw Data:

load taxi data to ec2 by using wget of links files in data:

wget -i links

upload taxi data to s3 by using:

aws s3 cp folder s3://bucket_name/folder --recursive

2. Mapreduce on AWS ERM:
Setup: Hadoop, 20 cores
Python: 2.7.x

