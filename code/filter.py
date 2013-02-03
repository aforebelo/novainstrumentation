from scipy import signal

from filtfilt import filtfilt


def highpass(s, f, order = 2, fs = 1000.0, use_filtfilt = True):
    '''
    @brief: for a given signal s rejects (attenuates) the frequencies lower then the cuttof frequency f
    and passes the frequencies higher than that value by applying a Butterworth digital filter
    
    @params:
    
    s: array-like
    signal
    
    f: int
    the cutoff frequency
    
    order: int
    Butterworth filter order
    
    fs: float
    sampling frequency  
    
    @return:
    
    signal: array-like
    filtered signal
    
    '''
    
    
    b, a=signal.butter(order, f/fs, btype = 'highpass')
    if use_filtfilt:
        return filtfilt(b, a, s)
    
    return signal.lfilter(b, a, s)




def bandstop(s, f1, f2, order = 2, fs = 1000.0, use_filtfilt = True):
    '''
    @brief: for a given signal s rejects (attenuates) the frequencies within a certain range (between f1 and f2)
    and passes the frequencies outside that range by applying a Butterworth digital filter
    
    @params:
    
    s: array-like
    signal
    
    f1: int
    the lower cutoff frequency
    
    f2: int
    the upper cutoff frequency
    
    order: int
    Butterworth filter order
    
    fs: float
    sampling frequency  
    
    @return:
    
    signal: array-like
    filtered signal
    
    '''
    b, a = signal.butter(order, [f1/fs, f2/fs], btype = 'bandstop')
    if use_filtfilt:
        return filtfilt(b, a, s)
    return signal.lfilter(b, a, s)

def bandpass(s, f1, f2, order = 2, fs = 1000.0, use_filtfilt = True):
    '''
    @brief: for a given signal s passes the frequencies within a certain range (between f1 and f2)
    and rejects (attenuates) the frequencies outside that range by applying a Butterworth digital filter
    
    @params:
    
    s: array-like
    signal
    
    f1: int
    the lower cutoff frequency
    
    f2: int
    the upper cutoff frequency
    
    order: int
    Butterworth filter order
    
    fs: float
    sampling frequency  
    
    @return:
    
    signal: array-like
    filtered signal
    
    '''
    b, a = signal.butter(order, [f1/fs, f2/fs], btype = 'bandpass')
    
    if use_filtfilt:
        return filtfilt(b, a, s)
    
    return signal.lfilter(b, a, s)