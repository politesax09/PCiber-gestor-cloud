from azure.mgmt.resource import ResourceManagementClient

from azure_auth import credentials, subscription_id



def list_resources_from_group(resource_group_name):
    # Cliente de administración de recursos
    resource_client = ResourceManagementClient(credentials, subscription_id)

    # Obtener los recursos del grupo de recursos
    resources = resource_client.resources.list_by_resource_group(resource_group_name)

    print()
    print()
    # Imprimir los recursos y sus características
    for resource in resources:
        print(f"Nombre: {resource.name}")
        print(f"Tipo: {resource.type}")
        print(f"Ubicación: {resource.location}")
        print(f"Etiquetas: {resource.tags}")
        print(f"Propiedades: {resource.properties}")
        print("-----------------------------------")
    print()
    print()

# Llamar a la función para listar los recursos del grupo de recursos
list_resources_from_group('PCiber')