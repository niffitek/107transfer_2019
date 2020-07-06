#!/usr/bin/python3

import sys
import math


def param_to_array():
    array = []
    ret = []
    word = ""
    for i in range(1, len(sys.argv)):
        for j in range(len(sys.argv[i])):
            if (sys.argv[i][j] == '*'):
                array.append(word)
                word = ""
            else:
                word += sys.argv[i][j]
        if (word != ""):
            array.append(word)
            word = ""
        ret.append(array)
        array = []
    return ret


def error_handling():
    if (len(sys.argv) % 2 != 1 or len(sys.argv) == 1):
        exit(84)
    array = param_to_array()
    try:
        for list_v in array:
            for i in list_v:
                int(i)
    except ValueError:
        exit(84)
    main_calc(array)


def main_calc(array):
    x = 0.000
    while (x < 1.001):
        y = 0
        y1 = 0
        y2 = 0
        j = 0
        while (j < len(array)):
            i = 0
            tmp_y1 = 0
            tmp_y2 = 0
            while (i < (len(array[j]))):
                tmp_y1 += int(array[j][i]) * math.pow(x, (i))
                i += 1
            j += 1
            i = 0
            while (i < (len(array[j]))):
                tmp_y2 += int(array[j][i]) * math.pow(x, (i))
                i += 1
            y1 += tmp_y1
            y2 += tmp_y2
            j += 1
        if (y2 == 0):
            exit(84)
        y = float(y1 / y2)
        print("%.3f -> %.5f\n" % (x, y), end='')
        x += 0.001


error_handling()
