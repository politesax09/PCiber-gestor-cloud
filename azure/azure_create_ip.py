from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

from azure_auth import subscription_id, credentials, location

# FIXME: Ignora el nombre introducido para la ip y pone el que quiere


# Configura la suscripción y el grupo de recursos
resource_group_name = 'PCiber'

# Configura el cliente de administración de red
network_client = NetworkManagementClient(credentials, subscription_id)

# Configura los parámetros para la dirección IP pública
public_ip_name = 'ip1-test'
public_ip_params = {
    'location': location,
    'public_ip_allocation_method': 'Dynamic'
}

# Crea la dirección IP pública
public_ip_result = network_client.public_ip_addresses.begin_create_or_update(
    resource_group_name,
    public_ip_name,
    public_ip_params
).result()

# Imprime la dirección IP pública creada
print(f'Se ha creado la dirección IP pública: {public_ip_result.ip_address}')