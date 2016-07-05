from bottle import route, response, request, get, post, TEMPLATE_PATH, template, static_file, redirect, abort
import redis
from passlib.hash import bcrypt
import uuid

red = redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
TEMPLATE_PATH.insert(0,'/var/www/html/templates')

# Retrieve static files
@get('/static/<path:path>')
def static_callback(path):
  return static_file(path,root='/var/www/html/static/')

#Return 401 error
def error401():
  return "Sorry, access is denied. Please log in on the home page"