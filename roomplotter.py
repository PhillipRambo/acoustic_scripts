import numpy as np
import matplotlib.pyplot as plt

def roomplot(room_dimensions,source_position, receiver_position):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot([0, 0], [0, 0], [0, room_dimensions[2]], color='k')
    ax.plot([0, 0], [room_dimensions[1], room_dimensions[1]], [0, room_dimensions[2]], color='k')
    ax.plot([room_dimensions[0], room_dimensions[0]], [0, 0], [0, room_dimensions[2]], color='k')
    ax.plot([room_dimensions[0], room_dimensions[0]], [room_dimensions[1], room_dimensions[1]], [0, room_dimensions[2]], color='k')
    ax.plot([0, room_dimensions[0]], [0, 0], [0, 0], color='k')
    ax.plot([0, room_dimensions[0]], [0, 0], [room_dimensions[2], room_dimensions[2]], color='k')
    ax.plot([0, room_dimensions[0]], [room_dimensions[1], room_dimensions[1]], [0, 0], color='k')
    ax.plot([0, room_dimensions[0]], [room_dimensions[1], room_dimensions[1]], [room_dimensions[2], room_dimensions[2]], color='k')
    ax.plot([0, 0], [0, room_dimensions[1]], [0, 0], color='k')
    ax.plot([0, 0], [0, room_dimensions[1]], [room_dimensions[2], room_dimensions[2]], color='k')
    ax.plot([room_dimensions[0], room_dimensions[0]], [0, room_dimensions[1]], [0, 0], color='k')
    ax.plot([room_dimensions[0], room_dimensions[0]], [0, room_dimensions[1]], [room_dimensions[2], room_dimensions[2]], color='k')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(0, room_dimensions[0])
    ax.set_ylim(0, room_dimensions[1])
    ax.set_zlim(0, room_dimensions[2])

    #plotting the source and receiver

    ax.scatter(source_position[0], source_position[1], source_position[2], color='r', marker='o', label='Source')
    ax.scatter(receiver_position[0], receiver_position[1], receiver_position[2], color='b', marker='o', label='Receiver')

    plt.legend()
    plt.show()