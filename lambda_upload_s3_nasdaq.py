from datetime import datetime

import requests
import boto3
import os

# Configurações
s3_bucket_name = "projeto-bucket-nuclea"
csv_folder = "/tmp"

# Configurando o cliente S3
s3_client = boto3.client("s3")

# URL do relatório CSV da Nasdaq
nasdaq_csv_url = "https://data.nasdaq.com/api/v3/datasets/FINRA/FNSQ_AMZN.csv"


# Função para baixar o CSV e salvar no S3
def lambda_handler(event, context):
    response = requests.get(nasdaq_csv_url)
    if response.status_code == 200:
        csv_content = response.text

        # Salvar localmente em um arquivo CSV temporário
        csv_filename = "temp_report" + str(datetime.now().strftime("%Y_%m_%d")) + ".csv"
        csv_filepath = os.path.join(csv_folder, csv_filename)

        with open(csv_filepath, "w", newline="") as csvfile:
            csvfile.write(csv_content)

        # Fazer upload para o S3
        s3_client.upload_file(csv_filepath, s3_bucket_name, csv_filename)

        print(f"Arquivo {csv_filename} enviado para o S3.")
    else:
        print("Erro ao baixar o CSV da Nasdaq")
