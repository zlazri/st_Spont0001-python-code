import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# import images
data_some_pics = np.memmap("New_Image_0001_0001.raw", dtype = 'float64', mode = 'r', shape=(300,512,512), order = 'C')
data_denoised = np.zeros(shape=(300,512,512))

for nums in range(0, 300):
    for nums1 in range(0, 512):
        for nums2 in range(0, 512):
            if nums1-1<0:
                if nums2-1<0:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1),(nums2)] + data_some_pics[nums,(nums1),(nums2)] + data_some_pics[nums,(nums1+1),(nums2+1)])/3
                elif nums2+1>511:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1),(nums2-1)] + data_some_pics[nums,(nums1),(nums2)] + data_some_pics[nums,(nums1+1),(nums2-511)])/3
                else:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1),(nums2-1)] + data_some_pics[nums,(nums1),(nums2)] + data_some_pics[nums,(nums1+1),(nums2+1)])/3

            elif nums1+1>511:
                if nums2-1<0:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1),(nums2+511)] + data_some_pics[nums,(nums1),(nums2)] + data_some_pics[nums,(nums1-511),(nums2+1)])/3
                elif nums2+1>511:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1),(nums2-1)] + data_some_pics[nums,(nums1),(nums2)] + data_some_pics[nums,(nums1-511),(nums2-511)])/3
                else:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1),(nums2-1)] + data_some_pics[nums,(nums1),(nums2)]+ data_some_pics[nums,(nums1-511),(nums2+1)])/3

            else:
                if nums2-1<0:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1-1),(nums2+511)] + data_some_pics[nums,(nums1),(nums2)] + data_some_pics[nums,(nums1+1),(nums2+1)])/3
                elif nums2+1>511:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1-1),(nums2-1)] + data_some_pics[nums,(nums1),(nums2)] +  data_some_pics[nums,(nums1+1),(nums2-511)])/3
                else:
                    data_denoised[nums, nums1, nums2]= (data_some_pics[nums,(nums1-1),(nums2-1)] + data_some_pics[nums,(nums1),(nums2)] + data_some_pics[nums,(nums1+1),(nums2+1)])/3


outfile = open('/home/zlazri/Desktop/Spont_PNG_1_to_700/Newer_Image_0001_0001_mean.raw', 'w')
for nums in range(0, 300):
    outfile.write(data_denoised[nums,:,:])
outfile.close()
