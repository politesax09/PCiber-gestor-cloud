import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()


def listar_recursos_azure(subscription_id, resource_group):
    # Obtener el token de acceso
    token_url = os.environ['TOKEN_URL']
    client_id = os.environ['AZURE_CLIENT_ID']
    client_secret = os.environ['AZURE_CLIENT_SECRET']
    tenant_id = os.environ['AZURE_TENANT_ID']
    resource = "https://management.azure.com/"

    token_payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "resource": resource
    }

    token_response = requests.post(token_url.format(tenant_id=tenant_id), data=token_payload)
    print(token_response.json())
    # access_token = token_response.json()["access_token"]

    # # Obtener la lista de recursos
    # resources_url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/resources?api-version=2021-04-01"

    # headers = {
    #     "Authorization": f"Bearer {access_token}",
    #     "Content-Type": "application/json"
    # }

    # resources_response = requests.get(resources_url, headers=headers)
    # resources_json = resources_response.json()

    # # Mostrar los recursos y su estado
    # for resource in resources_json["value"]:
    #     resource_name = resource["name"]
    #     resource_type = resource["type"]
    #     resource_state = resource["properties"]["provisioningState"]
    #     print(f"Recurso: {resource_name} ({resource_type}), Estado: {resource_state}")

# Ejemplo de uso
subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
resource_group = "PCiber"

listar_recursos_azure(subscription_id, resource_group)