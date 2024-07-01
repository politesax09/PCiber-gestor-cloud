import boto3


def create_ip(ip_name):
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.allocate_address(Domain='vpc')
    
    public_ip = response['PublicIp']
    allocation_id = response['AllocationId']
    
    # Assign a name to the IP
    ec2_client.create_tags(Resources=[allocation_id], Tags=[{'Key': 'Name', 'Value': ip_name}])

    print(f"IP Publica: {public_ip}")
    print(f"Allocation IP: {allocation_id}")



def delete_ip(id_ip_address):
    ec2 = boto3.client('ec2')
    
    try:
        response = ec2.release_address(AllocationId=id_ip_address)
        print("La dirección IP {} ha sido eliminada exitosamente.".format(id_ip_address))
    except Exception as e:
        print("Error al eliminar la dirección IP: {}".format(str(e)))


def list_ips():
    # Crea una instancia del cliente EC2
    ec2_client = boto3.client('ec2')

    # Obtiene todas las direcciones IP
    response = ec2_client.describe_addresses()
    # Itera sobre las direcciones IP y las imprime junto con el nombre y el ID de asignación
    for address in response['Addresses']:
        print(f"IP: {address['PublicIp']} | Nombre: {address.get('Tags', [{}])[0].get('Value', 'N/A')} | ID de Asignación: {address.get('AllocationId', 'N/A')}")
    print()


def attach_public_ip(instance_id):
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    if 'Reservations' in response and len(response['Reservations']) > 0:
        instance = response['Reservations'][0]['Instances'][0]
        if 'NetworkInterfaces' in instance and len(instance['NetworkInterfaces']) > 0:
            network_interface_id = instance['NetworkInterfaces'][0]['NetworkInterfaceId']
            response = ec2_client.modify_network_interface_attribute(
                NetworkInterfaceId=network_interface_id,
                SourceDestCheck={'Value': False}
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                print("IP pública asignada correctamente.")
            else:
                print("Error al asignar la IP pública.")
        else:
            print("La instancia no tiene interfaces de red.")
    else:
        print("No se encontró la instancia con el ID especificado.")



def detach_public_ip(instance_id):
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    if 'Reservations' in response and len(response['Reservations']) > 0:
        instance = response['Reservations'][0]['Instances'][0]
        if 'PublicIpAddress' in instance:
            public_ip = instance['PublicIpAddress']
            response = ec2_client.disassociate_address(PublicIp=public_ip)
            print(f"La dirección IP pública {public_ip} ha sido desasignada correctamente.")
        else:
            print("La instancia no tiene una dirección IP pública asignada.")
    else:
        print("No se encontró ninguna instancia con el ID especificado.")