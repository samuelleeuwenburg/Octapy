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
    degree = args.degree
    s = scale.new(tonic, args.name, args.degree)

    # build and print message
    message = ''
    for i, n in enumerate(s.getScale()):
        if i == 0:
            message = n.render()
        else:
            message = message + ' - ' + n.render() 

    print message


def buildChord(args):
    ''' generate and output a chord ''' 

    # check if an accidental is present
    if len(args.root) == 2:
        accidental = args.root[1] 
    else:
        accidental = False

    # create tonic and scale
    root = note.new(args.root[0], accidental)
    s = chord.new(root, args.name)

    # build and print message
    message = ''
    for i, n in enumerate(s.getChord()):
        if i == 0:
            message = n.render()
        else:
            message = message + ' - ' + n.render() 

    print message



def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title = 'Commands',
        description = 'Valid subcommands',
        help = 'Output options'
    )

    # scales
    scaleParser = subparsers.add_parser('scale')
    scaleParser.add_argument(
        '-n', '--name',
        action = 'store', dest = 'name', default = 'major',
        help = 'Specify a scale name, defaults to major'
    )
    scaleParser.add_argument(
        '-t', '--tonic',
        action = 'store', dest = 'tonic', default = 'C',
        help = 'Set the tonic, defaults to C'
    )
    scaleParser.add_argument(
        '-d', '--degree',
        action = 'store', dest = 'degree', default = 1,
        help = 'Set the to start the scale on, defaults to the first'
    )
    scaleParser.set_defaults(func=buildScale)


    # chords
    chordParser = subparsers.add_parser('chord')
    chordParser.add_argument(
        '-n', '--name',
        action = 'store', dest = 'name', default = 'maj7',
        help = 'Set the tonic, defaults to maj7'
    )
    chordParser.add_argument(
        '-r', '--root',
        action = 'store', dest = 'root', default = 'C',
        help = 'Set the root of the chord, defaults to C'
    )
    chordParser.set_defaults(func=buildChord)

    # parse options
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()

    
