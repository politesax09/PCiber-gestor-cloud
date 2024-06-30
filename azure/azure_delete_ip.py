from azure.mgmt.network import NetworkManagementClient

from azure_auth import subscription_id, credentials, location

# FIXME: Elimina correctamete la ip con el nombre que se le ha dado en el codiogo a pesar de 
#  tener uno diferente en la consola web

# Variables de configuración
resource_group_name = 'PCiber'
ip_address_name = 'ip1-test'


# Cliente de administración de red de Azure
network_client = NetworkManagementClient(credentials, subscription_id)

# Eliminar la dirección IP
network_client.public_ip_addresses.begin_delete(resource_group_name, ip_address_name)