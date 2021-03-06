# -*- coding: utf-8 -*-

def get_main_frequency(a):
    # Задание 1

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

def task_2(a, b, m):
    # Задание 2

    if m == 0:
        return 0

    k = 0
    # Увеличиваем i до первого делящегося числа от а сверху
    i = a
    while i <= b:
        if i % m == 0:
            k = k + 1
            break
        i = i + 1
    if i >= b:
        return k

    # Увеличиваем j до первого делящегося числа
    j = b
    while j > a:
        if j % m == 0 and j != i:
            k = k + 1
            break
        j = j - 1

    if j <= a:
        return k

    return (j - i) / m + k - 1

def tests_2():
    # Тесты

    count = task_2(6, 11, 2)
    print 'A=6, B=11, M=2. result =', count

    count = task_2(3, 17, 3)
    print 'A=3, B=17, M=3. result =', count

    count = task_2(10, 13, 97)
    print 'A=10, B=13, M=97. result =', count

    count = task_2(10, 97, 13)
    print 'A=10, B=97, M=13. result =', count

    count = task_2(0, 2000000000, 2)
    print 'A=0, B=2000000000, M=2. result =', count

    count = task_2(0, 10, 0)
    print 'A=0, B=10, M=0. result =', count

    count = task_2(0, 10, 1)
    print 'A=0, B=10, M=1. result =', count

    count = task_2(5, 10, 5)
    print 'A=5, B=10, M=5. result =', count

    count = task_2(5, 5, 5)
    print 'A=5, B=5, M=5. result =', count

    count = task_2(3, 90, 3)
    print 'A=3, B=90, M=3. result =', count

    count = task_2(3, -3, 3)
    print 'A=3, B=-3, M=3. result =', count

    count = task_2(-3, 9, 3)
    print 'A=-3, B=9, M=3. result =', count

def task_3(a):
    # Задание 3

    b = []

    for i, value in enumerate(a):
        # Для каждого, кроме первого и последнего элементов
        if i > 0 and i < len(a) - 1:
            # Исключаем элементы, заведомо ненужные для рассчетов -
            # - находящиеся не на максимумах и минимумах
            if value >= a[i-1] and value <= a[i+1]:
                continue
            if value <= a[i-1] and value >= a[i+1]:
                continue
        b.append(value)

    max_dif = 0
    for i, value in enumerate(b[:len(b)-1]):
        m = max(b[i+1:])
        if m - value > max_dif:
            max_dif = m - value

    return max_dif


def tests_3():
    # tests

    import random
    op = [int(200000*random.random()) for i in xrange(4000)]

    t = task_3(op)
    print 'Random array, 4000 elements. result =', t

    t = task_3([25191, 23031, 23143, 23386, 23033, 23387])
    print '[25191, 23031, 23143, 23386, 23033, 23387]. result =', t

    t = task_3([25191, 23031, 23017, 23012, 23000])
    print '[25191, 23031, 23017, 23012, 23000]. result =', t 
tests_3()
