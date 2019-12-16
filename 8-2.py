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

"""
0 = Black
1 = White
2 = Transparent
"""
outputLine = ["" for x in range(150)]
currChar = "2"
m = 0
done = False
two = False
twos = 0
for x in range(100):  
    while done == False and two == False:
        print[line[x][m]]
        if line[x][m] == "1":
            outputLine[m] = "1"
            done = True
        if line[x][m] == "0":
            outputLine[m] = "0"
            done = True
        if line[x][m] == "2":
            outputLine[m] = "2"
            twos += 1
            m += 1
        if twos == 150 or m == 150:
            two = True
        
    m = 0
    two = False
    done = False

print(outputLine)
print(line[0])
        

    


    



