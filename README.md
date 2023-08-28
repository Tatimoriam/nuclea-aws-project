# nuclea-aws-project

Projeto desenvolvimento para o módulo de AWS Cloud do curso
oferecido pela [Ada Tech](https://www.linkedin.com/school/adatechbr/) 
em parceria com a [Núclea](https://www.linkedin.com/company/nucleabr/).

## Participantes

- [Fernanda Gabbai](https://github.com/fergabbai)
- [Michelle Lira](https://github.com/michelle-lira)
- [Andreza Pipolo](https://github.com/andrezapipolo)
- [Tatiane Paiva](https://github.com/Tatimoriam)


## A Proposta

A proposta deste projeto era criar uma forma de automatizar a 
subida de relatórios, garantido resiliência, segurança e 
alta disponibilidade.

Essa foi a solução proposta por este grupo.

## O Projeto
![Diagrama da arquitetura](https://github.com/michelle-lira/nuclea-aws-project/blob/main/img/arquitetura-projeto-cloud-aws.png)

Chegamos na ideia de subir esse relatório para a S3 utilizando
Lambda para rodar nossos script.

O fluxo do projeto se dá conforme diagrama a cima:
> Às 12:00 GMT+3 um evento será disparado pelo CloudWatch Event para a 
> função lambda chamada **projeto-lambda-nuclea**.
> Esta função então irá fazer uma requisição utilizando a biblioteca **yfinance**
> para gerar um relatório com os dados solicitados e subir esse relatório para o bucket 
> **projeto-bucket-nuclea**.
> 
> Essa alteração no bucket irá ser o gatilho para a execução da função Lambda **projeto-lbaviso-nuclea**
> que irá consultar o arquivo que foi inserido e enviá-lo para os e-mails cadastrados
> na fila SNS que está conectada como destino a esta função.
