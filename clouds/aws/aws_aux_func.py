import boto3


def get_vpc_id(vpc_name):
    ec2_client = boto3.client('ec2')

    try:
        response = ec2_client.describe_vpcs(Filters=[{'Name': 'tag:Name', 'Values': [vpc_name]}])
        vpcs = response['Vpcs']
        if vpcs:
            return vpcs[0]['VpcId']
        else:
            print("No se encontró ninguna VPC con ese nombre")
            return None
    except Exception as e:
        print("Error al obtener el ID de la VPC:", str(e))
        return None



def get_subnet_id(subnet_name):
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.describe_subnets(Filters=[{'Name': 'tag:Name', 'Values': [subnet_name]}])
        subnets = response['Subnets']
        if subnets:
            return subnets[0]['SubnetId']
        else:
            print("No se encontró ninguna subred con ese nombre")
            return None
    except Exception as e:
        print("Error al obtener el ID de la subred:", str(e))
        return None


def get_ami_id(ami_name):
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.describe_images(Filters=[{'Name': 'name', 'Values': [ami_name]}])
        images = response['Images']
        if images:
            return images[0]['ImageId']
        else:
            print("No se encontró ninguna imagen con ese nombre")
            return None
    except Exception as e:
        print("Error al obtener el ID de la imagen:", str(e))
        return None
    
def get_vm_id(vm_name):
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [vm_name]}])
        reservations = response['Reservations']
        if reservations:
            return reservations[0]['Instances'][0]['InstanceId']
        else:
            print("No se encontró ninguna instancia con ese nombre")
            return None
    except Exception as e:
        print("Error al obtener el ID de la instancia:", str(e))
        return None


def get_ip_id(ip_address):
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.describe_addresses(Filters=[{'Name': 'public-ip', 'Values': [ip_address]}])
        addresses = response['Addresses']
        if addresses:
            return addresses[0]['AllocationId']
        else:
            print("No se encontró ninguna dirección IP con esa dirección")
            return None
    except Exception as e:
        print("Error al obtener el ID de la dirección IP:", str(e))
        return None


def get_dns_zone_id(zone_name):
    client = boto3.client('route53')
    try:
        response = client.list_hosted_zones_by_name(DNSName=zone_name)
        zones = response['HostedZones']
        if zones:
            return zones[0]['Id'].split('/')[-1]
        else:
            print("No se encontró ninguna zona DNS con ese nombre")
            return None
    except Exception as e:
        print("Error al obtener el ID de la zona DNS:", str(e))
        return None


def select_ami(ami_selection):
    if ami_selection == "ubuntu":
        return "ami-04b70fa74e45c3917"
    elif ami_selection == "debian":
        return "ami-058bd2d568351da34"
    elif ami_selection == "amazon":
        return "ami-01b799c439fd5516a"
    elif ami_selection == "win-server-22":
        return "ami-04df9ee4d3dfde202"
    elif ami_selection == "win-server-19":
        return "ami-0e9a81e2d672e1017"
    else:
        print("AMI no reconocida")
        return None
    

def list_vm_names():
    # Crea una sesión de AWS
    session = boto3.Session()
    # Crea un cliente de EC2
    ec2_client = session.client('ec2')
    # Obtiene todas las instancias EC2
    response = ec2_client.describe_instances()
    # Itera sobre las reservas de instancias
    name_list = []
    for reservation in response['Reservations']:
        # Itera sobre las instancias dentro de cada reserva
        for instance in reservation['Instances']:
            # Obtiene la información deseada de cada instancia
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    name_list.append(tag['Value'])
                    break
    return name_list