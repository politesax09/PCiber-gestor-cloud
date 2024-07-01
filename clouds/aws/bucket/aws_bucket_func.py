import boto3

# FIXME: Error en LocationConstraint, dice que es ilegal y si lo dejo en blanco dice que falta

def create_bucket(bucket_name):
    # Crea una instancia del cliente de S3
    s3_client = boto3.client('s3')

    # Crea el bucket S3 con la ubicación adecuada
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

    print(f"Bucket '{bucket_name}' creado exitosamente.")


def delete_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    
    # Eliminar todos los objetos dentro del bucket
    bucket.objects.all().delete()
    
    # Eliminar el bucket
    bucket.delete()
    print(f"Bucket '{bucket_name}' eliminado exitosamente.")



def list_buckets():
    # Crea una instancia del cliente de AWS S3
    s3_client = boto3.client('s3')

    # Obtiene la lista de buckets S3
    response = s3_client.list_buckets()

    # Imprime el nombre de cada bucket
    for bucket in response['Buckets']:
        print(f"  - {bucket['Name']}")



def configure_web_bucket(bucket_name, file_name):
    # Crea una instancia del cliente de S3
    s3_client = boto3.client('s3')

    # Configura las opciones de hosting estático para el bucket
    s3_client.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration={
            'IndexDocument': {'Suffix': 'index.html'},
            'ErrorDocument': {'Key': 'error.html'}
        }
    )

    # Configura las políticas de acceso público para el archivo
    s3_client.put_object_acl(
        ACL='public-read',
        Bucket=bucket_name,
        Key=file_name
    )

    # Obtiene la URL del archivo
    file_url = f"http://{bucket_name}.s3-website.{s3_client.meta.region_name}.amazonaws.com/{file_name}"
    print(f"El archivo está disponible en: {file_url}")



def download_file_from_bucket(bucket_name, file_key, local_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, file_key, local_path)
        print(f"Archivo descargado exitosamente en {local_path}")
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")



def upload_file_to_bucket(file_path, bucket_name, object_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print("Archivo subido exitosamente.")
    except Exception as e:
        print("Error al subir el archivo:", e)
    





