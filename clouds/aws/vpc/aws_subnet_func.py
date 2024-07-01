import boto3


def create_subnet(vpc_id, cidr_block, subnet_name):
    ec2 = boto3.client('ec2')
    
    response = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock=cidr_block
    )
    
    subnet_id = response['Subnet']['SubnetId']
    
    # Add a name tag to the subnet
    ec2.create_tags(
        Resources=[subnet_id],
        Tags=[
            {
                'Key': 'Name',
                'Value': subnet_name
            },
        ]
    )
    print(f'Subnet created with ID: {subnet_id}')


def delete_subnet(subnet_id):
    ec2_client = boto3.client('ec2')
    
    try:
        response = ec2_client.delete_subnet(SubnetId=subnet_id)
        print("Subnet deleted successfully")
    except Exception as e:
        print("Error deleting subnet:", str(e))
