import gabor
from gabor import gabor
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import scipy.ndimage.filters
from scipy.ndimage.filters import correlate as correlate

data_some_pics = np.memmap('/home/zlazri/Desktop/Spont_PNG_1_to_700/Newer_Image_0001_0001_mean.raw', dtype = 'float64', mode = 'r', shape=(300, 512, 512), order = 'C')
img_in = data_some_pics[1,:,:]
r0=16
sigma=10
f0=1/5
gb = gabor(r0,sigma,f0)
img_out = np.zeros((512,512))
img_out = correlate(img_in, gb)

# Subplots commented out
#f = plt.figure()

#plt.subplot(211)
#plt.imshow(img_in, cmap='gray')

#plt.subplot(212)
#plt.imshow(img_out, cmap='gray')

plt.imshow(img_out, cmap='gray')
plt.show()
#scipy.ndimage.correlate
#scipy.signal.correlate

