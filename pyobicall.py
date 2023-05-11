import sys
sys.path.insert(0, '/share/CACHEDEV1_DATA/Public/dlna')
sys.path.insert(0, '/share/CACHEDEV1_DATA/Public/googleapis')
import TTS as mytts
import googlepeople as mycontacts
import time
import xml.etree.ElementTree
import requests
from requests.auth import HTTPDigestAuth
import logging
import logging.handlers
logger = logging.getLogger('obicall google api integration')
#hdlr = logging.FileHandler('/share/CACHEDEV1_DATA/Public/mqtt/obihai-logger.log', mode='w')
hdlr = logging.handlers.TimedRotatingFileHandler('/share/CACHEDEV1_DATA/Public/mqtt/obihai-logger.log',when="D",interval=1,backupCount=1)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
url = 'http://192.168.1.180/PI_FXS_1_Stats.xml'
voiceFlag = 0
logger.info("Voice Flag is initialized with 0.")
while(1):
	res = requests.get(url, auth=HTTPDigestAuth('admin', 'admin'))
	logger.info("Made Request to 192.168.1.180")
	e = xml.etree.ElementTree.fromstring(res.text)
	#print(e[0][3][2].attrib.get("current"))
	#print(e[0][7][2].attrib.get("current"))
	ringStatus = e[0][3][2].attrib.get("current")
	rawCallerID = e[0][7][2].attrib.get("current")
	if rawCallerID == "--" :
		rawphone = None
	else:
		rawphone = rawCallerID.split(" ")[1]
	
	#print(rawphone)
	logger.info("Parsed XML and raw phone no received is %s.",rawphone)
	logger.info("Ring status of phone is %s.",ringStatus)
	logger.info("Raw caller id is %s.",rawCallerID)
	
	if ringStatus == "Ringing" :
		if voiceFlag == 0:
			if rawphone is None:
				phone = "Unknown"
				contactName = "Unknown"
				logger.info("Phone is ringing but rawphone is nothing, caller id and caller name is unknown.")
			else:
				phone = rawphone[1:4] + "-" + rawphone[4:7] + "-" + rawphone[7:]
				rawphone= "+" + rawphone
				contactName = mycontacts.getName(rawphone)
				logger.info("Phone is ringing but phone is %s and caller name is %s",phone,contactName)
			voiceFlag = 1
			logger.info("Voice Flag is set to 1.")
			ttstext = "Hello, you have a call on your home phone from caller name  " + contactName + " and  number is " + phone + "."
			mytts.Notify('114','50',ttstext)
			logger.info("TTS is provided to speaker to notify.")

	if ringStatus != "Ringing" :
	     voiceFlag = 0
	     logger.info("Voice Flag is set to 0. and sleep for 7 seconds.")
	time.sleep(7)
