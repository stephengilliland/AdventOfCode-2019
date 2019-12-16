pos1 = [5,13,-3]
pos2 = [18,-7,13]
pos3 = [16,3,4]
pos4 = [0,8,8]

initial1 = [5,13,-3]
initial2 = [18,-7,13]
initial3 = [16,3,4]
initial4 = [0,8,8]

vel1 = [0,0,0]
vel2 = [0,0,0]
vel3 = [0,0,0]
vel4 = [0,0,0]

matching1 = []
matching2 = []
matching3 = []
matching4 = []

add = 0

# Given in X, Y, Z Order
for y in range(1000000):

    for x in range(3):
        
        if pos1[x] < pos2[x]:
            add += 1
        if pos1[x] < pos3[x]:
            add += 1
        if pos1[x] < pos4[x]:
            add += 1

        if pos1[x] > pos2[x]:
            add -= 1
        if pos1[x] > pos3[x]:
            add -= 1
        if pos1[x] > pos4[x]:
            add -= 1
            
        vel1[x] += add
        add = 0

        if pos2[x] < pos1[x]:
            add += 1
        if pos2[x] < pos3[x]:
            add += 1
        if pos2[x] < pos4[x]:
            add += 1

        if pos2[x] > pos1[x]:
            add -= 1
        if pos2[x] > pos3[x]:
            add -= 1
        if pos2[x] > pos4[x]:
            add -= 1

        vel2[x] += add
        add = 0

        if pos3[x] < pos1[x]:
            add += 1
        if pos3[x] < pos2[x]:
            add += 1
        if pos3[x] < pos4[x]:
            add += 1

        if pos3[x] > pos1[x]:
            add -= 1
        if pos3[x] > pos2[x]:
            add -= 1
        if pos3[x] > pos4[x]:
            add -= 1

        vel3[x] += add
        add = 0

        if pos4[x] < pos1[x]:
            add += 1
        if pos4[x] < pos2[x]:
            add += 1
        if pos4[x] < pos3[x]:
            add += 1

        if pos4[x] > pos1[x]:
            add -= 1
        if pos4[x] > pos2[x]:
            add -= 1
        if pos4[x] > pos3[x]:
            add -= 1
            
        vel4[x] += add
        add = 0


    for x in range(3):
        
        pos1[x] += vel1[x]
        pos2[x] += vel2[x]
        pos3[x] += vel3[x]
        pos4[x] += vel4[x]

    if pos1[0] == initial1[0] and vel1[0] == 0:
        matching1.append(y)
    if pos2[0] == initial2[0] and vel2[0] == 0:
        matching2.append(y)
    if pos3[0] == initial3[0] and vel3[0] == 0:
        matching3.append(y)
    if pos4[0] == initial4[0] and vel4[0] == 0:
        matching4.append(y)


power = (abs(pos1[0]) + abs(pos1[1]) + abs(pos1[2]))*(abs(vel1[0]) + abs(vel1[1]) + abs(vel1[2])) + (abs(pos2[0]) + abs(pos2[1]) + abs(pos2[2]))*(abs(vel2[0]) + abs(vel2[1]) + abs(vel2[2])) + (abs(pos3[0]) + abs(pos3[1]) + abs(pos3[2]))*(abs(vel3[0]) + abs(vel3[1]) + abs(vel3[2])) + (abs(pos4[0]) + abs(pos4[1]) + abs(pos4[2]))*(abs(vel4[0]) + abs(vel4[1]) + abs(vel4[2]))

print("Match 1 = ", matching1)
print("Match 2 = ", matching2)
print("Match 3 = ", matching3)
print("Match 4 = ", matching4)
    
