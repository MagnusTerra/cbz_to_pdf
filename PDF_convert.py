import getopt
import sys
from func import *

argumentList = sys.argv[1:]

options = "hmop:c:t:f:n:"

# Long options
long_options = ["Help", "My_file", "Output=", "Path=", "compress", "to_img", "format=", "name=", "ShowLog"]

path = None
compress = False
to_img = None
show_log = None
format = None
name = None

try:
    if argumentList == []:
        main()
        
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

        elif currentArgument in ("-t", "--to_img"):
            to_img = True

        elif currentArgument in ("-f", "--format"):
            format = currentValue
            #print("Format set to %s" % (format))

        elif currentArgument in ("-n", "--name"):
            name = currentValue
            #print("Name set to %s" % (name))
        
        elif currentArgument in ("--ShowLog"):
            show_log = True

        else:
            assert False, "Unhandled Option"
        

    if path is not None:
        if to_img:
            pdf_to_img(pdf_file=path, output_folder=name,show_mess=show_log,format=format)



except getopt.error as err:
    print(str(err))
