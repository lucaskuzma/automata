import argparse


import sys
from random import randint


WIDTH = 64


def parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("rule", type=int, help="rule number")
    parser.add_argument("iterations", type=int, help="number of iterations")
    return parser.parse_args(args)


def stringify_state(state):
    return "".join('x' if x else '.' for x in state)


def iterate_state(state, rule, width):
    out_state = [False for i in range(width)]
    for i, cell in enumerate(state):
        # determine cell pattern
        l_neighbor = state[(i-1) % width]
        r_neighbor = state[(i+1) % width]
        pattern = (l_neighbor << 2) + (cell << 1) + r_neighbor
        
        # determine new state
        new_cell = rule[7 - pattern] == '1'
        out_state[i] = new_cell
    
    return out_state


def prepare_rule(rule):
    return str(bin(rule))[2:].zfill(8)


def main(args):
    args = parse(args)
    
    # get rule and make it into a binary appearing string
    rule = prepare_rule(args.rule)
    # print('rule: {}'.format(rule))
    
    # generate initial state
    n = randint(0, 2 ** WIDTH)
    state = [False for i in range(WIDTH)]
    for i in range(WIDTH):
        state[(WIDTH-1) - i] = True if n & 1 else False
        n = n >> 1

    print(stringify_state(state))
    
    # iterate state and print
    iterations = args.iterations
    for i in range(iterations):
        state = iterate_state(state, rule, WIDTH)
        print(stringify_state(state))


if __name__ == '__main__':
    main(sys.argv[1:])
