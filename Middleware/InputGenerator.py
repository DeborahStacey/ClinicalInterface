#!c:/Python34/python
import random
from time import *
from string import *

def randCode():
	return (''.join(random.choice(ascii_uppercase + digits) for _ in range(12)))

def randString(values):
	return random.choice(values)

def randDateTime(start, end, dateformat):
	startDate = mktime(strptime(start, dateformat))
	endDate = mktime(strptime(end, dateformat))
	randDate = startDate + random.random() * (endDate - startDate)
	return strftime(dateformat, localtime(randDate))