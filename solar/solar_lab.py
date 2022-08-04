
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

PROMINENCE = 0.09

data = pd.read_csv('solar.csv')
wavelengths = [i for i in data['Remote Data: Wavelength (nm)']]
intensities = [i for i in data['Remote Data: Intensity (rel)']]
x = [-1*i for i in intensities]

peaks, properties = find_peaks(x,prominence=PROMINENCE)
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.set_title("Raw Data with Marked Absorptions")
ax1.set_ylabel("Intensity (rel)")
ax1.set_xlabel("Wavelength (nm)")

plt.plot(intensities)
for i in range(len(peaks)):
    plt.scatter(peaks[i],intensities[peaks[i]],s=60)
    plt.plot(np.zeros_like(intensities), "--", color="gray")
    print(wavelengths[peaks[i]])
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot()
ax1.set_title("Absorption Lines")
ax1.set_xlabel("Wavelength (nm)")
for i in range(len(peaks)):
    plt.axvline(peaks[i])
    
plt.show()



    

