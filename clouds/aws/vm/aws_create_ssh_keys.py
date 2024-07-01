import boto3

def create_key_pair(key_name):
    ec2 = boto3.client('ec2')
    
    response = ec2.create_key_pair(KeyName=key_name)
    
    private_key = response['KeyMaterial']
    
    # Guarda la clave privada en un archivo
    with open(f'{key_name}.pem', 'w') as f:
        f.write(private_key)
    
    print(f'Se ha creado el par de claves SSH: {key_name}.pem')



def list_key_pairs():
    ec2 = boto3.client('ec2')
    
    response = ec2.describe_key_pairs()
    
    key_pairs = response['KeyPairs']
    
    key_list = []
    for key_pair in key_pairs:
        key_name = key_pair['KeyName']
        key_list.append(key_name)
    return key_list