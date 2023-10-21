import boto3

def lambda_handler(event, context):
    # Verifica si se proporcionaron el nombre del bucket y la clave del archivo en el evento
    if 'bucket_name' in event and 'file_key' in event:
        bucket_name = event['bucket_name']
        file_key = event['file_key']
    else:
        return {
            'statusCode': 400,
            'body': 'Faltan parámetros requeridos: bucket_name y file_key en el evento.'
        }
    
    # Configura el cliente de S3
    s3_client = boto3.client('s3')
    
    try:
        # Obtiene el objeto del archivo desde S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        
        # Lee el contenido del objeto (archivo)
        file_content = response['Body'].read()
        
        # Realiza aquí las operaciones que necesitas con el contenido del archivo
        
        # Por ejemplo, puedes imprimir el contenido
        print(file_content)
        
        return {
            'statusCode': 200,
            'body': 'Archivo obtenido exitosamente.'
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error al obtener el archivo.'
        }
