# -*- coding: utf-8 -*-

from components import *

def build(args):
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


def setup(subparsers):

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
    scaleParser.set_defaults(func=build)
