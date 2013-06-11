# Note, example is modified to allow execution without errors.
# Make sure there is a file called 'somefile.txt' in the same
# directory as this Python script.


# Opening the text file with the 'r' option,
# which only allows reading capability
f = open('somefile.txt', 'r')

# Parsing the file and splitting each line,
# which creates a list where each element of
# it is one line
alist = f.readlines()

# Closing file
f.close()

# Noted changed from example in book
newdata = alist.append(1)

# After a few operations, we open a new text file
# to write the data with the 'w' option. If there
# was data already existing in the file, it will be overwritten.
f = open('newtextfile.txt', 'w')

# Writing data to file
f.writelines(newdata)

# Closing file
f.close()
