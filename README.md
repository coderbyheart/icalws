# Webservice exposing python-dateutil

I implemented this webservice to have a way to calculate repeating dates with the complex ruleset present in [RFC 5545](https://tools.ietf.org/html/rfc5545).

[Python dateutil](http://labix.org/python-dateutil) is the only free implementation of theses rules.

If you look at [it's source](https://github.com/paxan/python-dateutil/blob/patches-for-1.5/dateutil/rrule.py#L229), you'll know why.

## Usage

See [tests.py](tests.py)

## Installation

See INSTALL

## Public Webservice

You'll find a public instance of this webservice at: http://icalws.coderbyheart.de/nextdates
