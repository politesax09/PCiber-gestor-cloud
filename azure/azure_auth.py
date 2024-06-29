from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
import os
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential

load_dotenv()

client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
vault_url = os.environ['AZURE_VAULT_URL']
secret_name = os.environ['PCIBER_SECRET_NAME']
subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']

# Crear objeto credenciales
credentials = ClientSecretCredential(
    client_id = client_id,
    client_secret = client_secret,
    tenant_id = tenant_id
)

# Crear objeto cliente de secretos
# secret_client = SecretClient(vault_url=vault_url, credential=credentials)

# Obtener valor del secreto de la boveda de claves
# secret_value = secret_client.get_secret(secret_name)

# print('Secreto de la boveda: ', secret_value.value)
