def gabor(r0, sigma, f0):

    import numpy as np
    import matplotlib
    from matplotlib import pyplot as plt
    import os
    import scipy
    from numpy import meshgrid
    from numpy import subtract
    from numpy import square
    from numpy import multiply
    from numpy import add
    from numpy import sqrt
    from numpy import meshgrid
    import math
    from math import pi
    from numpy import exp
    from numpy import cos
    from numpy import amax

    size = 5*sigma

    if round(size%2==0):
        size = size+1

    x = np.linspace(-round(size/2),round(size/2), round(size))
    y = np.linspace(round(size/2),-round(size/2), round(size))

    x1, y1 = meshgrid(x,y)

    r = sqrt(square(x1-sqrt(8))+square(y1-sqrt(8)))
    
    gb = (1/(2*pi*sigma*r0))*multiply(exp(-pi*square(r-r0)/(sigma^2)),cos(2*pi*f0*(r-r0)))
    max_gb =amax(gb)
    gb = gb/max_gb
#    plt.imshow(gb, cmap='gray')
#    plt.show()
    return gb
#Example
#gabor(16,10,1/5)
