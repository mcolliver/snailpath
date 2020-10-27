def snail(snail_map):
    lenofmap = len(snail_map)
    snailrow = 1
    overall = []
    final = []
    for character in snail_map[0]:
        overall.append(character)
        print(overall)
        
    while snailrow < lenofmap:
        overall.append(snail_map[snailrow][-1])
        print(overall)
        snailrow += 1
        
    if snailrow == lenofmap:
        for character in snail_map[(snailrow-1)]:
            final.append(character)
        overall.append(final[-2::-1])
        print(overall)
    pass
 
    
 def snail(snail_map):
   
    length = len(snail_map)
    print('SN',snail_map,'length',length)
    if len(snail_map)>1 :
        snaill = snail_map[0]
        snail_map.pop(0)
        for i in range(1,length-1):
            snaill.append( snail_map[i-1][length-1])
            snail_map[i-1].pop(length-1)
        print(snail_map)
        for i in range(length-1,-1,-1):
            print(length-2,i)
            snaill.append( snail_map[length-2][i])
        snail_map.pop(length-2)
        for i in range(length-2,1,-1):
            snaill.append( snail_map[i-1][0])
            snail_map[i-1].pop(0)
            
        return snaill + snail(snail_map)
    elif len(snail_map)==1:
        return snail_map[0]
    else:
        return [] 
        
