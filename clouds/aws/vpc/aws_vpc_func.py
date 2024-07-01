import boto3

def create_vpc(vpc_name, cidr_block):
    ec2 = boto3.client('ec2')
    
    # Crear la VPC
    response = ec2.create_vpc(
        CidrBlock=cidr_block
    )
    
    vpc_id = response['Vpc']['VpcId']
    
    # Asignar un nombre a la VPC
    ec2.create_tags(
        Resources=[vpc_id],
        Tags=[
            {
                'Key': 'Name',
                'Value': vpc_name
            },
        ]
    )
    
    print(f'VPC creada con éxito. ID: {vpc_id}')



def delete_vpc(vpc_id):
    ec2_client = boto3.client('ec2')
    
    try:
        response = ec2_client.delete_vpc(VpcId=vpc_id)
        print("VPC eliminada exitosamente")
    except Exception as e:
        print("Error al eliminar la VPC:", str(e))




def list_vpcs():
    # Crea una instancia del cliente de AWS para VPC
    ec2_client = boto3.client('ec2')

    # Obtiene todas las VPCs
    response = ec2_client.describe_vpcs()
    # Obtiene los nombres de las VPCs
    vpc_names = []
    for vpc in response['Vpcs']:
        vpc_id = vpc['VpcId']
        vpc_response = ec2_client.describe_tags(Filters=[{'Name': 'resource-id', 'Values': [vpc_id]}])
        for tag in vpc_response['Tags']:
            if tag['Key'] == 'Name':
                vpc_names.append(tag['Value'])
    
    # Obtiene los nombres de las subredes

    subnet_names = []
    for vpc in response['Vpcs']:
        vpc_id = vpc['VpcId']

        subnets_response = ec2_client.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
        subnets = subnets_response['Subnets']
        for subnet in subnets:
            subnet_id = subnet['SubnetId']
            subnet_response = ec2_client.describe_tags(Filters=[{'Name': 'resource-id', 'Values': [subnet_id]}])
            for tag in subnet_response['Tags']:
                if tag['Key'] == 'Name':
                    subnet_names.append(tag['Value'])
    
    # Itera sobre las VPCs y muestra su información
    for i, vpc in enumerate(response['Vpcs']):
        vpc_id = vpc['VpcId']
        cidr_block = vpc['CidrBlock']
        print(f"ID VPC: {vpc_id}")
        if i < len(vpc_names):
            vpc_name = vpc_names[i]
            print(f"Nombre VPC: {vpc_name}")
        else:
            print("Nombre VPC: No disponible")
        print(f"CIDR Block: {cidr_block}")
        
        # Obtiene las subredes asociadas a la VPC
        subnets_response = ec2_client.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
        subnets = subnets_response['Subnets']
        
        # Muestra la información de las subredes
        print()
        print("Subredes:")
        for j, subnet in enumerate(subnets):
            subnet_id = subnet['SubnetId']
            subnet_cidr_block = subnet['CidrBlock']
            subnet_name = subnet_names[j] if j < len(subnet_names) else "Not available"
            print(f"  ID Subred: {subnet_id}")
            print(f"  Nombre Subred: {subnet_name}")
            print(f"  Bloque CIDR: {subnet_cidr_block}")
            print()
        print()
