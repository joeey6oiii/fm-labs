import numpy as np


def trapz(f, t, v):
    F = []
    for k in v:
        F_k = np.trapz(f * np.exp(-1j * 2 * np.pi * k * t), t)
        F.append(F_k)
    return F


def undo_trapz(F, t, v):
    f = []
    for k in t:
        f_k = np.trapz(F * np.exp(1j * 2 * np.pi * k * v), v)
        f.append(f_k)
    return f


def dft(f, norm=None, coeff=1):
    fft_ = coeff * np.fft.fftshift(np.fft.fft(f, norm=norm))
    ifft_ = np.fft.ifft(np.fft.ifftshift(fft_ / coeff), norm=norm)
    return fft_, ifft_