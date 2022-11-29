#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

import cgo
content='''<html><body>
<h3>Name: {strname} </h3>
<h3>Password: {strpwd} </h3>
</body><html>'''

def main() : 
    form = cgi.FieldStorage()
    strname = form.getfirst("sname","")
    strpwd = form.getfirst("pwd","")
    print(content.format(**locals()))

try:
    main()
except:
    cgi.print_exception()