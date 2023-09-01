# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:

fhand = open("mx.txt")
for line in fhand:
    capital = line.strip().upper()
    print(capital)