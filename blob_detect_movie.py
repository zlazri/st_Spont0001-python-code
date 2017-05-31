import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skimage
from math import sqrt
from skimage import exposure
import os
from skimage.feature import blob_log, blob_dog, blob_doh
from matplotlib import animation

fig, axes = plt.subplots()
data_some_pics = np.memmap('Newer_Image_0001_0001_mean.raw', dtype = 'float64', mode = 'r', shape=(300, 512, 512), order = 'C')


def init():
    return []

def animate(n):
    patchy = []

    axes.cla()

    data_blw = data_some_pics[n,:,:]
    blobs_matrix = blob_log(data_blw, max_sigma = 30, threshold = .1)
    blobs_matrix[:, 2] = blobs_matrix[:, 2]*sqrt(2)

    blob_image = plt.imshow(data_blw, interpolation='nearest', cmap='gray')
    a = np.shape(blobs_matrix)

    for nums in range(0,a[0]):
        y = blobs_matrix[nums,0]
        x = blobs_matrix[nums,1]
        r = blobs_matrix[nums,2]
        c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
        patchy.append(c)
        patchy[nums].set_visible(True)
        axes.add_patch(c)
    return patchy
    
anim = animation.FuncAnimation(fig, animate, frames=10, blit = False)

plt.show()


