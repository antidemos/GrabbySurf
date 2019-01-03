

# python 3

import urllib.request
import datetime, pytz
from time import sleep


#dir = "/home/pi/GrabbySurf/" # for raspberry pi
dir = "/root/GrabbySurf/"
url_root = "http://www.transport.wa.gov.au/imarine/coastaldata/coastcam/archivegfx/"

def get_datetime():	# returns time in the format "0000"
	tz = pytz.timezone('Australia/West')
	now = datetime.datetime.now(tz=tz) - datetime.timedelta(minutes = 5)
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
	try:
		if int(get_datetime()[1][:2]) > 3 and int(get_datetime()[1][:2]) < 21:  # get between 4am and 9pm
			get_pics()
			sleep(55)
		else:
			print("Sleeping") 
			sleep(55)
	except (urllib.error.URLError):
		print("URLError")
	except (OSError):
		print("OSError")
		pass

# filecmp to compare files, delete if identical and get missing image
