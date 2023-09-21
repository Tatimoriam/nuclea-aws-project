import io
import boto3


def lambda_handler(event, context):
    # pega o bucket e a key do evento trigger
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # lê o objeto e conta as palavras
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, key)
    text = obj.get()['Body'].read().decode('utf-8')

    texto_evento = "Um novo arquivo foi enviado para o bucket!\n" \
                   "Bucket: {}\n" \
                   "Arquivo: {}\n\n" \
                   "Texto:\n" \
                   "\"{}\"".format(bucket, key, text)

    # envia mensagem para o SNS replicar
    client = boto3.client('sns')
    response = client.publish(
        TopicArn="[arn:aws:sns]",
        Subject="[AWS Lambda] Um novo arquivo foi enviado para o S3",
        Message=texto_evento,
        MessageStructure='string',
    )