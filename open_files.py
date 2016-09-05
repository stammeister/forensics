print "Type the file you want to open:"
file_open = raw_input(">>>>")

txt_content = open(file_open)

print txt_content.read()
