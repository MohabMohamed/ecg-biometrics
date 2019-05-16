import numpy as np
from scipy import fftpack


def _autocorr(data):
    """Gets the autocorrelation of the signal
    @param: the signal
    @return: autocorrelation result
    """
    result = np.correlate(data, data, mode='full')
    return result[len(result) // 2:]


def _dct(data):
    """Gets the discrete cosine transform of the signal
    @param: the signal
    @return: numpy ndarray of the discrete cosine transform
    """
    return fftpack.dct(data, norm='ortho')


def extract_features(data):
    """returns the features array of the signal
    @param: the signal
    @return: numpy ndarray of the features
    """
    corr_res = _autocorr(data)
    return _dct(corr_res)
