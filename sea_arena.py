# 0 - not ship
# 1 - the ship is on fire
# 2 - ship is already

import numpy as np
import random
from itertools import product

bot_arena = np.zeros(100).reshape(10, 10)
places = list(product(range(10), range(10)))

for i in range(4):
    bot_arena[random.choice(places)] = 2


print(bot_arena)

