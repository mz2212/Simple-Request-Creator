#I can't be held liable for damages!
#The MIT License (MIT)
#
#Copyright (c) 2016 Mike
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import sqlite3
import http.client
import random
import string
import time

conn = sqlite3.connect('sites.db')
c = conn.cursor()


#Some code to generate a random string. Thanks again, StackOverflow!
#All this is to make this as random as possible, so that a simple filter can't block out the noise.
def randomPage(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars for _ in range (size))

def size(lower=10, upper=30):
	return random.randint(lower, upper)

def waitTime(lower=30, upper=180):
	return random.randint(lower, upper)



try:
	while 1:
		#Get a random server, a source, and decide a page to go to (should result in a 404).
		c.execute('SELECT site FROM sites ORDER BY RANDOM() limit 1')
		site = c.fetchone()
		c.execute('SELECT site FROM sites ORDER BY RANDOM() limit 1')
		source = c.fetchone()
		page = randomPage(size())
		#Establish a connection to the random server, saying that you came from another random server
		connect = http.client.HTTPConnection(data[0], 80, timeout=10, source[0])
		#Request the random page that we generated earlier.
		#Note: This will NOT get any resources from the page, like CSS or images. Just the page (which should be a 404).
		connect.request("GET", page)
		time.sleep(1)
		#Give the server a second before closing the connection.
		connect.close()
		#Sleep for a random time, so that we're not DDOSing (Ehh, with 1,000,000 sites to choose from...).
		time.sleep(waitTime())

except KeyboardInterrupt:
	print("CTRL-C Recieved, Quitting!")

finally:
	connect.close() #Make for sure that connection is closed.
