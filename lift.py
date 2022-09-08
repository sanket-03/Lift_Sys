#elevator system logic


# 1 : up
# 0 : down

#consider the redButtons in timely order
#Before you called lift, all the red buttons were pressed accodingly up or down

#consider lift takes 5 sec to go to neighbouring floor
#consider 10 sec the lift stops at one floor

def liftSys(floors, liftLoc, urLoc, urMove, redButtons, direc):

    if liftLoc > floors or urLoc > floors:
        print("Wrong Data !: no such locn exist")
        return
    
    if len(redButtons) != len(direc): 
        print("Wrong Data ! floor-direc mismatch")
        return   
        
    for i in redButtons:
        if i > floors:
            print("Wrong Data !")
            return

    liftPath = []
    for i in range(len(redButtons)):
        if redButtons[i] == 0 and direc[i] == 0:
            print("Wrong data ! lift cant move that way, G")
            return
            
        if redButtons[i] == floors and direc[i] == 1:
            print("Wrong data ! lift cant move that way, Top")
            return
            
        path = [redButtons[i], direc[i]]
        liftPath.append(path)
               
    if urLoc == urMove:
        return [0, 0]
    
    urDir = 0 if urMove < urLoc else 1
    
    #liftDir = 0 if liftLoc > redButtons[0] else 1 
    #liftPath.insert(0, [liftLoc, liftDir])

    liftPath.append([urLoc, urDir])
    liftPath.append([-1, -1])
        
    #print(liftPath)
    time2Come = 0
    time2Reach = 10
    time = [time2Come, time2Reach]
    t_transit = 5
    t_stop = 10
    #n = len(liftPath)
    
    while len(liftPath) > 1:
        if liftPath[0][0] > liftLoc:
            liftDir = 1
            
        elif liftPath[0][0] == liftLoc:
            liftPath.pop(0)
            continue
            
        else:
            liftDir = 0

        
        if not liftDir:
            
            if urLoc > liftLoc:
                time2Come += abs(liftLoc - liftPath[0][0])*5
                j = 1
                while liftPath[j][0] != -1:
                    if liftPath[j][0] >= liftPath[0][0] and liftPath[j][0] <= liftLoc:                
                        time2Come += 10
                        liftPath.pop(j)
                        continue
                    j += 1
                 

                liftLoc = liftPath[0][0]
                liftPath.pop(0)
                continue
            
            else:
                time2Come += abs(liftLoc - urLoc)*5
                j = 1
                while liftPath[j][0] != -1:
                    if liftPath[j][0] >= urLoc and liftPath[j][0] < liftLoc:
                        time2Come += 10
                        if liftPath[j][0] == urLoc:
                            time2Come -= 10
                        liftPath.pop(j)
                        continue

                    j += 1
                liftLoc = urLoc
                liftPath.pop(0)
                liftPath.insert(-1, [urMove, None])                
                break
        
        if liftDir:
            if urLoc < liftLoc:
                time2Come += abs(liftLoc - liftPath[0][0])*5
                j = 1
                while liftPath[j][0] != -1:
                    if liftPath[j][0] <= liftPath[0][0] and liftPath[j][0] >= liftLoc:                
                        time2Come += 10
                        liftPath.pop(j)
                        continue
                    j += 1
                liftLoc = liftPath[0][0]
                liftPath.pop(0)
                continue
            
            else:
                time2Come += abs(liftLoc - urLoc)*5
                j = 1
                while liftPath[j][0] != -1:
                    if liftPath[j][0] <= urLoc and liftPath[j][0] > liftLoc:
                        time2Come += 10
                        if liftPath[j][0] == urLoc:
                            time2Come -= 10
                        liftPath.pop(j)
                        continue
                                               
                        
                    j += 1
                liftLoc = urLoc
                liftPath.pop(0)
                liftPath.insert(-1, [urMove, None])                 
                break
        
    print(liftPath)
    print(liftLoc)
    
    while len(liftPath) > 1:
        if liftPath[0][0] > liftLoc:
            liftDir = 1
            
        elif liftPath[0][0] == liftLoc:
            liftPath.pop(0)
            continue
            
        else:
            liftDir = 0
        
        if not liftDir:
            if urMove > liftLoc:
                time2Reach += abs(liftLoc - liftPath[0][0])*5
                j = 1
                
                '''
                #put here range till -1 and you can moderate real time data too
                '''
                while liftPath[j][1] != None:
                    if liftPath[j][0] >= liftPath[0][0] and liftPath[j][0] <= liftLoc:                
                        time2Reach += 10
                        liftPath.pop(j)
                        continue
                    j += 1
                liftLoc = liftPath[0][0]
                liftPath.pop(0)
                continue
            
            else:
                time2Reach += abs(liftLoc - urMove)*5
                j = 1
                if len(liftPath) > 2:
                    while liftPath[j][1] != None:
                        if liftPath[j][0] >= urMove and liftPath[j][0] < liftLoc:                      
                            if liftPath[j][0] == urMove:
                                liftPath.pop(j)
                                continue                        
                            time2Reach += 10
                            liftPath.pop(j)
                            continue
                        j += 1
                    liftLoc = urMove
                    liftPath.pop(0)                
                    break
                else:
                    break
        
        if liftDir:
            if urMove < liftLoc:
                time2Reach += abs(liftLoc - liftPath[0][0])*5
                j = 1
                while liftPath[j][1] != None:
                    if liftPath[j][0] <= liftPath[0][0] and liftPath[j][0] >= liftLoc:                
                        time2Reach += 10
                        liftPath.pop(j)
                        continue
                    j += 1
                liftLoc = liftPath[0][0]
                liftPath.pop(0)
                continue
            
            else:
                time2Reach += abs(liftLoc - urMove)*5
                j = 1
                if len(liftPath) > 2:
                    while liftPath[j][1] != None:
                        if liftPath[j][0] <= urMove and liftPath[j][0] > liftLoc:                
                            if liftPath[j][0] == urMove:
                                liftPath.pop(j)
                                continue                        
                            time2Reach += 10
                            liftPath.pop(j)
                            continue
                        j += 1
                    liftLoc = urMove
                    liftPath.pop(0)            
                    break
                else:
                    break
                
    print(liftPath)
    print(liftLoc)
    
    '''
    while len(liftPath) > 1:
        if liftPath[0][0] > liftLoc:
            liftDir = 1
        elif liftPath[0][0] == liftLoc:
            liftPath.pop(0)
            continue
        else:
            liftDir = 0
        
        if not liftDir:
            if urLoc > liftLoc:
                time2Come += abs(liftLoc - liftPath[0][0])*5
                j = 1
                while liftPath[j][0] != -1:
                    if liftPath[j][0] >= liftPath[i][0] and liftPath[j][0] <= liftLoc:                
                        time2Come += 10
                        liftPath.pop(j)
                        continue
                    j += 1
                        
                liftLoc = liftPath[0][0]
                continue
            else:
                time2Come += abs(liftLoc - urLoc)*5
                i = 0
                for j in range(i+1, len(liftPath)):
                    if liftPath[j][0] > urLoc and liftPath[j][0] < liftLoc:
                        time2Come += 10   
                liftPath.pop(-2)
                liftPath.insert(-1, [urMove, None]) 
                break
        
        if liftDir:
            if urLoc < liftLoc:
                time2Come += abs(liftLoc - liftPath[0][0])*5
                j = 1
                while liftPath[j][0] != -1:
                    if liftPath[j][0] <= liftPath[i][0] and liftPath[j][0] >= liftLoc:                
                        time2Come += 10
                        liftPath.pop(j)
                        continue
                    j += 1
                        
                liftLoc = liftPath[0][0]
                continue
            else:
                time2Come += abs(liftLoc - urLoc)*5
                i = 0
                for j in range(i+1, len(liftPath)):
                    if liftPath[j][0] < urLoc and liftPath[j][0] > liftLoc:
                        time2Come += 10    
                liftPath.pop(-2)
                liftPath.insert(-1, [urMove, None]) 
                break
    
    '''
    '''
    if (not liftPath[0][1] and liftPath[0][0] >= urLoc) or (liftPath[0][1] and liftPath[0][0] <= urLoc):
            path_length = abs(liftPath[0][0] - urLoc)
            time2Come += path_length*t_transit

            if liftPath[0][1] == 0:
                for j in redButtons:
                    if j > urLoc and j < liftPath[0][0]:
                        time2Come += t_stop

            if liftPath[0][1] == 1:
                for j in redButtons:
                    if j < urLoc and j > liftPath[0][0]:
                        time2Come += t_stop
        
    if (not liftPath[0][1] and liftPath[0][0] <= urLoc) or (liftPath[0][1] and liftPath[0][0] >= urLoc):
            path_length1 = abs(liftPath[0][0] - urLoc)
            path_length2 = abs(liftPath[0][0] - liftPath[1][0])*2
            time2Come += path_length1*t_transit
            time2Come += path_length2*t_transit
            
            if liftPath[0][1] == 0:
                for j in redButtons:
                    if j >= liftPath[1][0] and j < urLoc:
                        if j == liftPath[0][0]:
                            if count:
                                time2Come += t_stop
                            count += 1
                        time2Come += t_stop    
                        
                        

            if liftPath[0][1] == 1:
                for j in redButtons:
                    if j <= liftPath[1][0] and j > urLoc:
                        if j == liftPath[0][0]:
                            if count:
                                time2Come += t_stop
                            count += 1
                        time2Come += t_stop     
    '''
    return time2Come, time2Reach
    
    
floors = int(input('total floors: '))
liftLoc = int(input('Current lift locn: '))
urLoc = int(input('You are at: '))
urMove = int(input('You want to go to: '))

redButtons = list(map(int, input().split()))
direc = list(map(int, input().split()))

a = liftSys(floors, liftLoc, urLoc, urMove, redButtons, direc)
print('You have to wait for {} seconds and you will reach floor #{} in approx {} seconds'.format(a[0], urMove, a[0]+a[1]))

#arrange ascending liftPath to cover double pressed floors 





