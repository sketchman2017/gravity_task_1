# -*- coding: utf-8 -*-

def get_main_frequency(a):
    frequency = {}
    half = len(a)/2
    flag = False
    number = 0

    for i, key in enumerate(a):
        frequency[key] = frequency.get(key, 0) + 1
        if frequency[key] > half:
            flag = True
            number = i
            break

    if flag:
        return number
    else:
        return -1 


def tests():
    print 'Tests:'

    # test 1
    value = get_main_frequency([1, 2, 3, 4, 3, 3, 3, 3, 3])
    print '[1, 2, 3, 4, 3, 3, 3, 3, 3], result: ', value

    # test 2
    value = get_main_frequency([1, 2, 3, 4, 5, 3, 3, 3, 3])
    print '[1, 2, 3, 4, 5, 3, 3, 3, 3], result: ', value

    # test 3
    value = get_main_frequency([1, 2, 3, 4, 5, 5, 3, 3, 3])
    print '[1, 2, 3, 4, 5, 5, 3, 3, 3], result: ', value

    # test 4
    value = get_main_frequency([1])
    print '[1], result', value

    # test 5
    import random
    op = [int(100000*random.random()) for i in xrange(100000)]

    value = get_main_frequency(op)
    print 'random array len = 100000, result', value

    # test 6
    value = get_main_frequency([])
    print '[], result', value

tests()
