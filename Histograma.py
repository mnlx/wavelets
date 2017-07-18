import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as sci


# example data
for l in range(len(D.keys())):
    data = D[D.keys()[l]][6][-3000:-1]
             
    while data.max(axis = 0) > np.std(data)*3 or data.min(axis = 0) < -np.std(data)*3:
        data = np.delete(data, np.argmax(data, axis=0) , axis = 0)
        data = np.delete(data, np.argmin(data, axis=0) , axis = 0)
        
        
            
    
    mu = np.mean( data) # mean of distribution
    sigma = np.sqrt(np.var( data ))  # standard deviation of distribution
    x = data
    
    num_bins = 50
    # the histogram of the data
    n, bins, patches = plt.hist(x, num_bins, normed=2, facecolor='green', alpha=0.5,rwidth=0.2)
    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('%s' % D.keys()[l])
    
    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.show()
    
    norm = sci.normaltest(data,nan_policy='omit')