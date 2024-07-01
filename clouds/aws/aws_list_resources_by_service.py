import boto3

def list_resources_by_service():
    # Inicializar el cliente de AWS
    client = boto3.client('resourcegroupstaggingapi')

    # Obtener una lista de todos los servicios de AWS
    services = client.get_tag_keys()

    # Iterar sobre cada servicio y obtener los recursos asociados
    for service in services['TagKeys']:
        # Obtener los recursos asociados al servicio
        response = client.get_resources(
            TagFilters=[
                {
                    'Key': service
                }
            ]
        )

        # Imprimir los recursos asociados al servicio
        print(f"Recursos para el servicio {service}:")
        for resource in response['ResourceTagMappingList']:
            print(resource['ResourceARN'])

# Llamar a la función para listar los recursos por servicio
list_resources_by_service()

