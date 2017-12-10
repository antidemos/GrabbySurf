# python 3

import urllib.request
from datetime import datetime, timedelta
from time import sleep

dir = "/home/pi/GrabbySurf/"
url_root = "http://www.transport.wa.gov.au/imarine/coastaldata/coastcam/archivegfx/"

def get_datetime():	# returns time in the format "0000"
	now = datetime.utcnow() + timedelta(hours = 8) - timedelta(minutes = 5)
	time = str(now.hour).zfill(2) + str(now.minute).zfill(2)
	date = str(now.year)[-2:] + str(now.month).zfill(2) + str(now.day).zfill(2)
	return date, time

def get_pics(): 
	print(get_datetime()[1]) # print the time
	getfile = get_datetime()[1] + ".jpg"
	savefile = get_datetime()[0] + get_datetime()[1] + ".jpg"
	urllib.request.urlretrieve(url_root + "camswan/" + getfile, dir + "camswan/" + savefile)
	urllib.request.urlretrieve(url_root + "camtrigg1/" + getfile, dir + "camtrigg1/" + savefile)
	urllib.request.urlretrieve(url_root + "camlancelin/" +  getfile, dir + "camlancelin/" + savefile)
	urllib.request.urlretrieve(url_root + "camgeraldton/" + getfile, dir + "camgeraldton/" + savefile)

while True:
	if int(get_datetime()[1][:2]) > 3 and int(get_datetime()[1][:2]) < 21:  # get between 4am and 9pm
		get_pics()
		sleep(55)
	else:
		print("Sleeping") 
		sleep(55)

# filecmp to compare files, delete if identical and get missing image
