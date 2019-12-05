count = 0
inc = 0
match = 0

for x in range(240298, 784956):
    curr = str(x)
    inc = 0
    match = 0
    for y in range(len(curr)-1):
        
        if curr[y] == curr[y+1]:
            
            if y == 0 and curr[y] != curr[y+2]:
                match = 1
                
            if y <= 3 and y > 0:
                if curr[y+2] != curr[y] and curr[y-1] != curr[y]:
                    match = 1
                    
            if y == 4:
                if curr[y-1] != curr[y]:
                    match = 1
            
        
        if curr[y] <= curr[y+1]:
            inc += 1

    if match == 1 and inc == 5:
        count += 1

    
print(count)
