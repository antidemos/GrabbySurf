# python 3

import urllib.request
from datetime import datetime, timedelta
import sched, time

dir = "/home/pi/GrabbySurf/"
url_root = "http://www.transport.wa.gov.au/imarine/coastaldata/coastcam/archivegfx/"

def get_datetime():	# returns time in the format "0000"
	now = datetime.utcnow() + timedelta(hours = 8) - timedelta(minutes = 5)
	time = str(now.hour).zfill(2) + str(now.minute).zfill(2)
	date = str(now.year)[-2:] + str(now.month).zfill(2) + str(now.day).zfill(2)
	return date, time

#def cam_get(str camswan)

s = sched.scheduler(time.time, time.sleep) # instantiate a scheduler

def get_pics(sc): 
	print(get_datetime()[1]) # print the time
	getfile = get_datetime()[1] + ".jpg"
	savefile = get_datetime()[0] + get_datetime()[1] + ".jpg"
	urllib.request.urlretrieve(url_root + "camswan/" + getfile, dir + "camswan/" + savefile)
	s.enter(2, 1, get_pics, (sc,)) # remaining events, schedule a grab every 45s, priority 1

s.enter(1, 1, get_pics, (s,)) # first event
s.run()
