import sys


file1 =open(sys.argv[1],"rb").read()
file2 =open(sys.argv[2],"rb").read()

inp = zip(file1,file2)
out=""
for a,b in inp:
    if a^b == 0:
        out+="0"
    else:
        out+="1"

print(out)