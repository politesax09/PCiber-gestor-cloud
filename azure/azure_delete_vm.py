from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

from azure_auth import subscription_id, credentials


# Configura el ID de la suscripción y el nombre del grupo de recursos
resource_group_name = 'PCiber'

# Configura el nombre de la máquina virtual que deseas eliminar
vm_name = 'mv1'

# Crea una instancia del cliente de administración de computación de Azure
compute_client = ComputeManagementClient(credentials, subscription_id)

# Elimina la máquina virtual
compute_client.virtual_machines.begin_delete(resource_group_name, vm_name).wait()

print(f"La máquina virtual '{vm_name}' ha sido eliminada correctamente.")