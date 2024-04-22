import boto3
import json

dynamo_db_client = boto3.client(
    service_name = 'dynamodb',
    region_name = 'us-east-1'
)

def create_table(table_name, partitionkey,sortkey, attribute1, attribute2):
    response = dynamo_db_client.create_table(
    AttributeDefinitions = [
        {
            'AttributeName':attribute1,
            'AttributeType':'S'
        },
        {
            'AttributeName':attribute2,
            'AttributeType':'S'
        },
    ],
    TableName = table_name,
    KeySchema = [
        {
            'AttributeName':partitionkey,
            'KeyType':'HASH'
        },
        {
            'AttributeName':sortkey,
            'KeyType':'RANGE'
        }
    ],
    BillingMode = 'PROVISIONED',
    ProvisionedThroughput = {
        'ReadCapacityUnits' : 10,
        'WriteCapacityUnits' : 10
    }
    )
    return True
    # print(f"The Table {table_name} has been created in US-East 1 Region successfully")

def put_values(table_name):
    RollNo = ['ABC1234','ADEDVC','DEV1452','DEVESDEC']
    Name = ['Devin','Mark','Raghul','Drake']
    PhoneNo = ['45715487','15487865','4784165','2458751']
    Email = ['devin1@gmail.com', 'markref@gmail.com','raghul@gmail.com','drake142@ymail.com']
    for i in range(len(Name)):
        putstudentvalues = dynamo_db_client.put_item(
            TableName = "StudentDB",
            Item = {
                'RollNo':
                {
                    'S':RollNo[i]
                },
                'Name':
                {
                    'S':Name[i]
                }
            }
        )
        try:
            update_value = dynamo_db_client.update_item(
            TableName = "StudentDB",
            Key = {
                'RollNo': {
                    'S':RollNo[i]
                },
                'Name': {
                    'S':Name[i]
                }
            },
            UpdateExpression = "set Email=:e, PhoneNo=:ph",
            ExpressionAttributeValues = {
                ":e" : {
                    'S':Email[i]
                },
                ":ph" :{
                    'N':PhoneNo[i]
                }
            },
            ReturnValues = "UPDATED_NEW"
        )
        except ClientError as err:
            print(err)
        
    # print(f"The values are added in the table {table_name} successfully")
    return True

def read_values(table_name, rollno, name):
    read_value = dynamo_db_client.get_item(
    TableName = table_name,
    Key = {
        'RollNo': {
            'S':rollno
        },
        'Name': {
            'S':name
        }
    }
    )
    return json.dumps(read_value['Item'], indent = 4)

def update_values(table_name,rollno, Name, email, phoneno):
    update_value = dynamo_db_client.update_item(
        TableName = table_name,
        Key = {
            'RollNo': {
                'S':rollno
            },
            'Name': {
                'S':Name
            }
        },
        UpdateExpression = "set Email=:e, PhoneNo=:ph",
        ExpressionAttributeValues = {
            ":e" : {
                'S':email
            },
            ":ph" :{
                'N':phoneno
            }
        },
        ReturnValues = "UPDATED_NEW"
    )
    return True
    
def delete_value(table_name,rollno, Name):
    delete = dynamo_db_client.delete_item(
    TableName = table_name,
    Key = {
        'RollNo': {
            'S':rollno
        },
        'Name': {
            'S':Name
        }
    }
    )
    return True

def lambda_handler(event, context):
    
    task = json.loads(event.get("body")).get("input").get("task")
    if task == "create":
        table_name = json.loads(event.get("body")).get("input").get("table_name")
        partitionkey = json.loads(event.get("body")).get("input").get("partition_key")
        sortkey = json.loads(event.get("body")).get("input").get("sort_key")
        att1 = partitionkey
        att2 = sortkey
        if create_table(table_name, partitionkey, sortkey, att1, att2):
            response_text = f'{table_name} has been created in region us-east-1 successfully'
            return {
                'statusCode': 200,
                'body': json.dumps(response_text)
            }
            
    elif task == "putvalues":
        table_name = json.loads(event.get("body")).get("input").get("table_name")
        if put_values(table_name):
            response_text = f'The values are added in the table {table_name} successfully'
            return {
                'statusCode':200,
                'body':json.dumps(response_text)
            }
            
    elif task == "readvalues":
        table_name = json.loads(event.get("body")).get("input").get("table_name")
        rollno = json.loads(event.get("body")).get("input").get("rollno")
        name = json.loads(event.get("body")).get("input").get("name")
        response_text = read_values(table_name, rollno, name)
        return {
            'statusCode':200,
            'body': response_text
        }
        
    elif task == "updatevalues":
        table_name = json.loads(event.get("body")).get("input").get("table_name")
        rollno = json.loads(event.get("body")).get("input").get("rollno")
        name = json.loads(event.get("body")).get("input").get("name")
        email = json.loads(event.get("body")).get("input").get("email")
        phoneno = json.loads(event.get("body")).get("input").get("phoneno")
        if update_values(table_name, rollno, name, email, phoneno):
            response_text = read_values(table_name, rollno, name)
            return {
                'statusCode':200,
                'body': response_text
            }
    
    elif task == "deletevalues":
        table_name = json.loads(event.get("body")).get("input").get("table_name")
        rollno = json.loads(event.get("body")).get("input").get("rollno")
        name = json.loads(event.get("body")).get("input").get("name")
        if delete_value(table_name, rollno, name):
            response_text = f'The values are deleted in the table {table_name} successfully'
            return {
                'statusCode':200,
                'body': json.dumps(response_text)
            }
