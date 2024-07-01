import boto3

def create_dns_zone(zone_name):
    client = boto3.client('route53')

    response = client.create_hosted_zone(
        Name=zone_name,
        CallerReference=str(hash(zone_name)),
        HostedZoneConfig={
            'Comment': 'Created by AWS SDK',
            'PrivateZone': False
        }
    )

    print(f'Zona alojada DNS creada con ID: {response['HostedZone']['Id']}')

def delete_dns_zone(zone_id):
    client = boto3.client('route53')
    
    response = client.delete_hosted_zone(Id=zone_id)
    
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Zona DNS eliminada exitosamente.")
    else:
        print("Error al eliminar la zona DNS.")



def list_dns_zones():
    # Crea una instancia del cliente de Route 53
    client = boto3.client('route53')
    # Obtiene todas las zonas DNS alojadas en Route 53
    response = client.list_hosted_zones()
    # Imprime el nombre, descripción, recuento de registros e ID de cada zona DNS
    for zone in response['HostedZones']:
        zone_name = zone['Name']
        zone_description = zone['Config']['Comment']
        zone_record_count = zone['ResourceRecordSetCount']
        zone_id = zone['Id'].split('/')[-1]
        print(f"Nombre: {zone_name} | Descripción: {zone_description} | Recuento de registros: {zone_record_count} | ID: {zone_id}")
        print()



def create_dns_record(zone_id, record_name, record_type, record_value):
    client = boto3.client('route53')
    
    response = client.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': record_name,
                        'Type': record_type,
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': record_value
                            }
                        ]
                    }
                }
            ]
        }
    )
    
    print("Registro DNS creado correctamente.")



def delete_dns_record(zone_id, record_name, record_type):
    client = boto3.client('route53')
    
    response = client.list_resource_record_sets(HostedZoneId=zone_id)
    record_sets = response['ResourceRecordSets']
    
    for record_set in record_sets:
        if record_set['Name'] == record_name and record_set['Type'] == record_type:
            changes = [
                {
                    'Action': 'DELETE',
                    'ResourceRecordSet': record_set
                }
            ]
            
            response = client.change_resource_record_sets(
                HostedZoneId=zone_id,
                ChangeBatch={
                    'Changes': changes
                }
            )
            
            print(f"Registro {record_name} ({record_type}) eliminado con éxito.")
            return
    
    print(f"No se encontró el registro {record_name} ({record_type}).")



def list_dns_records(zone_id):
    client = boto3.client('route53')
    
    response = client.list_resource_record_sets(
        HostedZoneId=zone_id
    )
    
    records = response['ResourceRecordSets']
    
    for record in records:
        print(f"Name: {record['Name']}, Type: {record['Type']}, Value: {record['ResourceRecords'][0]['Value']}")

