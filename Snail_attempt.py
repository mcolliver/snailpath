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
