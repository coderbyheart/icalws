import site
site.addsitedir('/data/www/icalws.coderbyheart.de/develop/lib/python2.7/site-packages')

import sys, os, bottle

sys.path = ['/data/www/icalws.coderbyheart.de/'] + sys.path
os.chdir(os.path.dirname(__file__))

import icalws # This loads your application

application = icalws.icalws_app
