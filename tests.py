from webtest import TestApp
import icalws

def test_functional_login_logout():
    app = TestApp(icalws.app)

    app.post('/login', {'user': 'foo', 'pass': 'bar'}) # log in and get a cookie

    assert app.get('/admin').status == '200 OK'        # fetch a page successfully

    app.get('/logout')                                 # log out
    app.reset()                                        # drop the cookie

    # fetch the same page, unsuccessfully
    assert app.get('/admin').status == '401 Unauthorized'
