from bottle import route, request, run, Bottle, abort
from dateutil.rrule import *
from dateutil.parser import parse

icalws_app = Bottle()

@icalws_app.route('/nextdates')
def nextdates():
    if "dtstart" not in request.query:
        abort(400, "Missing dtstart")
    if "rrule" not in request.query:
        abort(400, "Missing rrule")
        
    rdates = list(rrulestr(request.query.rrule, dtstart=parse(request.query.dtstart)))
    res = {
        "dates":[]
    }
    for date in rdates:
        res["dates"].append(date.strftime('%Y%m%dT%H%M%SZ'))
    
    return res

if __name__ == "__main__":
    run(app=icalws_app, host='localhost', port=8080, debug=True, reloader=True)
