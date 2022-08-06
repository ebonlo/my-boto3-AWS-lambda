''' This script is to list all s3 buckets in my account'''
import boto3
session = boto3.session.Session(profile_name="root")
s3 = session.resource(service_name="s3", region_name="us-east-1")
s3 = session.client(service_name="s3", region_name="us-east-1")

#my_buckets = s3.buckets.all()
#for each in my_buckets:
#    print(each.name)

# using client object
response = s3.list_buckets().get('Buckets')
for each_bucket in response:
    print(each_bucket['Name'])