lenlayer = 150
inputFile = open('8-1-in.txt', 'r')
inp = []
currline = ""
count = 0
count = len(open('8-1-in.txt').readlines(  ))
print(count)
line = ["" for x in range(count)]
zeroctr = 0
onectr = 0
twoctr = 0

lineleastzeros = ""
leastzeros = 150

for x in range(count):
    line[x] = inputFile.readline().strip()
    currLine = line[x]
    print(x)

print(line)
lineList = []

for x in range(count):
    currLine = line[x]  
    print(currLine)
    for y in range(150):
        if currLine[y] == "0":
            zeroctr += 1
    if zeroctr < leastzeros:
        lineleastzeros = currLine
        print(zeroctr)
        leastzeros = zeroctr
    zeroctr = 0


print("line = ", lineleastzeros)

for x in range(150):
    if lineleastzeros[x] == "1":
        onectr += 1
    elif lineleastzeros[x] == "2":
        twoctr += 1
answer = 0
answer = onectr * twoctr
print(answer)

    



