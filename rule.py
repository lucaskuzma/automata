import argparse


import sys
from random import randint


WIDTH = 64


def parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("rule", type=int, help="rule number")
    parser.add_argument("iterations", type=int, help="number of iterations")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    return parser.parse_args(args)


def print_state(state):
    print("".join('x' if x else '.' for x in state))


def main(args):
    args = parse(args)
    
    rule = str(bin(args.rule))[2:].zfill(8)
    print('rule: {}'.format(rule))
    
    n = randint(0, 2 ** WIDTH)
    state = [False for i in range(WIDTH)]
    for i in range(WIDTH):
        state[(WIDTH-1) - i] = True if n & 1 else False
        n = n >> 1
    
    print_state(state)


if __name__ == '__main__':
    main(sys.argv[1:])
