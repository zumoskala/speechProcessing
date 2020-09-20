import wave
import numpy as np
import matplotlib.pyplot as plt

# Create audio file wave object
good_morning = wave.open('sound\hello.wav')

# Read all frames from wave object
signal_gm = good_morning.readframes(-1)

# View first 10
print(signal_gm[:10])

# Convert good morning audio bytes to integers
soundwave_gm = np.frombuffer(signal_gm, dtype='int16')

# if we don't know the frequency of our file, we can divide the length of the wave object array by the duration
# of the sound wave in seconds OR (in Python) call getframerate on a wave object
framerate_gm = good_morning.getframerate()
print(framerate_gm)

# to get file's duration
frames = good_morning.getnframes()
rate = good_morning.getframerate()
duration = frames / float(rate)
print(duration)

# get timestamps of each integer (each sample) to later visualise it
time_gm = np.linspace(start=0,
                      stop=len(soundwave_gm)/framerate_gm,
                      num=len(soundwave_gm))

# prepare another recording to compare it to good_morning
good_afternoon = wave.open('sound\evening_hello.wav')
signal_ga = good_afternoon.readframes(-1)
soundwave_ga = np.frombuffer(signal_ga, dtype='int16')
framerate_ga = good_afternoon.getframerate()
time_ga = np.linspace(start=0,
                      stop=len(soundwave_ga)/framerate_ga,
                      num=len(soundwave_ga))

# Visualisation
# Setup the title and axis titles
plt.title('Good Afternoon vs. Good Morning')
plt.ylabel('Amplitude')
plt.xlabel('Time (seconds)')

# Add the Good Afternoon data to the plot
plt.plot(time_ga, soundwave_ga, label='Good Afternoon')

# Add the Good Morning data to the plot
plt.plot(time_gm, soundwave_gm, label='Good Morning',
         # Set the alpha variable to 0.5
         alpha=0.5)

plt.legend()
plt.show()
# amplitude = 0 -> no sound at all
