import boto3

def create_vm(instance_name, type, id_ami, id_subnet, key_name):
    session = boto3.Session()

    # Crea una instancia de EC2
    ec2 = session.resource('ec2')
    instance = ec2.create_instances(
        # Ubuntu Server 20.04 LTS (HVM), SSD Volume Type
        ImageId=id_ami,
        MinCount=1,
        MaxCount=1,
        InstanceType=type,
        KeyName=key_name,
        SubnetId=id_subnet
    )

    # Espera a que la instancia esté en estado 'running'
    instance[0].wait_until_running()
    instance[0].create_tags(Tags=[{'Key': 'Name', 'Value': instance_name}])


    # Obtiene la IP pública de la instancia
    public_ip = instance[0].public_ip_address

    print(f"La instancia se ha creado correctamente. Nombre: {instance_name}, IP pública: {public_ip}")


def delete_vm(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    
    # Verificar el estado de la instancia
    if instance.state['Name'] == 'stopped':
        print(f"La instancia {instance_id} está detenida.")
    elif instance.state['Name'] == 'running':
        print(f"La instancia {instance_id} está en funcionamiento.")
        # Detener la instancia antes de eliminarla
        instance.stop()
        instance.wait_until_stopped()
    else:
        print(f"El estado de la instancia {instance_id} es desconocido.")
    
    # Eliminar la instancia
    instance.terminate()
    instance.wait_until_terminated()
    
    print(f"La instancia {instance_id} ha sido eliminada exitosamente.")



def list_vms():
    # Crea una sesión de AWS
    session = boto3.Session()
    # Crea un cliente de EC2
    ec2_client = session.client('ec2')
    # Obtiene todas las instancias EC2
    response = ec2_client.describe_instances()
    # Itera sobre las reservas de instancias
    for reservation in response['Reservations']:
        # Itera sobre las instancias dentro de cada reserva
        for instance in reservation['Instances']:
            # Obtiene la información deseada de cada instancia
            nombre = ''
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    nombre = tag['Value']
                    break
            id_instance = instance['InstanceId']
            status = instance['State']['Name']
            instance_type = instance['InstanceType']
            public_ip = instance['PublicIpAddress'] if 'PublicIpAddress' in instance else 'N/A'
            # Obtiene el nombre del par de claves SSH
            key_name = instance['KeyName'] if 'KeyName' in instance else 'N/A'
            # Imprime la información de la instancia
            print(f"Nombre: {nombre} | ID: {id_instance} | Estado: {status} | Tipo de instancia: {instance_type} | IP pública asignada: {public_ip} | Claves SSH: {key_name}")
            print()



def start_vm(instance_id):
    ec2 = boto3.client('ec2')
    response = ec2.start_instances(InstanceIds=[instance_id])
    print("La instancia se ha iniciado correctamente.")



def stop_vm(instance_id):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(InstanceIds=[instance_id])
    print("La instancia se ha detenido correctamente.")


