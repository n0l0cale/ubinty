Ubinty

A small and dirty python script to change the record type of your Ubiquiti cameras to Motion enabled and disabled via commandline executions (useful for example in homeassistant automation implementations)

Installation instructions:
- install python2
- install pip for python2
- install python requirements via pip

For raspbian this means:
```
sudo apt-get install python python-pip -y
pip install -r requirements.txt
```

Adjust the configfile (config.json) to your environment:
Insert the name of your camera and its ID here
to find this id: enable RTSP in your NVR Settings page, save that setting and return to your camera overview
now when you select a camera you see a new option "RTSP Service", where the RTSP URL is being displayed like rtsp://192.168.178.100:7447/5a71234567891_0 where 5a71234567891 is the ID you are looking for

Please use the config.json file as provided in the file repository - not the version below - json is not intended to be commented...
```
{
    "unifiserver": "controller.domain.tld", # your IP or FQDN of your NVR
    "unifiadminkey": "xx-your-api-key-xx", # this API key you find in the settings of your NVR
    "cameras": [
        {
           "name": "camera1", # this is the name of the camera1
           "id": "5a71234567891" # this is the id you have evaluated
        },
        {
            "name": "camera2", # this is the name of the camera2
            "id": "5a71234567892" # this is the id you have evaluated
        }
   ]
}
```

How to use this program:
"python ubinty.py camera1 false" to disable recording
"python ubinty.py camera1 true" to enable recording

Ideas to implement:
- not only to change motion on and off, but also enable permanent recording
