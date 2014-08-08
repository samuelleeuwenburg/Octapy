#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

import argparse
from interface import *
   
def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(
        title = 'Commands',
        description = 'Valid subcommands',
        help = 'Output options'
    )

    buildscale.setup(subparsers)
    buildchord.setup(subparsers)

    # parse options
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()

    
