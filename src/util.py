from bottle import route, get, post, static_file

# Retrieve static files
@get('/static/<path:path>')
def static_callback(path):
  return static_file(path,root='/var/www/html/static/')

#Return 401 error
def error401():
  return "Sorry, access is denied. Please log in on the home page"