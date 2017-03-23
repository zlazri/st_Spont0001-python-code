import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skimage
from math import sqrt
from skimage import exposure
from skimage.feature import blob_log
import os

# Import images

data_some_pics = np.memmap("Newer_Image_0001_0001_mean.raw", dtype = 'float64', mode = 'r', shape=(300, 512, 512), order = 'C')

# Blob LOG All Pics

os.chdir('/home/zlazri/Desktop/Spont_PNG_1_to_700/Denoised_Images/Mean/Blob_LOG')

for nums in range(75,100):

    data_blw = data_some_pics[nums,:,:]
    
    blobs_log = blob_log(data_blw, max_sigma=30, num_sigma=10, threshold=.1)
    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
        
    titles = ['Laplacian of Gaussian', 'Without Blobs']
    fig, axes = plt.subplots(1, 2, sharex=True, sharey=True, subplot_kw={'adjustable': 'box-forced'})
    ax = axes.ravel()
    
    for idx, title in enumerate(titles):
        ax[idx].set_title(title)
        ax[idx].imshow(data_blw, interpolation='nearest', cmap='gray')
        if title == 'Laplacian of Gaussian':
            for blob in blobs_log:
                y, x, r = blob
                c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
                ax[idx].add_patch(c)
        ax[idx].set_axis_off()
    
    plt.tight_layout()

    if nums < 10:
        str1 = "fig.savefig(\"Mean_Laplacian_Gaussian00" + str(nums) + ".png\")"
        exec(str1)
    elif 10<= nums < 100:
        str1 = "fig.savefig(\"Mean_Laplacian_Gaussian0" + str(nums) + ".png\")"
        exec(str1)
    else:
        str1 = "fig.savefig(\"Mean_Laplacian_Gaussian" + str(nums) + ".png\")"
        exec(str1)
