from azure.mgmt.compute import ComputeManagementClient

from azure_auth import subscription_id, credentials


# Configura el ID de la suscripción y el nombre del grupo de recursos
resource_group_name = 'PCiber'

# Configura el nombre de la máquina virtual que deseas detener
vm_name = 'vm1'

# Crea una instancia del cliente de administración de computación de Azure
compute_client = ComputeManagementClient(credentials, subscription_id)

# Detiene la máquina virtual
compute_client.virtual_machines.begin_power_off(resource_group_name, vm_name)