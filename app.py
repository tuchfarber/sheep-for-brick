from bottle import route, run, template
import redis

from src import user, lobby, login, util, game

if __name__ == "__main__":
  run(host='0.0.0.0',port=80,debug=True,reloader=True)
