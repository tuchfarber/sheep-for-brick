from bottle import route, response, request, get, post, TEMPLATE_PATH, template, static_file, redirect, abort
import redis
from passlib.hash import bcrypt
import uuid
from src import user, util

red = redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
TEMPLATE_PATH.insert(0,'/var/www/html/templates')

@get('/lobby')
def lobby():
  if user.checkIfLoggedIn():
    return template('lobby')
  abort(401,util.error401())

@get('/allgames')
def allgames():
  games = [i.decode('utf-8') for i in red.lrange('sfb:game:list',0,-1)]
  return {'allgames':games}