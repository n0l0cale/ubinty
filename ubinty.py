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

# LOADING CONFIG.JSON
with open('config.json') as json_data_file:
    data = json.load(json_data_file)

CAMERA_NAME=sys.argv[1]
CAMERA_RECTYPE=sys.argv[2]

cameraFound=0

if CAMERA_RECTYPE != "motion" and CAMERA_RECTYPE != "full" and CAMERA_RECTYPE != "none":
    print "unkown rectype - must be motion, full or none"
    sys.exit(0)

for i in data["cameras"]:
    if i['name'] == CAMERA_NAME:
        url = 'https://' + data['unifiserver'] + ':7443/api/2.0/camera/' + i['id'] + '?apiKey=' + data['unifiadminkey']
        if CAMERA_RECTYPE == "motion":
            payload = {'name': CAMERA_NAME,'recordingSettings': {'motionRecordEnabled': True, 'fullTimeRecordEnabled': False, 'channel': '0'}}
        if CAMERA_RECTYPE == "full":
            payload = {'name': CAMERA_NAME,'recordingSettings': {'motionRecordEnabled': False, 'fullTimeRecordEnabled': True, 'channel': '0'}}
        if CAMERA_RECTYPE == "none":
            payload = {'name': CAMERA_NAME,'recordingSettings': {'motionRecordEnabled': False, 'fullTimeRecordEnabled': False, 'channel': '0'}}
        headers = {'content-type': 'application/json'}
        response = requests.put(url, data=json.dumps(payload), headers=headers)
        logging.debug(response)
        print(response)
        cameraFound=1
        break

if cameraFound is 0:
    print "FATAL: camera-id (first parameter) could not be found"
