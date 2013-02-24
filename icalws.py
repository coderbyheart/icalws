from bottle import route, run, Bottle
from dateutil.rrule import *

app = Bottle()

@app.route('/nextdates')
def nextdates():
    return "Hello World!"

if __name__ == "__main__":
	run(host='localhost', port=8080, debug=True)
