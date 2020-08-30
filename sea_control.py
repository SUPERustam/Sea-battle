import numpy as np
import random
from itertools import product

bot_arena = np.zeros(100).reshape(10, 10)
places = list(product(range(10), range(10)))
