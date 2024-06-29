from azure.mgmt.network import NetworkManagementClient

from azure_auth import credentials, subscription_id


# BUG: El metodo del SDK se ejecuta bien y da OK pero la red no se elimina

def delete_virtual_network():
    # Define la suscripción y el grupo de recursos
    resource_group_name = 'PCiber'
    virtual_network_name = 'vpc2-ciber'

    # Crea una instancia del cliente de administración de red
    network_client = NetworkManagementClient(credentials, subscription_id)

    # Elimina la red virtual
    is_done = network_client.virtual_networks.begin_delete(resource_group_name, virtual_network_name).result()
    if is_done:
        print()
        print()
        print('La red virtual ha sido eliminada exitosamente.')
        print()
        print()
    else:
        print()
        print()
        print('Error al eliminar la red virtual.')
        print()
        print()
    

# Llamar a la funcion
delete_virtual_network()