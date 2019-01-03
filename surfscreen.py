
# python 3

import urllib.request
import datetime, pytz
import os
from time import sleep


#dir = "/home/pi/GrabbySurf/" # for raspberry pi
dir = "/root/GrabbySurf/"
url_root = "http://www.transport.wa.gov.au/imarine/coastaldata/coastcam/archivegfx/"
cams = ["camswan/", "camtrigg1/", "camlancelin/", "camgeraldton/"]


def get_datetime():	# returns time in the format "0000"
	tz = pytz.timezone('Australia/West')
	now = datetime.datetime.now(tz=tz) - datetime.timedelta(minutes = 5)
	time = str(now.hour).zfill(2) + str(now.minute).zfill(2)
	date = str(now.year)[-2:] + str(now.month).zfill(2) + str(now.day).zfill(2)
	return {"date":date, "time":time}


def get_pics(dt): 
	print(dt["time"]) # print the time
	getfile = dt["time"] + ".jpg"
	savefile = dt["date"] + dt["time"] + ".jpg"
	for cam in cams:
		print(dir + cam + dt["date"])
		if not os.path.exists(dir + cam + dt["date"]):
			os.mkdir(dir + cam + dt["date"])
		urllib.request.urlretrieve(url_root + cam + getfile, dir + cam + dt["date"] + "/" +  savefile)


while True:
	dt = get_datetime()
	try:
		if int(dt["time"][:2]) > 3 and int(dt["time"][:2]) < 22:  # get between 4am and 9pm
			get_pics(dt)
			sleep(55)
		else:
			print("Sleeping") 
			sleep(55)
	except (urllib.error.URLError):
		print("URLError")
	except (OSError):
		print("OSError")

# filecmp to compare files, delete if identical and get missing image
