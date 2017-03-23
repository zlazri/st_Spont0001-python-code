def regseq(**kwargs):

    import os
    import cv2
    import numpy as np
    import matplotlib
    from matplotlib import pyplot as plt

    def preproc(inp1):
        out1 = np.float64(np.subtract(inp1,np.amin(inp1))/np.ptp(np.float64(inp1)))
        return out1

    def postproc(inp2):
        out2 = np.divide(inp2,np.amax(inp2))
        return out2

    def adjust_t(t0, dim):
        if t0> np.fix(dim/2):
            t = t0-dim-1
        else:
            t = t0-1
        return t

    def phase_corr_reg(F0, F):
        X = np.fft.ifft2(np.multiply(F0, np.conj(F)))
        max1 = np.amax(X, axis=0)
        argmax1 = np.argmax(X, axis=0)
        max2 = np. amax(max1, axis=0)
        argmax2 = np.argmax(max1, axis=0)
        tx = argmax2
        ty = argmax1[argmax2]
        m,n = F0.shape
        tx = adjust_t(tx, m)
        ty = adjust_t(ty, n)
        tval={'tx':tx, 'ty':ty, 'm':m, 'n':n}
        return tval


    if len(kwargs)<2:
        print('first two arguments must be input and output path')

    if len(kwargs)<3:
        kwargs['opts'] = {'dimX':512, 'dimY':512, 'numChannels':4, 'channel':1, 'templateFrame':0, 'timePts':300, 'dtype':'uint16', 'shape':(15000, 4, 512, 512), 'startFrame':0, 'stopFrame':300, 'debug':True, 'mode':'r', 'order':'C'} 
    
    
    infile = np.memmap(kwargs['inpath'], dtype = kwargs['opts']['dtype'], mode = kwargs['opts']['mode'],  shape = kwargs['opts']['shape'], order = kwargs['opts']['order'])
    img=preproc(infile[kwargs['opts']['templateFrame'],kwargs['opts']['channel'],:,:])
    templatefft = np.fft.fft2(img)

    outfile = open(kwargs['outpath'], 'w')
    for frame in range(kwargs['opts']['startFrame'],kwargs['opts']['stopFrame']):
        img = preproc(infile[frame,kwargs['opts']['channel'],:,:])
        tval = phase_corr_reg(templatefft, np.fft.fft2(img))
        M =np.float64([[1, 0, tval['tx']],[0, 1, tval['ty']]])
        new_img = cv2.warpAffine(img,M,(tval['m'],tval['n']))
        outfile.write(postproc(new_img))
    outfile.close()

kwargs = {'inpath':'/media/sf_Spont0001/Image_0001_0001.raw', 'outpath':'/home/zlazri/Desktop/Spont_PNG_1_to_700/New_Image_0001_0001.raw'}
regseq(**kwargs)
