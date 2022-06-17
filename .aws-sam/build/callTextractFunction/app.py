import boto3
from trp import Document
import json
import uuid

#function that returns all items in KV pairs
def get_all(doc):
        kvs = {}
        for page in doc.pages:
            kvs = []
            for field in page.form.fields:
                print("{},{}".format(field.key, field.value))
                #kvs["{}".format(field.key)] = "{}".format(field.value)
                kvs.append({"{}:{}".format(field.key, field.value)})
        return kvs

#function that retruns single item
def get_item(key, doc):
    get_kv = []
    for page in doc.pages:
        print("\nSearch Fields:")
        fields = page.form.searchFieldsByKey(key)
        for field in fields:
            print("{}","{}".format(field.key, field.value))
            get_kv = {}
            #get_kv = "{}","{}".format(field.key, field.value)
            get_kv.append({field.key:field.value})
    return get_kv

#function to write recrod to DynamoDB Table
def add_item(items):
    table_name = 'serverless-hack-a-thon'
    region = 'us-east-1'
    
    table = boto3.resource(
        'dynamodb',
        region_name=region
    )
    table = table.Table(table_name)
    
    print("Hey, I got this as items: ",items)

    for item in items :
        print("printed item-->",item)

        skid = str(uuid.uuid4())
        params = {
            'pk':skid,
            'id': item
        }
        print("params",params)
    
    response = table.put_item(
        TableName=table_name,
        Item=params
    )
    print(response)

    params['msg']='Item Created'

    print('Returning response: ', json.dumps(params))
    return "DynamoDB "

def lambda_handler(event, context):  
    #Let's set what file and bucket to store image of license
    s3BucketName = "bling-textract-demo"
    documentName = "washington-drivers-license.jpeg"
    fileLocation = '/tmp/' + documentName
    
    # Amazon Textract client setup
    textract = boto3.client('textract')
    
    #Setup the S3 client and retrieve the file
    s3 = boto3.client('s3')
    s3.download_file(s3BucketName, documentName, fileLocation)
    
   
    
    # Call Amazon Textract
    with open(fileLocation, "rb") as document:
        response = textract.analyze_document(
            Document={
                'Bytes': document.read(),
            },
            FeatureTypes=["FORMS"])
    
    #Create a variable for the document
    doc = Document(response)
    
    all_kvs = get_all(doc)
    single_kvs = get_item('4d', doc)
    print("get specfic item: 4d  ",single_kvs)
    print("get all items:  ",all_kvs)
    add_item(all_kvs)
    
    return {
        'statusCode': 200,
        'body': json.dumps("success")
    }
