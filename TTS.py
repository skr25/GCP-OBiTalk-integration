import requests
import urllib
#This requires DLNA Media controller plugin installed on Vera. You can substitute langauage and engine to US-en and GOOGLE/MICROSOFT/MARYTTS
#Replace XXX.XXX.XXX.XXX with local IP of Vera Hub
def Notify(pSpeaker,pVolume,pText):

	varText = urllib.parse.quote_plus(pText)
	url = "http://192.168.1.50/port_3480/data_request?id=lu_action&output_format=xml&DeviceNum="+str(pSpeaker)+"&serviceId=urn:dlna-org:serviceId:DLNAMediaController1&action=Say&Text="+varText+"&Language=en-US&Engine=GOOGLE&Volume="+str(pVolume)
	print(url)
	r = requests.get(url, verify=False)
	return r.status_code


