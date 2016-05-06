# BigData_Project

load taxi data to ec2 by using wget of links files in data:

wget -i links

upload taxi data to s3 by using:

aws s3 cp folder s3://bucket_name/folder --recursive
