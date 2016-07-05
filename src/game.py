from bottle import route, response, request, get, post, TEMPLATE_PATH, template, static_file, redirect, abort
import redis
import uuid

red = redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
TEMPLATE_PATH.insert(0,'/var/www/html/templates')

@get('/game/new')
def newGame():
    new_hash = uuid.uuid4()
    red.hset('sfb:game:' + str(new_hash), 'init', 1)
    red.lpush('sfb:game:list', str(new_hash))
    return str(new_hash)

@get('/game/<hash>')
def viewGame(hash):
    if red.hget('sfb:game:' + hash, 'init'):
        return "Game: " + hash
    return "This game does not exist"
