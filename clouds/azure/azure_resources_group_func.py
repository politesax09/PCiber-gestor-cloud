from azure.mgmt.resource import ResourceManagementClient

from clouds.azure.azure_auth import credentials, subscription_id

def azure_list_resource_groups():
    resource_client = ResourceManagementClient(credentials, subscription_id)

    # Get a list of resource groups
    resource_groups = resource_client.resource_groups.list()

    # Iterate over the resource groups and print their names and statuses
    for resource_group in resource_groups:
        print(f"Resource Group: {resource_group.name}")
        print(f"Status: {resource_group.properties.provisioning_state}")
        print("")




def azure_list_resources_from_group(resource_group_name):
    # Cliente de administración de recursos
    resource_client = ResourceManagementClient(credentials, subscription_id)

    # Obtener los recursos del grupo de recursos
    resources = resource_client.resources.list_by_resource_group(resource_group_name)

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



def azure_list_resources_by_type():
    # FIXME: Error .list() por el resource_provider_namespace

    # Configura el cliente de administración de recursos
    resource_client = ResourceManagementClient(credentials, subscription_id)

    # Obtiene todos los tipos de recursos disponibles
    # resource_types = resource_client.resource_types.list()
    resource_types = resource_client.provider_resource_types.list(resource_provider_namespace='Microsoft.Resources')

    # Itera sobre los tipos de recursos y lista los recursos activos de cada tipo
    for resource_type in resource_types:
        resources = resource_client.resources.list_by_type(resource_type.resource_type)
        print(f"Recursos del tipo {resource_type.resource_type}:")
        for resource in resources:
            print(f"- {resource.name} ({resource.id})")