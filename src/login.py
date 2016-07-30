from bottle import route, response, request, get, post, TEMPLATE_PATH, template, static_file, redirect, abort
import redis
from passlib.hash import bcrypt
import uuid
from src import user

red = redis.StrictRedis(host='redis_01',port=6379,db=0)
TEMPLATE_PATH.insert(0,'/var/www/html/templates')

@get('/')
def index():
  if user.checkIfLoggedIn():
    redirect('/lobby')
  return template('login')

@post('/login')
def login_callback():
  username = request.forms.get('username')
  password = request.forms.get('password')
  return user.login(username,password)

@post('/signup')
def signup_callback():
  username = request.forms.get('username')
  password = request.forms.get('password')
  return user.signup(username,password)
