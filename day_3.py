import numpy as np

def run_year_one():
    with open('day_3_input.txt', 'rb') as fh:
        directions = fh.read()

    loc = np.array([0, 0])
    houses = {}

    def deliver_present():
        house = str(loc)
        if house in houses:
            houses[house] += 1
        else:
            houses[house] = 1

    deliver_present()

    for d in directions:
        if d == '^':
            loc += [0, 1]
        elif d == '>':
            loc += [1, 0]
        elif d == 'v':
            loc += [0, -1]
        elif d == '<':
            loc += [-1, 0]

        deliver_present()

    print "Year 1: Houses that get at least one present: %s\n" % len(houses)


def run_year_two():
    with open('day_3_input.txt', 'rb') as fh:
        directions = fh.read()

    santa_loc = np.array([0, 0])
    robot_loc = np.array([0, 0])
    houses = {}

    def deliver_present(loc):
        house = str(loc)
        if house in houses:
            houses[house] += 1
        else:
            houses[house] = 1

    def move(loc, d):
        if d == '^':
            loc += [0, 1]
        elif d == '>':
            loc += [1, 0]
        elif d == 'v':
            loc += [0, -1]
        elif d == '<':
            loc += [-1, 0]
        return loc

    deliver_present(santa_loc)
    deliver_present(robot_loc)

    diter = iter(directions)
    for d in diter:
        santa_loc = move(santa_loc, d)
        deliver_present(santa_loc)
        try:
            robot_loc = move(robot_loc, next(diter))
            deliver_present(robot_loc)
        except StopIteration:
            break

    print "Year 2: Houses that get at least one present: %s\n" % len(houses)


run_year_one()
run_year_two()
