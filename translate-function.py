import json
import boto3

def lambda_handler(event, context):

    translate = boto3.client('translate')
    input_text = 'JAY SDAYS 2021を楽しんでいますか？'

    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode='ja',
        TargetLanguageCode='en'
    )

    output_text = response['TranslatedText']

    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text': output_text
        })
    }
