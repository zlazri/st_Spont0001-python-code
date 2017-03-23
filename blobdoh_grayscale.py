import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skimage
from math import sqrt
from skimage import exposure
from skimage.feature import blob_doh
import os

# Import images

data_some_pics = np.memmap("Newer_Image_0001_0001_mean.raw", dtype = 'float64', mode = 'r', shape=(300, 512, 512), order = 'C')

# Blob DOH All Pics

os.chdir('/home/zlazri/Desktop/Spont_PNG_1_to_700/Denoised_Images/Mean/Blob_DOH')

for nums in range(250,300):

    data_blw = data_some_pics[nums,:,:]
    
    blobs_doh = blob_doh(data_blw, max_sigma=30, threshold=.01)
        
    titles = ['Difference of Hessian', 'Without Blobs']
    fig, axes = plt.subplots(1, 2, sharex=True, sharey=True, subplot_kw={'adjustable': 'box-forced'})
    ax = axes.ravel()
    
    for idx, title in enumerate(titles):
        ax[idx].set_title(title)
        ax[idx].imshow(data_blw, interpolation='nearest', cmap='gray')
        if title == 'Difference of Hessian':
            for blob in blobs_doh:
                y, x, r = blob
                c = plt.Circle((x, y), r, color='lime', linewidth=2, fill=False)
                ax[idx].add_patch(c)
        ax[idx].set_axis_off()
    
    plt.tight_layout()

    if nums < 10:
        str1 = "fig.savefig(\"Mean_Difference_Hessian00" + str(nums) + ".png\")"
        exec(str1)
    elif 10<= nums < 100:
        str1 = "fig.savefig(\"Mean_Difference_Hessian0" + str(nums) + ".png\")"
        exec(str1)
    else:
        str1 = "fig.savefig(\"Mean_Difference_Hessian" + str(nums) + ".png\")"
        exec(str1)
