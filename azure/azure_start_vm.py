from azure.mgmt.compute import ComputeManagementClient

from azure_auth import subscription_id, credentials

# TODO: Probar a iniciar y parar maquina virtual

# Configura el ID de la suscripción y el nombre del grupo de recursos
resource_group_name = 'PCiber'

# Configura el nombre de la máquina virtual
vm_name = 'vm1'

# Crea el cliente de administración de computación
compute_client = ComputeManagementClient(credentials, subscription_id)

# Obtiene el estado actual de la máquina virtual
vm = compute_client.virtual_machines.get(resource_group_name, vm_name, expand='instanceView')
if vm.instance_view.statuses[1].code == 'PowerState/deallocated':
    # Si la máquina virtual está detenida, la arranca
    compute_client.virtual_machines.begin_start(resource_group_name, vm_name)
    print('La máquina virtual se ha iniciado correctamente.')
else:
    print('La máquina virtual ya está en ejecución.')
