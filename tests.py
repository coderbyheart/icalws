from webtest import TestApp
import icalws

def test_nth_weekday_in_month():
    app = TestApp(icalws.icalws_app)
    
    # WMFRA-Example
    r = app.get('/nextdates', {"dtstart": "20130114T183000Z", "rrule": "FREQ=MONTHLY;UNTIL=20131209T183000Z;BYDAY=2MO"})
    assert r.status == '200 OK'
    assert r.content_type == 'application/json'
    assert len(r.json["dates"]) == 12
    expected_dates = [
        "20130114T183000Z", 
        "20130211T183000Z", 
        "20130311T183000Z", 
        "20130408T183000Z", 
        "20130513T183000Z", 
        "20130610T183000Z", 
        "20130708T183000Z", 
        "20130812T183000Z", 
        "20130909T183000Z", 
        "20131014T183000Z", 
        "20131111T183000Z", 
        "20131209T183000Z"]
    assert r.json["dates"] == expected_dates

def test_weekly():
    app = TestApp(icalws.icalws_app)
    
    r = app.get('/nextdates', {"dtstart": "20121025T131500Z", "rrule": "FREQ=WEEKLY;UNTIL=20121108T131500Z;BYDAY=TH"})
    assert r.status == '200 OK'
    assert r.content_type == 'application/json'
    assert len(r.json["dates"]) == 3
    expected_dates = [
        "20121025T131500Z",
        "20121101T131500Z",
        "20121108T131500Z",
    ] 
    assert r.json["dates"] == expected_dates

def test_daily():
    app = TestApp(icalws.icalws_app)
    
    r = app.get('/nextdates', {"dtstart": "20121206T110000Z", "rrule": "FREQ=DAILY;COUNT=3"})
    assert r.status == '200 OK'
    assert r.content_type == 'application/json'
    assert len(r.json["dates"]) == 3
    expected_dates = [
        "20121206T110000Z",
        "20121207T110000Z",
        "20121208T110000Z",
    ] 
    assert r.json["dates"] == expected_dates