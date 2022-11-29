#!/usr/bin/python3.6
#-*- coding: UTF-8 -*-
# enable debugging

import boto3
import cgitb
import cgi
import os
import shutil  




#********************************************************************************************** CGI
cgitb.enable()

print ("Content-type:text/html\r\n\r\n")

form = cgi.FieldStorage()   
name = form.getfirst("name", "0") # 0 is optional - if no  # gets info from html file 
Student_Number = form.getfirst("Student_Number", "0") # gets info from html file 
email = form.getfirst("email", "0")# gets info from html file 
fileitem = form['fileToUpload'] # gets info from html file 



if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('files/' + fn, 'wb').write(fileitem.file.read())
    message = 'Your application was uploaded successfully'

else:
    message = 'No file was uploaded'


#################################################################################  s3
errormessage = 'no error'
try:
    file = open("files/"+fn, 'rb')
except IOError:
    errormessage = 'error could not open'

s3 = boto3.client('s3',region_name='us-east-2') #connects to s3
s3.upload_fileobj(file, "wyatt-in", '('+Student_Number+')'+fn)  #transfers the file to s3


########################################################################################  Database



dynamodb = boto3.resource('dynamodb',region_name='us-east-2') # connects to dynamoDB

#this is the table name
table = dynamodb.Table('Applications')


#this puts the item in the table
table.put_item(
   Item={
        'Snumber': Student_Number,
	'Name': name,
	'Email': email,
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





#########################################################################################

print ("<html>")
print ("<body>")
print ("<p>%s</p>" % message)
print ("</body>")
print ("</html>")




