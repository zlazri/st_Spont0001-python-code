
def blob_detect(method, rawfile, outpath, frame_start, frame_stop, **kwargs):
    
    import matplotlib
    from matplotlib import pyplot as plt
    import numpy as np
    import skimage
    from math import sqrt
    from skimage import exposure
    import os
    
    # Import Method (note only 3 methods. If another method is specified, blob_log will automatically be implemented)
    if method == 'blob_log':
        from skimage.feature import blob_log
        blob_method = blob_log

    elif method == 'blob_dog':
        from skimage.feature import blob_dog
        blob_method = blob_dog

    else:
        from skimage.feature import blob_doh
        blob_method = blob_doh

    # Import images
    
    data_some_pics = np.memmap(rawfile, dtype = 'float64', mode = 'r', shape=(300, 512, 512), order = 'C')
    
    # Blob LOG All Pics
    
    # (Commented out code) os.chdir('/home/zlazri/Desktop/Spont_PNG_1_to_700/Denoised_Images/Mean/Blob_LOG')

    outfile = open(outpath, 'w')
    for nums in range(frame_start,frame_stop):
    
        data_blw = data_some_pics[nums,:,:]
        
        # Implmenting the blob detection functions, specifying inputs for method
        if method == 'blob_log':
            blobs_method = blob_method(data_blw, max_sigma = kwargs['max_sigma'], num_sigma = kwargs['num-sigma'], threshold = kwargs['threshold'])
        
        elif method == 'blob_dog':
            blobs_method = blob_method(data_blw, max_sigma = kwargs['max_sigma'], threshold = kwargs['threshold'])
        
        else:
            blobs_method = blob_method(data_blw, max_sigma = kwargs['max_sigma'], threshold = kwargs['threshold'])

        # The next two lines are only reuqired for DOG and LOG
        if method != 'blob_doh':
            blobs_method[:, 2] = blobs_method[:, 2] * sqrt(2)
        


        # Creating the images
        titles = [method, 'Without Blobs']
        fig, axes = plt.subplots(1, 2, sharex=True, sharey=True, subplot_kw={'adjustable': 'box-forced'})
        ax = axes.ravel()
        
        for idx, title in enumerate(titles):
            ax[idx].set_title(title)
            ax[idx].imshow(data_blw, interpolation='nearest', cmap='gray')
            if title == method:
                for blob in blobs_method:
                    y, x, r = blob
                    c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
                    ax[idx].add_patch(c)
            ax[idx].set_axis_off()
        
        plt.tight_layout()
        
        outfile.write(fig)
    outfile.close()


# Testing that the dunction works

kwargs = {'max_sigma':30, 'num_sigma':10, 'threshold':.1}
blob_detect('blob_dog', '/home/zlazri/Desktop/Spont_PNG_1_to_700/Newer_Image_0001_0001_mean.raw', '/home/zlazri/Desktop/Spont_PNG_1_to_700/Image_blob_detect_func.raw', 50, 60, **kwargs)
