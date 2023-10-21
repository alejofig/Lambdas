import boto3
from botocore.exceptions import ClientError
import json

def send_email(subject, body, recipient):
    # Configura el cliente SES
    ses_client = boto3.client('ses', region_name='us-east-1')  # Cambia 'us-east-1' a la región que desees

    # Define el remitente (debe estar verificado en SES)
    sender = 'alejofig@alejofig.com'

    # Define el formato del mensaje
    charset = 'UTF-8'

    # Crea el mensaje de correo electrónico
    email = {
        'Subject': {
            'Data': subject,
            'Charset': charset
        },
        'Body': {
            'Text': {
                'Data': body,
                'Charset': charset
            }
        }
    }

    try:
        # Envía el correo electrónico
        response = ses_client.send_email(
            Source=sender,
            Destination={
                'ToAddresses': [recipient]
            },
            Message=email
        )
        return True
    except ClientError as e:
        print(f"Error al enviar el correo electrónico: {e}")
        return False

def lambda_handler(event, context):
    try:
        # Parsea los datos JSON desde el cuerpo de la solicitud POST
        body = json.loads(event['body'])
        subject = body.get('subject', "Asunto predeterminado")
        body_text = body.get('body', "Cuerpo predeterminado")
        recipient = body.get('recipient', "alejofig@hotmail.com")

        if send_email(subject, body_text, recipient):
            return {
                'statusCode': 200,
                'body': f'Correo electrónico enviado con éxito a {recipient}'
            }
        else:
            return {
                'statusCode': 500,
                'body': 'Error al enviar el correo electrónico'
            }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': f'Error al procesar la solicitud: {str(e)}'
        }
