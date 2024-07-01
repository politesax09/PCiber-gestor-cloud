import boto3

# def list_resources_by_type():
#     # Crea una instancia del cliente de AWS
#     client = boto3.client('ec2')

#     # Obtiene la lista de tipos de recursos disponibles
#     resource_types = client.describe_instance_types()

#     # Itera sobre cada tipo de recurso y obtiene los recursos activos
#     for resource_type in resource_types:
#         # Obtiene los recursos activos para el tipo de recurso actual
#         resources = client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

#         # Imprime el tipo de recurso y la lista de recursos activos
#         print(f"Tipo de recurso: {resource_type}")
#         for resource in resources['Reservations']:
#             for instance in resource['Instances']:
#                 print(f"ID de instancia: {instance['InstanceId']}")
#                 # Agrega aquí cualquier otra información que desees mostrar

#         print()  # Agrega una línea en blanco para separar los resultados de cada tipo de recurso

# # Llama a la función para listar los recursos por tipo
# list_resources_by_type()

def list_resources_by_type():
    # Crea una instancia del cliente de AWS
    client = boto3.client('ec2')
    # Obtiene la lista de tipos de recursos disponibles
    resource_types = client.describe_instance_types()
    # Itera sobre cada tipo de recurso y obtiene los recursos activos
    for resource_type in resource_types:
        # Obtiene los recursos activos para el tipo de recurso actual
        resources = client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        # Imprime el tipo de recurso y la lista de recursos activos
        print(f"Tipo de recurso: {resource_type}")
        for resource in resources['Reservations']:
            for instance in resource['Instances']:
                print(f"ID de instancia: {instance['InstanceId']}")
                # Agrega aquí cualquier otra información que desees mostrar
                print(f"Nombre de recurso: {instance['Tags'][0]['Value']}")
        print()  # Agrega una línea en blanco para separar los resultados de cada tipo de recurso

# Llama a la función para listar los recursos por tipo
list_resources_by_type()