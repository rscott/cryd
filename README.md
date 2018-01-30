# cryd
Cry detection in python

## TODO
* set and count detected cries based on a per minute threshold for alerting
* alert with SMS via Twilio https://www.twilio.com/sms/pricing/us

## Dependencies 
aubio, numpy, pyaudio

## Usage
`python cryd.py`

Outputs frequency, amplitude, and a cry message if cryd thinks there's a cry happening

