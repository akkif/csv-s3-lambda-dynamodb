import boto3

s3=boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('csv_demo')

def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    object_key = event["Records"][0]["s3"]["object"]["key"]
    
    object = s3.get_object(Bucket=bucket_name,Key=object_key)
    body = object["Body"].read().decode("utf-8")
    splitted_body = body.split("\n")
    #print(splitted_body)
    for i in splitted_body:
        a = i.split(",")
        #print(a)
        if a[0]=='':
            pass
        else:
            #print(a)
            table.put_item(Item={
            "student_id" :a[0],
            "name" : a[1],
            "age" :int(a[2]),
            "marks_avg" :int(a[3])
            })
        
