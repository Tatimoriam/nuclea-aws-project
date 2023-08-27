import boto3
import yfinance as yf
from datetime import datetime


def lambda_handler(event, context):
    # Dados do arquivo
    local_arquivo = "/tmp/local_arquivo.txt"
    nome_arquivo = "relatorio_" + str(datetime.now().strftime("%Y_%m_%d")) + ".txt"
    nome_bucket = "projeto-bucket-nuclea"

    tickers = ['ITSA4.SA', 'PETR4.SA']

    # Criar arquivo
    try:
        for ticker in tickers:
            acao = yf.download(ticker, progress=False)

            with open(local_arquivo, 'a') as arquivo:
                arquivo.write("Relatorio da acao: " + ticker + "\n")
                arquivo.write(str(acao.tail()))
                arquivo.write("\n-----------------\n")

            arquivo.close()

    except Exception as e:
        return print(f"Erro ao obter dados da ação. Detalhes do erro: {e}")

    # Inserir no bucket
    s3 = boto3.client('s3')
    with open(local_arquivo, "rb") as f:
        s3.upload_fileobj(f, nome_bucket, nome_arquivo)