import numpy as np
import pylab as pyl
import math

pi2 = math.pi * 2

freq=440 
amp=0.7
offset=0.0
duration= 0.5
framerate=50
start=0.0
n = round(duration * framerate)
ts = start + np.arange(n) / framerate
phases = pi2 * freq * ts + offset
ys = amp * np.sin(phases)
hs = np.fft.fft(ys)

pyl . plot (ts ,ys)
pyl . plot (hs ,ys)
pyl . show ( )