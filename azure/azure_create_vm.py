from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

from azure.mgmt.compute.models import HardwareProfile, NetworkProfile, OSProfile, StorageProfile, VirtualHardDisk, \
    VirtualMachine, VirtualMachineSizeTypes, OSDisk

from azure_auth import credentials, subscription_id, location


# Configura los detalles de la suscripción y el grupo de recursos
resource_group_name = 'PCiber'

# Configura los detalles de la máquina virtual
vm_name = 'vm1'
vm_size = 'Standard_B2s'
admin_username = 'adminuser'
admin_password = 'Adminuser-123'
virtual_network_name = 'vpc-pciber'
subnet_name = 'subred1'

# Crea los clientes de administración de recursos, redes, almacenamiento y cómputo
resource_client = ResourceManagementClient(credentials, subscription_id)
network_client = NetworkManagementClient(credentials, subscription_id)
storage_client = StorageManagementClient(credentials, subscription_id)
compute_client = ComputeManagementClient(credentials, subscription_id)

# Crea un grupo de recursos
resource_client.resource_groups.create_or_update(resource_group_name, {'location': location})

# Crea una cuenta de almacenamiento
storage_account_name = 'mv1adfasd'
# storage_client.storage_accounts.create(resource_group_name, storage_account_name, {
storage_client.storage_accounts.begin_create(resource_group_name, storage_account_name, {
    'sku': {'name': 'Standard_LRS'},
    'kind': 'StorageV2',
    'location': location
})

# Crea una interfaz de red
network_interface_name = 'mv1interface'
network_client.network_interfaces.begin_create_or_update(resource_group_name, network_interface_name, {
    'location': location,
    'ip_configurations': [{
        'name': 'ipconfig1',
        'subnet': {'id': '/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/virtualNetworks/{}/subnets/{}'.format(subscription_id, resource_group_name, virtual_network_name, subnet_name)},
    }]
})

# Crea una máquina virtual
vm = VirtualMachine(location=location, os_profile=OSProfile(computer_name='ubuntuserver', admin_username=admin_username, admin_password=admin_password),
                   hardware_profile=HardwareProfile(vm_size=vm_size),
                   network_profile=NetworkProfile(network_interfaces=[{'id': '/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/networkInterfaces/{}'.format(subscription_id, resource_group_name, network_interface_name)}]),
                   storage_profile=StorageProfile(image_reference={'publisher': 'Canonical', 'offer': 'UbuntuServer', 'sku': '16.04-LTS', 'version': 'latest'},
                                                #  os_disk=VirtualHardDisk(create_option='FromImage'),
                                                os_disk=OSDisk(create_option='FromImage'),
                                                 data_disks=[]))

compute_client.virtual_machines.begin_create_or_update(resource_group_name, vm_name, vm)