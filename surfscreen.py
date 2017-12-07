
# python 3

import urllib.request
from datetime import datetime, timedelta
import sched, time


dir = "/home/pi/GrabbySurf/"
#print('here we go')

def get_time():	# returns time in the format "0000"
	now = datetime.now() + timedelta(hours = 8) - timedelta(minutes = 5)

	if now.hour < 10:
		hr_str = "0" + str(now.hour)
	else:
		hr_str = str(now.hour)

	if now.minute < 10:
		min_str = "0" + str(now.minute)
	else:
		min_str = str(now.minute)

	time = hr_str + min_str
	return time


print(get_time())
#def cam_get(str camswan)

s = sched.scheduler(time.time, time.sleep)

def get_pics(sc): 
	print("Doing stuff...")
	filename = get_time()
	urllib.request.urlretrieve("http://www.transport.wa.gov.au/imarine/coastaldata/coastcam/archivegfx/camswan/"+filename+".jpg", dir+"camswan/"+filename+".jpg")
	s.enter(30, 1, get_pics, (sc,))

s.enter(30, 1, get_pics, (s,))
s.run()
