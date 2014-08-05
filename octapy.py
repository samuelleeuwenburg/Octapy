#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

import argparse
from components import *

def buildScale(args):
    ''' generate and output a scale '''
   
    # check if an accidental is present
    if len(args.tonic) == 2:
        accidental = args.tonic[1] 
    else:
        accidental = False

    # create tonic and scale
    tonic = note.new(args.tonic[0], accidental)
    s = scale.new(tonic, args.mode)

    # build and print message
    message = ''
    for i, n in enumerate(s.getScale()):
        if i == 0:
            message = n.render()
        else:
            message = message + ' - ' + n.render() 

    print message


def buildChord(args):
    ''' TODO '''
    return args


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title = 'Commands',
        description = 'Valid subcommands',
        help = 'Output options'
    )

    # scales
    scaleParser = subparsers.add_parser('build-scale')
    scaleParser.add_argument(
        '-m', '--mode',
        action = 'store', dest = 'mode', default = 'ionian',
        help = 'Specify a scale name, defaults to ionian'
    )
    scaleParser.add_argument(
        '-t', '--tonic',
        action = 'store', dest = 'tonic', default = 'C',
        help = 'Set the tonic, defaults to C'
    )
    scaleParser.set_defaults(func=buildScale)

    # chords
    chordParser = subparsers.add_parser('build-chord')
    chordParser.set_defaults(func=buildChord)

    # parse options
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()

    
