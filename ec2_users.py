''' This is a script to list all ec2-instance id's in my account'''
import boto3

session = boto3.session.Session(profile_name="ec2_developer")
ec2 = session.resource(service_name="ec2", region_name="us-east-1")
ec2 = session.client(service_name="ec2", region_name="us-east-1")

# Using Resource object

#my_instances = ec2.instances.all()
#for each in my_instances:
#   print(each.instance_id)

# using client object
response = ec2.describe_instances().get('Reservations')
for each in response:
    for each_instance in each['Instances']:
        print(each_instance['InstanceId'])
    