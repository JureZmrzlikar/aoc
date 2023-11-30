def iterate_loop1(stop):
    n = 1
    x, y, order = 0, 0, 0
    dont_go_up, dont_go_left = True, True
    while True:
        # print((n, x, y, order))
        if n == stop:
            return abs(x) + abs(y)
        if y < order and not dont_go_up:
            # print('up')
            n += 1
            y += 1
        elif x > -order and not dont_go_left:
            # print('left')
            n += 1
            x -= 1
            dont_go_up = True
        elif y > -order:
            # print('down')
            n += 1
            y -= 1
            dont_go_left = True
        elif x < order:
            # print('right')
            n += 1
            x += 1
        else:
            # print('new order!')
            n += 1
            x += 1
            order += 1
            dont_go_up = False
            dont_go_left = False


def sum_adjacent(x, y, memory):
    possible = [
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
    ]
    sum_ = 0
    for (px, py) in possible:
        sum_ += memory.get((px, py), 0)
    return sum_


def iterate_loop2(stop):
    n = 1
    x, y, order = 0, 0, 0
    dont_go_up, dont_go_left = True, True
    memory = {(0, 0): 1}
    while True:
        # print((n, x, y, order))
        if n > stop:
            return n
        if y < order and not dont_go_up:
            # print('up')
            y += 1
        elif x > -order and not dont_go_left:
            # print('left')
            x -= 1
            dont_go_up = True
        elif y > -order:
            # print('down')
            y -= 1
            dont_go_left = True
        elif x < order:
            # print('right')
            x += 1
        else:
            # print('new order!')
            x += 1
            order += 1
            dont_go_up = False
            dont_go_left = False
        n = sum_adjacent(x, y, memory)
        memory[(x, y)] = n


STOP = 289326
print(iterate_loop1(STOP))
print(iterate_loop2(STOP))
