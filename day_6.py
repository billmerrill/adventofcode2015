import numpy as np
import re

def part_one():

    lights = np.zeros((1000,1000), dtype=np.uint8)

    def inside(it, ul, lr):
        x = ul[0] <= it.multi_index[0] <= lr[0]
        xx = ul[1] <= it.multi_index[1] <= lr[1]
        return x and xx

    def turn_on(ul, lr):
        it = np.nditer(lights, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            if inside(it, ul, lr):
                it[0] = 1
            it.iternext()

    def turn_off(ul, lr):
        it = np.nditer(lights, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            if inside(it, ul, lr):
               it[0] = 0
            it.iternext()

    def toggle(ul, lr):
        it = np.nditer(lights, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            if inside(it, ul, lr):
               it[0] = 0 if it[0] else 1
            it.iternext()

    def turn_up(ul, lr):
        it = np.nditer(lights, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            if inside(it, ul, lr):
                it[0] += 1
            it.iternext()

    def new_toggle(ul,lr):
        it = np.nditer(lights, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            if inside(it, ul, lr):
                it[0] += 2
            it.iternext()

    def turn_down(ul, lr):
        it = np.nditer(lights, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            if inside(it, ul, lr):
                it[0] = 0 if it[0] == 0 else it[0]-1
            it.iternext()




    INST = {'turn on': turn_on,
            'turn off': turn_off,
            'toggle': toggle}

    INST = {'turn on': turn_up,
            'turn off': turn_down,
            'toggle': new_toggle}

    with open('day_6_input.txt', 'rb') as fh:
        ins = fh.read()
    inx = ins.split('\n')

    instruct_re = re.compile(r'(?P<instruct>turn on|turn off|toggle)\s+' +
                             r'(?P<ax>[0-9]+)\,(?P<ay>[0-9]+)' +
                             r'\s+through\s+' +
                             r'(?P<bx>[0-9]+)\,(?P<by>[0-9]+)')

    for s in inx:
        m = re.match(instruct_re, s)
        if m is None:
            # print 'No Match |%s|' % s
            continue
        ln = m.groupdict()
        INST[ln['instruct']]((int(ln['ax']),int(ln['ay'])), (int(ln['bx']), int(ln['by'])))
        # turn_on((int(ln['ax']),int(ln['ay'])), (int(ln['bx']), int(ln['by'])))
        # ons = lights.sum()
        print ln['ax']



    print "THERE ARE %d LIGHTS!" % lights.sum()



part_one()
