import requests
import json
import sys

import logging
import datetime

now = datetime.datetime.now()
logging.basicConfig(filename='ubinty.log',level=logging.DEBUG)
logging.debug("Ubinty started" + str(now))
logging.debug("Parameter 1: " + sys.argv[1])
logging.debug("Parameter 2: " + sys.argv[2])

# MODIFY 
UNIFI_SERVER="controller.domain.tld" # your IP or FQDN of your NVR
UNIFI_ADMIN_APIKEY="xx-your-api-key-xx" # this API key you find in the settings of your NVR

# insert the name of your camera and its ID here
# to find this id: enable RTSP in your NVR Settings page, save that setting and return to your camera overview
# now when you select a camera you see a new option "RTSP Service", where the RTSP URL is being displayed like rtsp://192.168.178.100:7447/5a71234567891_0 where 5a71234567891 is the ID you are looking for
CAM_DICT={'camera1': '5a71234567891', 'camera2': '5a71234567892'}


# program
CAMERA_NAME=sys.argv[1]
CAMERA_ACTION=sys.argv[2]

url = 'https://' + UNIFI_SERVER + ':7443/api/2.0/camera/' + CAM_DICT[CAMERA_NAME] + '?apiKey=' + UNIFI_ADMIN_APIKEY
payload = {'name': CAMERA_NAME,'recordingSettings': {'motionRecordEnabled': CAMERA_ACTION, 'fullTimeRecordEnabled': False, 'channel': '0'}}
headers = {'content-type': 'application/json'}
response = requests.put(url, data=json.dumps(payload), headers=headers)
logging.debug(response)
print(response)
