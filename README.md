# cryd
Cry detection in python

## TODO
* set and count detected cries based on a per minute threshold for alerting
* alert with SMS via Twilio https://www.twilio.com/sms/pricing/us

## Dependencies 
1. brew install aubio
1. brew install portaudio
1. pip install pyaudio
1. pip install aubio
## Usage
`python cryd.py`

Outputs frequency, amplitude, and a cry message if cryd thinks there's a cry happening

