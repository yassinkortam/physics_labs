
import pandas as pd

expected_peaks = 4
sample_maxima = 17


raw_data = pd.read_csv('hydrogen.csv')
i = [i for i in raw_data['Latest: Intensity (rel)']]
l = [i for i in raw_data['Latest: Wavelength (nm)']]

wavelengths_of_peaks = []

counter = 0

for k in range(sample_maxima):
    max_intensity = max(i)
    max_intensity_index = i.index(max_intensity)
    wavelength_of_peak = l[max_intensity_index]

    wavelengths_of_peaks.append(wavelength_of_peak)
    i.remove(max_intensity) 

wavelengths_of_peaks.sort()

def remove_repeats(dataset, variance):
    for k in range(len(dataset)-1):
        if k>0 and k < len(dataset):
            thisvariance = 100*abs((dataset[k]-dataset[k-1])/dataset[k])
            if thisvariance < variance:
                dataset.remove(dataset[k])
    return dataset

variance = 0
while len(wavelengths_of_peaks) > expected_peaks:
    remove_repeats(wavelengths_of_peaks, variance)
    variance += 1
print(wavelengths_of_peaks)
