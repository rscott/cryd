import aubio
import collections
import numpy as num
import pyaudio

# PyAudio object.
p = pyaudio.PyAudio()

seconds = .5
#gonna need a circular buffer to calculate averages. There's prob a better way, but I understand this
buffer = collections.deque(maxlen=43*seconds)

# Open stream.
stream = p.open(format=pyaudio.paFloat32,
    channels=1, rate=44100, input=True,
    frames_per_buffer=1024)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", 2048,
    2048//2, 44100)
# Set unit.
pDetection.set_unit("Hz")
pDetection.set_silence(-40)

while True:

    data = stream.read(1024)
    samples = num.fromstring(data,
        dtype=aubio.float_type)
    pitch = pDetection(samples)[0]
    # Compute the energy (volume) of the
    # current frame.
    volume = num.sum(samples**2)/len(samples)
    # Format the volume output so that at most
    # it has six decimal numbers.
    volume = "{:.6f}".format(volume)

    #print(chr(27) + "[2J") #clear screen like a hacker 
    print(pitch)
    print(volume)
    

    # midpass filter crying frequencies into the buffer
    # freq range from http://research.ijcaonline.org/iceice/number3/iceice022.pdf
    
    if 300 <= pitch <= 650:
        buffer.append(pitch)
    else:
        buffer.append(0)
    avg_pitch = sum(buffer) / len(buffer)

    #print if buffer is mainly a cry
    if 300 <= avg_pitch <= 650:
        print("Cry detected")

    

