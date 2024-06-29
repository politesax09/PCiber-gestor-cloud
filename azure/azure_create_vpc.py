from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.models import VirtualNetwork, AddressSpace, Subnet

from azure_auth import credentials, subscription_id

# TODO: Parametrizar funcion y gestionar opciones introducidas por usuario
# TODO: Controlar si existe una red como la que se va a crear

def create_virtual_network():
    # Configura el cliente de administración de red
    network_client = NetworkManagementClient(credentials, subscription_id)

    # Define los parámetros de la red virtual
    virtual_network_name = "vpc2-pciber"
    virtual_network_ip_block = "20.0.0.0/16"
    subnet_name = "vpc2-ciber-subnet1"
    subnet_ip_block = "20.0.0.0/24"
    location = 'eastus'
    resources_group_name = 'PCiber'

    # Crea la red virtual
    virtual_network = VirtualNetwork(location=location, address_space=AddressSpace(address_prefixes=[virtual_network_ip_block]))
    virtual_network = network_client.virtual_networks.begin_create_or_update(resources_group_name, virtual_network_name, virtual_network).result()

    # Crea la subred dentro de la red virtual
    subnet = Subnet(name=subnet_name, address_prefix=subnet_ip_block)
    subnet = network_client.subnets.begin_create_or_update(resources_group_name, virtual_network_name, subnet_name, subnet).result()

    print()
    print()
    print("Red virtual creada exitosamente.")
    print()
    print()

# Llamada a la funcion
create_virtual_network()