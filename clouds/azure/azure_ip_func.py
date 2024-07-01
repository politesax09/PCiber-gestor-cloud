from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

from clouds.azure.azure_auth import subscription_id, credentials, location

# FIXME: Ignora el nombre introducido para la ip y pone el que quiere



def azure_create_ip(resource_group_name, ip_name):
    # Configura el cliente de administración de red
    network_client = NetworkManagementClient(credentials, subscription_id)

    # Configura los parámetros para la dirección IP pública
    public_ip_name = ip_name
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



def azure_delete_ip(resource_group_name, ip_name):
    # Cliente de administración de red de Azure
    network_client = NetworkManagementClient(credentials, subscription_id)

    # Eliminar la dirección IP
    network_client.public_ip_addresses.begin_delete(resource_group_name, ip_name)



def azure_attach_ip(resource_group_name, nic_name, public_ip_name):
    # Configura el cliente de administración de red
    network_client = NetworkManagementClient(credentials, subscription_id)

    # Obtén la NIC actual
    nic = network_client.network_interfaces.get(resource_group_name, nic_name)


    # FIXME: El id de la ip es NoneType asique da error
    # Verifica si la IP pública existe antes de asignarla
    public_ip = network_client.public_ip_addresses.get(resource_group_name, public_ip_name)
    if public_ip is not None:
        public_ip_address_id = public_ip.id
        nic.ip_configurations[0].public_ip_address.id = public_ip_address_id
    else:
        print("La IP pública especificada no existe.")

    # Actualiza la NIC con la nueva configuración
    update_result = network_client.network_interfaces.create_or_update(resource_group_name, nic_name, nic)
    update_result.wait()

    print("La dirección IP pública ha sido actualizada.")