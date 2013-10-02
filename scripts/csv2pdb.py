#!/usr/bin/env python
__author__ = "Gon Nido"
__copyright__ = "Copyright 2012"
__credits__ = ["Gon Nido"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Gon Nido"
__email__ = "insectopalo@gmail.com"
__status__ = "Production"

import sys
import re
import getopt

def usage():
    sys.stderr.write("usage: "+sys.argv[0]+" <inputfile.csv> " +
                     "<outputfile.pdb>\n")

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"h")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
    if len(args) != 2:
        usage()
        sys.exit(2)
    inputfile = args[0]
    outputfile = args[1]
    
    try:
        f = open(inputfile, 'r')
    except IOError:
        sys.stderr.write("File " + inputfile + " does not exist\n")
        sys.exit(2)
    try:
        pdb = open(outputfile, 'w')
    except IOError:
        sys.stderr.write("File " + outputfile + " could not be opened for " +
                         "writing")
    lines = f.readlines()
    f.close()

    i = 1
    for line in lines:
        coords = map(float, line.split(','))
        if len(coords) != 3:
            sys.stderr.write("Line skipped, coordinates comma-separated " +
                             "not found")
            sys.stderr.write(line)
        pdb.write( "ATOM     {0:2d}  BOX BOX     1       ".format(i) +
                   "{0:.3f}   {1:.3f}   {2:.3f}\n".format(*coords))
        i = i+1

    sys.stderr.write("CSV={} ".format(inputfile) +
                     "to PDB={} [ SUCCESS ]\n".format(outputfile))

if __name__ == "__main__":
    main(sys.argv[1:])

#for (i=0;i<dots;i++)
#{
#   fprintf(fp, "ATOM     %2d  BOX BOX     1      %2d.000  %2d.000  %2d.0000\n",i+1,HamWalk[i][0],HamWalk[i][1],HamWalk[i][2]);
#}		
#
#for (i=0;i<dots-1;i++)
#{
#   fprintf(fp, "CONECT   %2d   %2d           \n",i+1,i+2);
#}