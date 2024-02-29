import numpy as np
import matplotlib.pyplot as plt
from roomplotter import roomplot
from impulse_response import*

c = 343
omega = 1
room_dimensions = np.array([30, 30, 30])
Xm = np.array([10, 10, 2.5])  # Source position
X = np.array([15, 15, 2.5])  # Receiver position
alpha = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]  # Absorption coefficients

source_position = Xm
receiver_position = X


#plotting the room
roomplot(room_dimensions, source_position, receiver_position)

# doing the impuls response for single sample
P = single_p(c, omega, room_dimensions, Xm, X, alpha)
print(P)

Resp=impulseresponse_generator(alpha, room_dimensions, Xm, X, 44100, 1)

plt.plot(Resp)
plt.show()

