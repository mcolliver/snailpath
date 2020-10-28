def snail(snail_map):
   
    length = len(snail_map)
    
    if len(snail_map) > 1 :  # top
        snailPath = snail_map[0]
        snail_map.pop(0) # removes top list
        length -= 1
        
        for i in range(1,length):  #down
            snailPath.append( snail_map[i-1][length])
            snail_map[i-1].pop(length) # removes rightermost list as moves down
        
        for i in range(length,-1,-1):  # back across
            snailPath.append( snail_map[length-1][i] )
        snail_map.pop(length-1) # removes bottom list
        length -=1
    
        for i in range(length,1,-1):  #up
            snailPath.append( snail_map[i-1][0] )
            snail_map[i-1].pop(0) # popps leftermost list as moves up
            
        return snailPath + snail(snail_map) # calls itself again, but with outermost 'path' of trail popped
    
    elif len(snail_map)==1:
      
      return snail_map[0]
    
    else:
        return [] 
