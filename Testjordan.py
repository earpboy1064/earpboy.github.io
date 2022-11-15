#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

import cgi   

form = cgi.FieldStorage()   
# html form inputs are simple key value pairs - 
#in php they are associative arrays
#in ruby they are hashes
# and in python dictionaries
# keys are form elements' name (in our example 'textinput')
# values are user inputs
input_text = form.getfirst("textinput", "0") # 0 is optional - if no 
#values entered automatically set it to "0". same as
#>>> x = {2:"a"}
#>>> x.get(2, "nonexistent")
#'a'
#>>> x.get(3, "nonexistent")
#'nonexistent'
#have a look up this -http://www.tutorialspoint.com/python/dictionary_get.htm
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<body>")
#print "<p>%s</p>" % form  #uncomment this line if you want 
#to see what does form hashes look like 
print ("<p>%s</p>" % input_text)
print ("</body>")
print ("</html>")