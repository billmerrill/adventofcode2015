# nice:
# - at least 3 vowels
# - at least one double (xx)
# - no substrs ab, cd, pq, xy
import re

def part_one():
    with open('day_5_input.txt', 'rb') as fh:
        input = fh.read()

    strings = input.split('\n')

    nice_count = 0
    naughty_count = 0
    naughty_combos_re = re.compile("ab|cd|pq|xy")
    three_vowels_re = re.compile("[aeiou]")
    double_letter_re = re.compile(r"(.)\1")
    for s in strings:
        if len(re.findall(naughty_combos_re, s)) > 0:
            naughty_count += 1
            continue
        if len(re.findall(three_vowels_re, s)) < 3:
            naughty_count += 1
            continue
        if len(re.findall(double_letter_re, s)) > 0:
            nice_count += 1
            continue
        naughty_count + 1

    print 'part one'
    print 'naughty {} \nnice {}\n'.format(naughty_count, nice_count)


def part_two():
    with open('day_5_input.txt', 'rb') as fh:
        input = fh.read()

    strings = input.split('\n')
    nice_triplet_re = re.compile(r'(.).\1')
    two_doubles_re = re.compile(r'(.{2}).*\1')
    nice_count = 0
    naughty_count = 0
    for s in strings:
        if len(re.findall(nice_triplet_re, s)) > 0 and \
           len(re.findall(two_doubles_re, s)) > 0:
            nice_count += 1
            continue
        naughty_count += 1

    print 'part two'
    print 'naughty {} \nnice {}'.format(naughty_count, nice_count)



part_one()
part_two()
