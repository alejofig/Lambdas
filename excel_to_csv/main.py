import pandas as pd
import io
import boto3

def lambda_handler(event, context):
    json_file_name = event['Records'][0]['s3']['object']['key']
    
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    
    s3_client = boto3.client('s3')
    json_object = s3_client.get_object(Bucket=s3_bucket, Key=json_file_name)
    
    json_data = json_object['Body'].read().decode('utf-8')

    json_df = pd.read_json(json_data)

    csv_data = json_df.to_csv(index=False)

    csv_file_name = json_file_name.split('/')[-1].replace('.json', '.csv')

    s3_client.put_object(Bucket=s3_bucket, Key='csv/'+csv_file_name, Body=csv_data)

    return {
        'statusCode': 200,
        'body': f'Archivo CSV {csv_file_name} generado con éxito.'
    }
