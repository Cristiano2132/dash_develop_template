import os

s3_bucket_name='underberg-datalake-prd'

analytics_params_dict = {
        'database': os.getenv('ANALYTICS_DATABASE'),
        'user': os.getenv('ANALYTICS_USER'),
        'password': os.getenv('ANALYTICS_PASSWORD'),
        'host': os.getenv('ANALYTICS_HOST'),
        'port':  os.getenv('ANALYTICS_PORT')
    }

# Parametros de conexão com Athena
athena_params_dict = {
    's3_staging_dir': os.getenv('ATHENA_S3_STAGING_DIR'),
    'region_name': os.getenv('AWS_DEFAULT_REGION'),
    'access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
    'secret_key_id': os.getenv('AWS_SECRET_ACCESS_KEY')
}

if __name__=='__main__':
    print(analytics_params_dict)
    print(athena_params_dict)