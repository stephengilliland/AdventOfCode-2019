import math

input = [3,8,1001,8,10,8,105,1,0,0,21,46,67,88,101,126,207,288,369,450,99999,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,102,3,9,9,1001,9,4,9,4,9,99,3,9,102,3,9,9,1001,9,3,9,1002,9,2,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99
]

skip = 0
opcode = 0
a = "a"
par1mode = 0
par2mode = 0
par3mode = 0
param1 = 0
param2 = 0
param3 = 0
var = ""
code = []
temp = 0 
skip = 3
x = 0
pointer = -1

numbers = [1, 0, 1, 2, 3]
inputnum = 1
output = 0
input = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

"""
810828
86312
218702
[0, 4, 1, 2, 3] - 810088
[2, 1, 3, 4, 0] - 737102
[0, 3, 1, 4, 2] - 810716
[4, 3, 1, 0, 2] - 229740
[1, 2, 4, 3, 0] - 218582
[1, 0, 1, 2, 3] - 246568


"""
biggestout = 0
numoptions = 0
temp = ""
options = []
e = 0
currstr = []
while e < 43210:
    temp = str(e)
    currstr = list(temp)
    while len(currstr) < 5:
        currstr.insert(0, "0")
    print(currstr)
    if currstr[0] != currstr[1] and currstr[0] != currstr[2] and currstr[0] != currstr[3] and currstr[0] != currstr[4]:
        if currstr[1] != currstr[2] and currstr[1] != currstr[3] and currstr[1] != currstr[4]:
            if currstr[2] != currstr[3] and currstr[2] != currstr[4]:
                if currstr[3] != currstr[4]:
                    if int(currstr[0]) < 5 and int(currstr[1]) < 5 and int(currstr[2]) < 5 and int(currstr[3]) < 5 and int(currstr[4]) < 5:
                        options.append(currstr)
                        numoptions += 1
    e += 1

print(numoptions)
print(options) 


for w in range(119):
    output = 0
    numbers = options[w]
    for r in range(5):
        numbers[r] = int(numbers[r])

    for s in range(5):
        skip = 0
        opcode = 0
        a = "a"
        par1mode = 0
        par2mode = 0
        par3mode = 0
        param1 = 0
        param2 = 0
        param3 = 0
        var = ""
        code = []
        temp = 0 
        skip = 3
        x = 0
        pointer = -1
        inputnum = 1
        input = [3,8,1001,8,10,8,105,1,0,0,21,46,67,88,101,126,207,288,369,450,99999,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,102,3,9,9,1001,9,4,9,4,9,99,3,9,102,3,9,9,1001,9,3,9,1002,9,2,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99
        ]
        #print("Goin Again")
        while x < len(input)-3:

            #print("x = ", x)
            code = []
            var = str(input[x])

            for m in range(len(var)):
                code.append(var[m])

            if len(code) == 1:
                a = code[0]
            else:
                while len(code) <= 4:
                    code.insert(0, "0")

                a = code[4]
                if a[0] == "0" and len(a) > 1:
                    a = a[1]
            
            if len(code) == 1:
                opcode = int(a)
                #print("Opcode = ", opcode)
                par1mode = 0
                par2mode = 0
                par3mode = 0
            elif len(code) == 5:
                opcode = int(a)
                par1mode = int(code[2])
                par2mode = int(code[1])
                par3mode = int(code[0])

            if par1mode == 0:
                param1 = input[x+1]
            elif par1mode == 1:
                param1 = x+1
            else:
                print("Fail")
                print(x)
                print(code)

            if par2mode == 0:
                param2 = input[x+2]
            elif par2mode == 1:
                param2 = x+2
            else:
                print("Fail")
                print(x)
                print(code)

            if par3mode == 0:
                param3 = input[x+3]
            elif par3mode == 1:
                param3 = x+3
            else:
                print("Fail")
                print(x)
                print(code)

            if opcode == 99:
                temp = 1

            elif opcode == 1 and temp != 1:
                input[param3] = input[param1] + input[param2]
                skip = 4

            elif opcode == 2 and temp != 1:
                input[param3] = input[param1] * input[param2]
                skip = 4

            elif opcode == 3 and temp != 1:
                if inputnum == 1:
                    input[param1] = numbers[s]
                    #print(inputnum)
                    inputnum += 1
                    #print("input = ", input[x], "Number = ", numbers[s])
                elif inputnum == 2:
                    input[param1] = output
                    #print(inputnum)
                    inputnum = 1
                    #print("input = ", input[x])
                
                skip = 2

            elif opcode == 4 and temp != 1:
                print("Output = ", input[param1])
                output = input[param1]
                if output > biggestout:
                    biggestout = output
                skip = 2

            elif opcode == 5 and temp != 1:
                if input[param1] > 0:
                    pointer = input[param2]
                else:
                    skip = 3

            elif opcode == 6 and temp != 1:
                if input[param1] == 0:
                    pointer = input[param2]
                else:
                    skip = 3

            elif opcode == 7 and temp != 1:
                if input[param1] < input[param2]:
                    input[param3] = 1
                elif input[param1] >= input[param2]:
                    input[param3] = 0
                skip = 4

            elif opcode == 8 and temp != 1:
                if input[param1] == input[param2]:
                    input[param3] = 1
                elif input[param1] != input[param2]:
                    input[param3] = 0
                skip = 4

            else:
                temp = 1
            

            x += skip
            if pointer != -1:
                x = pointer
                pointer = -1
            
            skip = 0

            if temp == 1:
                break
        inputnum = 1
print(biggestout)
