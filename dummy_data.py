import numpy as np
import matplotlib.pyplot as plt


def make_positive(mask):
    mask[1, 4] = 1
    mask[4, 5] = 1
    mask[5, 6] = 1
    mask[6, 5] = 1
    mask[2, 2] = 0
    mask[2, 7] = 0
    mask[7, 2] = 0
    mask[7, 7] = 0
    return mask


def make_negative(mask):
    mask[2, 2] = 1
    mask[2, 7] = 1
    mask[7, 2] = 1
    mask[7, 7] = 1
    mask[5, 4] = 0
    mask[4, 5] = 0
    mask[5, 6] = 0
    mask[6, 5] = 0
    return mask

random_grid = np.random.uniform(0.2,0.7,[10,10])
mask = random_grid
# print(make_positive(mask))
plt.subplot(121)
plt.imshow(make_positive(mask), cmap="inferno")
random_grid = np.random.uniform(0.2,0.7,[10,10])
mask = random_grid
# print(make_negative(mask))
plt.subplot(122)
plt.imshow(make_negative(mask),cmap="inferno")

plt.show()