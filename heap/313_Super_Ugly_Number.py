# -*- coding: utf-8 -*-
"""
Description:

Created on: 
@author: YIPENG ZHU
"""
import heapq


# Method 1 ???
def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    uglies = [0] * n
    idx = [0] * len(primes) # That's for idx
    uglies[0] = 1

    # Build a heap
    heap = []
    for k, p in enumerate(primes):
        heapq.heappush(heap, (p, k))

    u_p = [0] * n

    for i in range(1, n):
        uglies[i], k = heapq.heappop(heap)
        u_p[i] = k
        idx[k] += 1

        while u_p[idx[k]] > k:
            idx[k] += 1

        heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))

    return uglies[-1]


# Method 2
def nthSuperUglyNumber2(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    uglies = [1]

    def gen(prime):
        for ugly in uglies:
            yield ugly * prime

    print(*map(gen, primes))
    print("--------------------")
    merged = heapq.merge(*map(gen, primes))

    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)

    return uglies[-1]



def m_f(*iterables):
    h = []
    for order, it in enumerate(map(iter, iterables)):
        try:
            next = it.__next__   # A function
            h.append([next(), order * 1, next])
        except StopIteration:
            pass

    heapq.heapify(h)
    print(len(h))

    while len(h) > 1:
        try:
            while True:
                value, order, next = s = h[0]
                yield value
                s[0] = next()  # raises StopIteration when exhausted
                heapq.heapreplace(h, s)  # restore heap condition
        except StopIteration:
            heapq.heappop(h)  # remove empty iterator

    # When h == 1
    if h:
        # fast case when only a single iterator remains
        value, order, next = h[0]
        yield value
        yield from next.__self__



if __name__ == "__main__":
    print('----------------------------')
    x = [[3, 3, 130], [1, 2, 6]]
    z = m_f(*x)
    print(next(z))
