# Webservice exposing python-dateutil

I implemented this webservice to have a way to calculate repeating dates with the complex 
ruleset present in [RFC 5545](https://tools.ietf.org/html/rfc5545) in other programming 
environments.

[Python dateutil](http://labix.org/python-dateutil) is the only free implementation of 
these rules. If you look at [it's source](https://github.com/paxan/python-dateutil/blob/patches-for-1.5/dateutil/rrule.py#L229), 
you'll know why.

## Installation

See [INSTALL](INSTALL)

## Usage

See [tests.py](tests.py)

## Public Webservice

You'll find a public instance of this webservice at: http://icalws.coderbyheart.de/nextdates
