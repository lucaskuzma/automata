import argparse


import sys


def parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("rule", type=int, help="rule number")
    parser.add_argument("iterations", type=int, help="number of iterations")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    return parser.parse_args(args)


def main(args):
    args = parse(args)
    rule = str(bin(args.rule))[2:].zfill(8)
    print('rule: {}'.format(rule))
    

if __name__ == '__main__':
    main(sys.argv[1:])
