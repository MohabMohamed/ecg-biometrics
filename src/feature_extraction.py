import numpy as np
from scipy import fftpack


def autocorr(data):
    """Gets the autocorrelation of the signal
    @param: the signal
    @return: autocorrelation result
    """
    result = np.correlate(data, data, mode='full')
    return result[result.size / 2:]


def dct(data):
    """Gets the adiscrete cosine transform of the signal
    @param: the signal
    @return: numpy ndarray of the discrete cosine transform
    """
    return fftpack.dct(data, norm='ortho')


def extract_features(data):
    """returns the features array of the signal
    @param: the signal
    @return: numpy ndarray of the features
    """
    corr_res = autocorr(data)
    return dct(corr_res)
