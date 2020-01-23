#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os
from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie
#q1-3
#print("Content-Type: text/html\n")
#print()
#print("<!doctype html><title>Hello</title><h2>Hello World</h2>")


#q4-7
print("Content-Type: text/html")

#q1
#print(os.environ)

#q2
#print(os.environ["QUERY_STRING"])

#q3
#print(os.environ["HTTP_USER_AGENT"])

#q4

print(login_page())

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")
