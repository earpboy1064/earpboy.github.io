
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.



#this is the table name
table = dynamodb.Table('Applications')


#puts student information. will be replaced with data from html page
table.put_item(
   Item={
        'Snumber': 'S00336669',
	'Name': 'William LeMaster'
        
    }
)

#pulls data back off the table to show that you can search using just the
#primary key that is the student number
response = table.get_item(
    Key={
        'Snumber': 'S00336669'
            }
)
item = response['Item']
print(item)