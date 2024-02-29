import numpy as np
import math
def single_p(c, omega, room_dimensions, Xm, X, alpha):
    beta = np.sqrt(1 - np.array(alpha))

    Rp = np.array([
        X + Xm,
        X - Xm,
        X + np.array([Xm[0], -Xm[1], Xm[2]]),
        X + np.array([Xm[0], Xm[1], -Xm[2]]),
        X - np.array([-Xm[0], Xm[1], Xm[2]]),
        X - np.array([-Xm[0], -Xm[1], Xm[2]]),
        X + np.array([Xm[0], -Xm[1], -Xm[2]]),
        X - np.array([-Xm[0], Xm[1], -Xm[2]])
    ])

    P = 0
    for n in range(-2, 3):
        for l in range(-2, 3):
            for m in range(-2, 3):
                Rr = 2 * np.array([n * room_dimensions[0], l * room_dimensions[1], m * room_dimensions[2]])
                for p in range(8):
                    P += np.abs(np.exp(1j * (omega / c) * np.abs(Rp[p] + Rr)) / (4 * np.pi * np.abs(Rp[p] + Rr)) * np.exp(-1j * omega * 1))

    return P

def impulseresponse_generator(alpha, room_dimensions, Xm, X, fs, duration):
    c = 343

    omega = 2 * np.pi * fs
    
    Lx = room_dimensions[0]
    Ly = room_dimensions[1]
    Lz = room_dimensions[2]

    N = int(fs * duration)

    beta = np.sqrt(1 - np.array(alpha))

    bx1 = beta[0]
    bx2 = beta[1]
    by1 = beta[2]
    by2 = beta[3]
    bz1 = beta[4]
    bz2 = beta[5]
    
    # Making all combinations
    Ref = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])

    # Making the impulse response
    h = np.zeros(N)

    for n in range(0,10):
        for l in range(0,10):
            for m in range(0,10):
                for p in range(0,8):
                    Rp = np.array([X[0]-(Xm[0]+ 2 * Ref[p,:] * Xm), X[1]-(Xm[1]+2 * Ref[p,:] * Xm), X[2]-(Xm[2]+2 * Ref[p,:] * Xm)])   
                    Rr = 2 * np.array([n * Lx, l * Ly, m * Lz])
                    A = Rp + Rr
                    length = np.linalg.norm(A)
                    delay = length / c
                    sample = math.floor(delay * fs)
                    if sample > len(h):
                        break          
                    h[sample] = h[sample] + (bx1**(abs(n)) + bx2**(abs(n))) * (by1**(abs(l)) + by2**(abs(l))) * (bz1**(abs(m)) + bz2**(abs(m))) * np.exp(-1j * omega * length) / (4 * np.pi * length)
    return h



    





            










