import urllib
from datetime import datetime

dir = "/home/pi/GrabbySurf/"
#print('here we go')

def get_time():	# returns time in the format "0000"
	now=datetime.now()
	print(now.hour)

	if now.minute-1 < 10:
		time = str(now.hour) + "0" + str(now.minute-1)
	else:
		time = str(now.hour)+str(now.minute-1)
	return time
#
print(get_time())

#def cam_get(str cam_swan)
#filename=get_time()
#urllib.urlretrieve("http://www.transport.wa.gov.au/imarine/coastaldata/coastcam/archivegfx/camswan/"+filename+".jpg", dir+"cam_swan/"+filename+".jpg")

