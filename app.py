import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region as needed

# Launch instance
response = ec2.run_instances(
    ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI (example for us-east-1)
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='your-key-pair-name',  # Replace with your existing key pair name
    SecurityGroupIds=['sg-0123456789abcdef0'],  # Replace with your security group ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyFirstInstance'}
            ]
        }
    ]
)

print("Launched EC2 Instance with ID:", response['Instances'][0]['InstanceId'])

