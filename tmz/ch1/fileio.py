f = open("inputFile.txt", "r")
# print(f.read())
newfile = open("newfile.txt", "w")
newfile2 = open("newfile2.txt", "w")

count = 0
for line in f:
    # print(str(count) + " " + line)
    line_split = line.split()
    if line_split[2] == "P":
        newfile.write(line)
    else:
        newfile2.write(line)

        count = count  + 1

print(count)
f.close()
newfile.close()       
   
