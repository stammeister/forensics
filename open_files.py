from sys import argv

script,filename = argv

open_file=open(filename)

print "so you want to open %r"  %filename

print open_file.read()

print "Type the filename again"

type_file=raw_input("")

open_type=open(type_file)

print open_type.read()
