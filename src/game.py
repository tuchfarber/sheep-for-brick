from bottle import route, response, request, get, post, TEMPLATE_PATH, template, static_file, redirect, abort
import redis
import uuid
from src import util, user

red = redis.StrictRedis(host='redis_01',port=6379,db=0)
TEMPLATE_PATH.insert(0,'/var/www/html/templates')

@get('/game/new')
def newGame():
    new_hash = uuid.uuid4()
    red.hset('sfb:game:' + str(new_hash), 'init', 1)
    red.lpush('sfb:game:list', str(new_hash))
    return str(new_hash)

@get('/game/<hash>')
def viewGame(hash):
    cur_user = user.checkIfLoggedIn()
    cur_players = red.hget('sfb:game:' + hash,'players')
    if cur_players == None or len(cur_players) < 4:
        red.lpush('sfb:game:' + hash + ':players',cur_user)
    else:
        return "Game is at maximum capacity"
    if cur_user:
        if red.hget('sfb:game:' + hash, 'init'):
            num_players = red.lrange('sfb:game:' + hash + ':players',0,-1)
            return template('game',hash=hash,user=cur_user,num_players=num_players)
        return "This game does not exist"
    abort(401,util.error401())
