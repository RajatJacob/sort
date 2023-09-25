import numpy as np
import matplotlib.pyplot as plt
from search import LinSearch, BinarySearch

if __name__ == '__main__':
    x = range(1, int(1e4), 100)
    bt = []
    lt = []
    for i in x:
        ba = []
        la = []
        for j in range(100):
            a = np.random.randint(0, i*1000, i)
            target = np.random.choice(a)
            b = BinarySearch(a, target)
            b.search()
            ba.append(b._time())
            li = LinSearch(a, target)
            li.search()
            la.append(li._time())
        bt.append(sum(ba)/len(ba))
        lt.append(sum(la)/len(la))
    plt.plot(x, lt, label='Linear')
    plt.plot(x, bt, label='Binary')
    plt.legend()
    plt.show()
