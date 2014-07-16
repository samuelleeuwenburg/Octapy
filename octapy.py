#!/usr/bin/env python2.7

from optparse import OptionParser
from components import *


def main():
    parser = OptionParser()

    # General options
    parser.add_option(
        '-m', '--mode', 
        action="store", type="string", dest="mode", default="ionian",
        help="Specify a scale name, defaults to ionian"
    )
    parser.add_option(
        '-t', '--tonic', 
        action="store", type="string", dest="tonic", default="C",
        help="Set the tonic, defaults to C"
    )

    # output options
    parser.add_option(
        '-s', '--scale',
        action="store_true", dest="output_scale", default=False,
        help="Outputs scale when set"
    )

    # parse options
    (options, args) = parser.parse_args()

    # handle arguments
    if options.output_scale:
        s = scale.new(options.tonic, options.mode)
        print s.getScale()


if __name__ == "__main__":
    main()

    
