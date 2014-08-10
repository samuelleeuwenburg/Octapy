# -*- coding: utf-8 -*-

from components import *

def build(args):
    # check if an accidental is present

    if len(args.root) > 1:
        accidental = args.root[1:len(args.root)] 
    else:
        accidental = False

    # create tonic and scale
    root = note.new(args.root[0].upper(), accidental)

    if not root:
        exit()

    c = chord.new(root, args.name)

    # render and print
    print c.render()

def setup(subparsers):

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

    chordParser.set_defaults(func=build)


