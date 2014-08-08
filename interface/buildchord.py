# -*- coding: utf-8 -*-

from components import *

def build(args):
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



