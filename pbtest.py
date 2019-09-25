from bottle import route, run
import os

port = int(os.getenv("PORT"))

@route('/')
def hello():
    return "Hello World!"

run(host='0.0.0.0', port=port, debug=True)
