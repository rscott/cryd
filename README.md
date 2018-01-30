# cryd
Cry detection in python

## TODO
* set and count detected cries based on a per minute threshold for alerting
* alert with SMS via Twilio https://www.twilio.com/sms/pricing/us

## Dependencies 
brew install aubio
brew install portaudio
pip install pyaudio
pip install aubio
## Usage
`python cryd.py`

Outputs frequency, amplitude, and a cry message if cryd thinks there's a cry happening

