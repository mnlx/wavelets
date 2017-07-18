#import pywt
##import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd
##import scipy.stats as sci
#
#
#
#def upArrow_op(li, j):
#    if j == 0:
#        return [1]
#    N = len(li)
#    li_n = np.zeros(2 ** (j - 1) * (N - 1) + 1)
#    for i in range(N):
#        li_n[2 ** (j - 1) * i] = li[i]
#    return li_n
#
#
#def period_list(li, N):
#    n = len(li)
#    # append [0 0 ...]
#    n_app = N - np.mod(n, N)
#    li = list(li)
#    li = li + [0] * n_app
#    if len(li) < 2 * N:
#        return np.array(li)
#    else:
#        li = np.array(li)
#        li = np.reshape(li, [-1, N])
#        li = np.sum(li, axis=0)
#        return li
#
#
#def circular_convolve_mra(h_j_o, w_j):
##    ''' calculate the mra D_j'''
#    N = len(w_j)
#    l = np.arange(N)
#    D_j = np.zeros(N)
#    for t in range(N):
#        index = np.mod(t + l, N)
#        w_j_p = np.array([w_j[ind] for ind in index])
#        D_j[t] = (np.array(h_j_o) * w_j_p).sum()
#    return D_j
#
#
#def circular_convolve_d(h_t, v_j_1, j):
##    '''
##    jth level decomposition
##    h_t: \tilde{h} = h / sqrt(2)
##    v_j_1: v_{j-1}, the (j-1)th scale coefficients
##    return: w_j (or v_j)
##    '''
#    N = len(v_j_1)
#    L = len(h_t)
#    w_j = np.zeros(N)
#    l = np.arange(L)
#    for t in range(N):
#        index = np.mod(t - 2 ** (j - 1) * l, N)
#        v_p = np.array([v_j_1[ind] for ind in index])
#        w_j[t] = (np.array(h_t) * v_p).sum()
#    return w_j
#
#
#def circular_convolve_s(h_t, g_t, w_j, v_j, j):
##    '''
##    (j-1)th level synthesis from w_j, w_j
##    see function circular_convolve_d
##    '''
#    N = len(v_j)
#    L = len(h_t)
#    v_j_1 = np.zeros(N)
#    l = np.arange(L)
#    for t in range(N):
#        index = np.mod(t + 2 ** (j - 1) * l, N)
#        w_p = np.array([w_j[ind] for ind in index])
#        v_p = np.array([v_j[ind] for ind in index])
#        v_j_1[t] = (np.array(h_t) * w_p).sum()
#        v_j_1[t] = v_j_1[t] + (np.array(g_t) * v_p).sum()
#    return v_j_1
#
#
#def modwt(x, filters, level):
##    '''
##    filters: 'db1', 'db2', 'haar', ...
##    return: see matlab
##    '''
#    # filter
#    wavelet = pywt.Wavelet(filters)
#    h = wavelet.dec_hi
#    g = wavelet.dec_lo
#    h_t = np.array(h) / np.sqrt(2)
#    g_t = np.array(g) / np.sqrt(2)
#    wavecoeff = []
#    v_j_1 = x
##==============================================================================
##     
##  Importante: j é o nível de frequência que se deseja
##     
##     
##==============================================================================
#    for j in range(level):
#        w = circular_convolve_d(h_t, v_j_1, j + 1)
#        v_j_1 = circular_convolve_d(g_t, v_j_1, j + 1)
#        wavecoeff.append(w)
#    wavecoeff.append(v_j_1)
#    return np.vstack(wavecoeff)
#
#
#
#
#
#######################################################################
##inicio da minha parte
#
#
#
#
#preco = pd.read_excel('DATA_Consolidado.xlsx',index_col=0)
#
#ret = preco.pct_change(1)
#
#
#
#
#ret = ret.dropna()
#ret_ary = np.array(ret)[-3000:]
#
#
#D = {}
#col = 0
#
#for k in ret.columns:
#    D[k] = modwt(ret_ary[0:-1, list(ret.columns).index(k)] , 'haar' , 7)
#
#
#writer = pd.ExcelWriter('RRR.xlsx')
#
#



import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# example data
mu = np.mean( D[u'CMIG4.SA'][0]) # mean of distribution
sigma = np.var( D[u'CMIG4.SA'][0] )  # standard deviation of distribution
x = D[u'CMIG4.SA'][0]

num_bins = 200
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()




