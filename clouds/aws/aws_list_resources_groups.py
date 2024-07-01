import boto3


# FIXME: Intenta listar los grupos de recursos pero la lista está vacía

def list_resource_groups():
    # Crea una instancia del cliente de AWS Resource Groups
    client = boto3.client('resource-groups')

    # Obtiene la lista de grupos de recursos
    response = client.list_groups()
    print(response)
    # response = client.list_group_resources()

    # Itera sobre los grupos de recursos y muestra sus características
    for group in response['Groups']:
        group_name = group['GroupName']
        group_description = group['Description']
        group_arn = group['GroupArn']
        print(f"Nombre del grupo: {group_name}")
        print(f"Descripción del grupo: {group_description}")
        print(f"ARN del grupo: {group_arn}")
        print("")

# Llama a la función para listar los grupos de recursos
list_resource_groups()


# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print()
#     print(bucket.name)
#     print()


