import getopt
import sys
from func import *

argumentList = sys.argv[1:]

options = "hmop:c"

# Long options
long_options = ["Help", "My_file", "Output=", "Path=", "compress"]

path = None
compress = False

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print("Displaying Help")
            
        elif currentArgument in ("-m", "--My_file"):
            print("Displaying file_name:", sys.argv[0])
            
        elif currentArgument in ("-o", "--Output"):
            print("Enabling special output mode (%s)" % (currentValue))
        
        elif currentArgument in ("-p", "--Path"):
            path = currentValue
            #print("Path set to %s" % (path))

        elif currentArgument in ("-c", "--compress"):
            compress = True

        else:
            assert False, "Unhandled Option"

    if path is not None:
        file = convert_cbz_to_pdf(path)
        if compress:
            reduce_pdf_size(file)

except getopt.error as err:
    print(str(err))
