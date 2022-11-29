#!/usr/bin/python3.6
#-*- coding: UTF-8 -*-
# enable debugging

import boto3
import cgitb
import cgi   


#********************************************************************************************** CGI
cgitb.enable()

form = cgi.FieldStorage()   
# html form inputs are simple key value pairs - 
#in php they are associative arrays
#in ruby they are hashes
# and in python dictionaries
# keys are form elements' name (in our example 'textinput')
# values are user inputs
input_text = form.getfirst("textinput", "0") # 0 is optional - if no 
#values entered automatically set it to "0". same as
Student_Number = form.getfirst("Student_Number", "0")
#>>> x = {2:"a"}
#>>> x.get(2, "nonexistent")
#'a'
#>>> x.get(3, "nonexistent")
#'nonexistent'
#have a look up this -http://www.tutorialspoint.com/python/dictionary_get.htm
#**********************************************************************************************


########################################################################################  Database
region_name='us-east-1',
aws_access_key_id='AKIAWA3VERQCVBU3QCH3',
aws_secret_access_key='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'



dynamodb = boto3.resource('dynamodb',region_name='us-east-2')

#this is the table name
table = dynamodb.Table('Applications')


#this puts the item in the table
table.put_item(
   Item={
        'Snumber': Student_Number,
	'Name': input_text
        
    }
)

#pulls data back off the table to show that you can search using just the
#primary key that is the student number
response = table.get_item(
    Key={
        'Snumber': Student_Number
            }
)


item = response['Item']  # item from database
#print(item)

#################################################################################

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<body>")
#print "<p>%s</p>" % form  #uncomment this line if you want 
#to see what does form hashes look like 
print ("<p>%s</p>" % item)
#print ("<p>%s</p>" % item.Name)
print ("</body>")
print ("</html>")

#print("Content-Type: text/plain;charset=utf-8")
print(Student_Number)
print("Hello World!")



