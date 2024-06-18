from azure.mgmt.resource import ResourceManagementClient

from azure_auth import credentials, subscription_id

def list_resource_groups():
    # Create a credential object using default Azure credentials
    # credential = DefaultAzureCredential()

    # Create a resource management client
    # resource_client = ResourceManagementClient(credential, subscription_id)
    resource_client = ResourceManagementClient(credentials, subscription_id)


    # Get a list of resource groups
    resource_groups = resource_client.resource_groups.list()

    # Iterate over the resource groups and print their names and statuses
    for resource_group in resource_groups:
        print(f"Resource Group: {resource_group.name}")
        print(f"Status: {resource_group.properties.provisioning_state}")
        print("")

# Call the function to list resource groups
list_resource_groups()