from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.models import VirtualNetwork, AddressSpace, Subnet

from clouds.azure.azure_auth import credentials, subscription_id


def azure_create_vpc(virtual_network_name, virtual_network_ip_block, subnet_name, subnet_ip_block, resources_group_name):
    # Configura el cliente de administración de red
    network_client = NetworkManagementClient(credentials, subscription_id)

    location = 'eastus'

    # Crea la red virtual
    virtual_network = VirtualNetwork(location=location, address_space=AddressSpace(address_prefixes=[virtual_network_ip_block]))
    virtual_network = network_client.virtual_networks.begin_create_or_update(resources_group_name, virtual_network_name, virtual_network).result()

    # Crea la subred dentro de la red virtual
    subnet = Subnet(name=subnet_name, address_prefix=subnet_ip_block)
    subnet = network_client.subnets.begin_create_or_update(resources_group_name, virtual_network_name, subnet_name, subnet).result()

    print()
    print("Red virtual creada exitosamente.")
    print()




# FIXME: El metodo del SDK se ejecuta bien y da OK pero la red no se elimina

def azure_delete_vpc(virtual_network_name, resource_group_name):
    # Crea una instancia del cliente de administración de red
    network_client = NetworkManagementClient(credentials, subscription_id)

    # Elimina la red virtual
    is_done = network_client.virtual_networks.begin_delete(resource_group_name, virtual_network_name).result()
    if is_done:
        print()
        print('La red virtual ha sido eliminada exitosamente.')
        print()
    else:
        print()
        print('Error al eliminar la red virtual.')
        print()



def azure_list_vpcs(resource_group_name):
    # Crea una instancia del cliente de administración de red
    network_client = NetworkManagementClient(credentials, subscription_id)
    # Obtiene todas las redes virtuales en el grupo de recursos especificado
    virtual_networks = network_client.virtual_networks.list(resource_group_name)
    # Itera sobre cada red virtual y muestra su información
    for virtual_network in virtual_networks:
        print(f"Nombre de la red virtual: {virtual_network.name} | Bloque IP: {virtual_network.address_space.address_prefixes[0]}")
        print("Subredes:")
        for subnet in virtual_network.subnets:
            print(f"- Nombre de la subred: {subnet.name} | Bloque IP: {subnet.address_prefix}")
        print()
    print()