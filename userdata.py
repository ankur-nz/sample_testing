import boto3
import base64
import sys
import os

if os.path.exists("output.csv"):
    os.remove("output.csv")
else:
    print("")
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances :
    response = instance.describe_attribute(Attribute='userData')
    if 'UserData' in response and response['UserData']:
        print((base64.b64decode(response['UserData']['Value'])), file=open("output.csv", "a"))
        print("\n",file=open("output.csv", "a"))
    print((
         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
         )
     ),file=open("output.csv", "a"))
    