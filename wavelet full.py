#%%
import numpy as np
import pywt
from pandas_datareader import data
from datetime import datetime
import pandas as pd
import os


def upArrow_op(li, j):
    if j == 0:
        return [1]
    N = len(li)
    li_n = np.zeros(2 ** (j - 1) * (N - 1) + 1)
    for i in range(N):
        li_n[2 ** (j - 1) * i] = li[i]
    return li_n


def period_list(li, N):
    n = len(li)
    # append [0 0 ...]
    n_app = N - np.mod(n, N)
    li = list(li)
    li = li + [0] * n_app
    if len(li) < 2 * N:
        return np.array(li)
    else:
        li = np.array(li)
        li = np.reshape(li, [-1, N])
        li = np.sum(li, axis=0)
        return li


def circular_convolve_mra(h_j_o, w_j):
    ''' calculate the mra D_j'''
    N = len(w_j)
    l = np.arange(N)
    D_j = np.zeros(N)
    for t in range(N):
        index = np.mod(t + l, N)
        w_j_p = np.array([w_j[ind] for ind in index])
        D_j[t] = (np.array(h_j_o) * w_j_p).sum()
    return D_j


def circular_convolve_d(h_t, v_j_1, j):
    '''
    jth level decomposition
    h_t: \tilde{h} = h / sqrt(2)
    v_j_1: v_{j-1}, the (j-1)th scale coefficients
    return: w_j (or v_j)
    '''
    N = len(v_j_1)
    L = len(h_t)
    w_j = np.zeros(N)
    l = np.arange(L)
    for t in range(N):
        index = np.mod(t - 2 ** (j - 1) * l, N)
        v_p = np.array([v_j_1[ind] for ind in index])
        w_j[t] = (np.array(h_t) * v_p).sum()
    return w_j


def circular_convolve_s(h_t, g_t, w_j, v_j, j):
    '''
    (j-1)th level synthesis from w_j, w_j
    see function circular_convolve_d
    '''
    N = len(v_j)
    L = len(h_t)
    v_j_1 = np.zeros(N)
    l = np.arange(L)
    for t in range(N):
        index = np.mod(t + 2 ** (j - 1) * l, N)
        w_p = np.array([w_j[ind] for ind in index])
        v_p = np.array([v_j[ind] for ind in index])
        v_j_1[t] = (np.array(h_t) * w_p).sum()
        v_j_1[t] = v_j_1[t] + (np.array(g_t) * v_p).sum()
    return v_j_1


def modwt(x, filters, level):
    '''
    filters: 'db1', 'db2', 'haar', ...
    return: see matlab
    '''
    # filter
    wavelet = pywt.Wavelet(filters)
    h = wavelet.dec_hi
    g = wavelet.dec_lo
    h_t = np.array(h) / np.sqrt(2)
    g_t = np.array(g) / np.sqrt(2)
    wavecoeff = []
    v_j_1 = x
#==============================================================================
#     
#  Importante: j é o nível de frequência que se deseja
#     
#     
#==============================================================================
    for j in range(level):
        w = circular_convolve_d(h_t, v_j_1, j + 1)
        v_j_1 = circular_convolve_d(g_t, v_j_1, j + 1)
        wavecoeff.append(w)
    wavecoeff.append(v_j_1)
    return np.vstack(wavecoeff)



ibov_list =['ABEV3.SA', 'BBAS3.SA', 'BBDC3.SA',
 'BRAP4.SA', 'BRFS3.SA',
  'CPFE3.SA',
 'CPLE6.SA', 'CSNA3.SA',
 'CYRE3.SA', 'EMBR3.SA',
 'GGBR4.SA', 'GOAU4.SA',
 'ITSA4.SA', 'LAME4.SA',
 'PETR3.SA', 'PETR4.SA',
 'SBSP3.SA', 'SUZB5.SA',
 'USIM5.SA', 'VALE3.SA',
 'VIVT4.SA', 'WEGE3.SA']
             


yah_fin = [data.DataReader(x ,  'yahoo', datetime(2003,1,1), datetime(2016,6,1))['Close'] for x in ibov_list]
preco = pd.concat(yah_fin , axis=1)
preco.columns = ibov_list


wrt = pd.ExcelWriter('PrecosCru.xlsx' )

preco.to_excel(wrt, 'sheet1')

wrt.save()


#%%




# removendo dado outliers

def reject_outliers(data, m=0.3):
    return data[abs(data) < m]

def zero_sum(data):
    return np.where( [0 == data ])[1].size/float(data.size)

#skew = ret.skew()
#kurt = ret.kurt()
#norm = sci.normaltest(ret,nan_policy='omit')







D = {}
date = {}


for k in preco.columns:
    mod_ret = reject_outliers(preco[k].pct_change(1)).dropna()
    mod_ret_array = np.array(mod_ret)
    if mod_ret_array.shape[0] < 3000:
        pass
    elif zero_sum(mod_ret_array)>0.1:

        pass
    else:
        date[k] = mod_ret.index
        D[k] = np.c_[ modwt( mod_ret_array , 'haar' , 7).T, mod_ret]



for x in D.keys():
    
    nme= str.split(str(x), '.')[0]
    
    writer = pd.ExcelWriter(os.path.join(os.getcwd(),'dados\\%s.xlsx' % nme))
    df = pd.DataFrame(D[x]).set_index(date[x])
    df.to_excel(writer, 'sheet1')

    writer.save()
    
