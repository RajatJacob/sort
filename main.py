import numpy as np
import matplotlib.pyplot as plt
from search import LinSearch, BinarySearch

if __name__ == '__main__':
    x = range(1, int(1e6), 10000)
    print(x)
    bt = []
    lt = []
    for i in x:
        a = np.random.randint(0, i, i)
        target = np.random.choice(a)
        b = BinarySearch(a, target)
        b.search()
        bt.append(b._time())
        li = LinSearch(a, target)
        li.search()
        lt.append(li._time())
    plt.plot(x, bt, label='Binary')
    plt.plot(x, lt, label='Linear')
    plt.legend()
    plt.show()
    print(bt, lt)
