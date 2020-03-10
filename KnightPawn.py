#!/usr/bin/env python3.7
from queue import Queue
digits = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
chars = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def find_path(filename):
    f = open(filename, 'r', encoding='utf-8')
    n = 1
    input = []
    output = []
    for line in f:
        if n == 1:
            input.append((digits[line[0]], int(line[1])))
        else:
            input.append((digits[line[0]], int(line[1])))
        n += 1
    f.close()
    parents = dict()
    q = Queue()
    q.put(input[0])
    while not q.empty():
        point = q.get()
        if point == input[1]:
            output.append(input[1])
            while point != input[0]:
                point = parents[point]
                output.append(point)
            break
        for dx in [-2, 2]:
            x_point = (point[0] + dx, point[1])
            for dy in [-1, 1]:
                xy_point = (x_point[0], x_point[1] + dy)
                if xy_point[0] < 1 or xy_point[0] > 8 \
                        or xy_point[1] < 1 or xy_point[1] > 8 \
                        or xy_point == (input[1][0] - 1, input[1][1] - 1) \
                        or xy_point == (input[1][0] + 1, input[1][1] - 1)\
                        or xy_point in parents.keys():
                    continue
                q.put(xy_point)
                parents[xy_point] = point
        for dy in [-2, 2]:
            y_point = (point[0], point[1] + dy)
            for dx in [-1, 1]:
                yx_point = (y_point[0] + dx, y_point[1])
                if yx_point[0] < 1 or yx_point[0] > 8 \
                        or yx_point[1] < 1 or yx_point[1] > 8 \
                        or yx_point == (input[1][0] - 1, input[1][1] - 1) \
                        or yx_point == (input[1][0] + 1, input[1][1] - 1)\
                        or yx_point in parents.keys():
                    continue
                q.put(yx_point)
                parents[yx_point] = point
    output.reverse()
    result = ''
    for e in output:
        result += chars[e[0]] + str(e[1]) + '\n'
    f = open('out.txt', 'w', encoding='utf-8')
    f.write(result)
    f.close()


if __name__ == '__main__':
    find_path('in.txt')
