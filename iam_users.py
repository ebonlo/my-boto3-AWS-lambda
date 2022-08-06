''' This script is to list all iam users present in my account'''

import boto3
import pprint

session = boto3.session.Session(profile_name="root")
iam = session.resource(service_name="iam")
iam = session.client(service_name="iam")

# Using resource object

#my_users = iam.users.all()
#for each in my_users:
#    print(each.name)

# Using client object
response = iam.list_users().get('Users')
for each in response:
    print(each.get('UserName'))


