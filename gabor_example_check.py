import gabor
from gabor import gabor
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import scipy.ndimage.filters
from scipy.ndimage.filters import convolve as convolve
import scipy.signal
from scipy.signal import argrelmax

data_some_pics = np.memmap('Newer_Image_0001_0001_mean.raw', dtype = 'float64', mode = 'r', shape=(300, 512, 512), order = 'C')
img_in = data_some_pics[1,:,:]
r0=10
sigma=16
f0=1/5
gb = gabor(r0,sigma,f0)
img_out = np.zeros((512,512))
img_out = convolve(img_in, gb, mode='constant', cval=0.0)

#Plots of responses
#for nums in range(1,17):
#plt.plot(img_out[256])
#plt.show()

max_vector = []
b = 0
for row in range(0, 512):
    line = img_out[row, 0:512]
    maxs = argrelmax(line, order=30)
    for i in range(0, maxs[0].shape[0]):
        if img_out[row, maxs[0][i]] > 0.01:
            max_vector = [max_vector, img_out[row,maxs[0][i]]]
            max_index = np.array([[row, maxs[0][i]]])
            if b == 0:
                indices = max_index
                b = b + 1
            else:
                indices = np.concatenate((indices, max_index), axis=0)
    if b!=0:
        if b == 1:
            total_indices = indices
        else:
            total_indices = np.concatenate((total_indices, indices), axis=0)
    else:
        continue

# Subplots
#plt.figure()

#plt.subplot(211)
#plt.imshow(img_out, cmap='gray')

#plt.subplot(212)
plt.imshow(img_in, cmap = 'gray')
plt.scatter(x=total_indices[:,0], y=total_indices[:,1], c='r', s=0.5)

plt.show()
