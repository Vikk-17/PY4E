fhand = open('./files/mbox-short.txt')
count = 0
# for line in fhand:
#     count = count + 1
# print(f"Total line: {count}")

# inp = fhand.read()
# print(len(inp))
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
# print(fhand)