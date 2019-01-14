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

How to use this program:
"python ubinty.py camera1 false" to disable recording
"python ubinty.py camera1 true" to enable recording

Ideas to implement:
- not only to change motion on and off, but also enable permanent recording
