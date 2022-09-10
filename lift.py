#Basic Elevator System

'''

# Terminology

1 : up
0 : down

# Input Variables

floors [int]  : total number of floors in the building (Do not count ground floor)
liftLoc [int] : current instantaneous stationery location of lift in terms of floor number
urLoc [int] : user's current floor
urMove [int] : user's destination floor
redButtons [list] : calls made to lift from various floors in timely arranged order 
direc [list] : represents respective call made from the floors in {redButtons} list (Use Terminology)

# Note: 

- It is considered that when user called the lift all the floors of {redButtons} has already called the lift
- consider lift takes 5 sec to move to its neighbouring floor
- consider 10 sec is the halt time of lift at called floor, if single floor calls lift twice it will stay there for 20 sec

'''

# defining func named liftSys 

def liftSys(floors, liftLoc, urLoc, urMove, redButtons, direc):

    # Unacceptable cases
    
    if 0 < liftLoc > floors or 0 < urLoc > floors or 0 < urMove > floors or floors <= 0:   
        print("Wrong Data !: no such locn exist")   
        return
    
    # A valid call has both direction and floor number
    
    if len(redButtons) != len(direc):                       
        print("Wrong Data ! floor-direc mismatch")
        return   
    
    # Lift can only be called from 0th or ground floor to the top floor
       
    for i in redButtons:        
        if i > floors:
            print("Wrong Data !")                           
            return

    liftPath = []   # Variable lift path will show us real time location of lift 
                    # liftPath [list of lists] : [ ..., [ redButtons[i], direc[i] ], ... ]  
                    
    for i in range(len(redButtons)):
    
        # One can only move up from ground floor
        
        if redButtons[i] == 0 and direc[i] == 0:           
            print("Wrong data ! lift cant move that way, G")
            return
    
        # One can only move down from top floor
    
        if redButtons[i] == floors and direc[i] == 1:       
            print("Wrong data ! lift cant move that way, Top")
            return
            
        # Temporary variable for lists of liftPath variable 
        
        path = [redButtons[i], direc[i]]  
        liftPath.append(path)
    
    # Location same as Destination 
      
    if urLoc == urMove:
        return [0, 0]
    
    # Gives the direction of user's upcoming movement (According to Terminology)
    
    urDir = 0 if urMove < urLoc else 1
    
    # Appending user's call to lift

    liftPath.append([urLoc, urDir])
    
    # Setting up a marker/flag as [-1, -1] for iteration limit
    
    liftPath.append([-1, -1])
    
    '''
    # New Variables
    
        # Output Variables 
        
        time2Come [int] : the approx time of lift arrival to user's floor or {urLoc}
        time2Reach [int] : the approx time to reach the destination floor or {urMove}
        
        # Note
        - Output will acknowledge the user about the probable arrival time of lift i.e. {time2Come} and how much total time will it take to reach his destination floor i.e. {time2Come + time2Reach}
    
        # Other Variables
        
        t_transit : time taken by lift to move to it's just neighbouring floor [predefined to 5 sec]
        t_stop : halt timing of lift [predefined to 10 sec] 
    
    '''
    
    
    time2Come = 0
    time2Reach = 0
    
    t_transit = 5
    t_stop = 10

    #First While Loop
    '''
        The While Loop will iterate over liftPath to increment the time2Come values accordingly 
    '''

    while len(liftPath) > 1:
    
        # Series of If - Elif - Else will define the lift direction (According to the Terminology) on each case of lift movement 
        
        if liftPath[0][0] > liftLoc:
            liftDir = 1
            
        elif liftPath[0][0] == liftLoc:
            liftPath.pop(0)
            continue
            
        else:
            liftDir = 0
        
        # Considering the case when lift is moving down
        
        if not liftDir:
        
            # The case when lift is moving down but user's location is either above the lift's location or below the next location
            
            if urLoc > liftLoc or urLoc < liftPath[0][0]:
            
                # As our next location will be now the first element of {liftPath}, time it will take to reach there in ideal case can be calculated by multiplying differnce between the floors with {t_transit}
                
                time2Come += abs(liftLoc - liftPath[0][0])*t_transit
                
                # Another While Loop
                '''
                    The loop will see if there are any other floors who called the lift in between the lift's journey
                '''
                
                j = 0
                nextLoc = liftPath[0][0] # To maintain the value of next location it is stored in {nextLoc}
                while liftPath[j][0] != -1:  # Flag used to mark end of list
                    if liftPath[j][0] >= nextLoc and liftPath[j][0] <= liftLoc:                
                        time2Come += t_stop  # At each stop halt time is {t_stop}
                        liftPath.pop(j)
                        continue
                    j += 1
                 
                # moving on for next iteration in external while loop
                
                liftLoc = nextLoc
                continue
            
            # The case when lift is moving down and user's location is also there
            
            else:
                
                # Ideal case when no floor in between current journey
                
                time2Come += abs(liftLoc - urLoc)*t_transit
                
                # Another While Loop
                '''
                    The loop will see if there are any other floors who called the lift in between the lift's journey
                '''
                    
                j = 0
                while liftPath[j][0] != -1: # List end flag
                    if liftPath[j][0] >= urLoc and liftPath[j][0] <= liftLoc:
                        
                        # Consider if lift is called twice from user's floor (both up(1) and down(0) movement call)
                        
                        if liftPath[j][0] == urLoc: 
                            time2Reach += t_stop  # The time of halt there will not affect {time2Come} but {time2Reach} is affected
                            liftPath.pop(j)
                            continue
                    
                        time2Come += t_stop                          
                        liftPath.pop(j)
                        continue    
                    j += 1
 
                # moving out from the main loop as lift has reached user's floor also appending the destiny floor in {listPath}
                
                liftLoc = urLoc
                liftPath.insert(-1, [urMove, None])                
                break
        
        # Considering the case when lift is moving up
        
        if liftDir:
        
            # The case when lift is moving up but user's location is either below the lift's location or above the next location   
            
            if urLoc < liftLoc or urLoc > liftPath[0][0]:
            
            # As our next location will be now the first element of {liftPath}, time it will take to reach there in ideal case can be calculated by multiplying differnce between the floors with {t_transit}

                time2Come += abs(liftLoc - liftPath[0][0])*t_transit
                
                # Another While Loop
                '''
                    The loop will see if there are any other floors who called the lift in between the lift's journey
                '''
                
                j = 0
                nextLoc = liftPath[0][0]
                while liftPath[j][0] != -1:
                    if liftPath[j][0] <= nextLoc and liftPath[j][0] >= liftLoc:                
                        time2Come += t_stop
                        liftPath.pop(j)
                        continue
                    j += 1

                # moving on for next iteration in external while loop

                liftLoc = nextLoc
                continue
       
            # The case when lift is moving up and user's location is also there
            
            else:

                # Ideal case when no floor in between current journey
                
                time2Come += abs(liftLoc - urLoc)*t_transit
                
                # Another While Loop
                '''
                    The loop will see if there are any other floors who called the lift in between the lift's journey
                '''
                    
                j = 0
                while liftPath[j][0] != -1:
                    if liftPath[j][0] <= urLoc and liftPath[j][0] >= liftLoc:
                        
                        if liftPath[j][0] == urLoc:
                            time2Reach += t_stop
                            liftPath.pop(j)
                            continue
                            
                        time2Come += t_stop                            
                        liftPath.pop(j)
                        continue    
                    j += 1
                    
                # moving out from the main loop as lift has reached user's floor and appending the destiny floor in {liftPath}
                
                liftLoc = urLoc
                liftPath.insert(-1, [urMove, None])                 
                break

    #Second While Loop
    '''
        The While Loop will iterate over liftPath to increment the time2Reach values accordingly 
        Its similar to above loop as now the current instantaneous stationery location of lift is {urLoc} or user's location and destiny is {urMove}
    '''   

    
    while len(liftPath) > 1:
    
        # Series of If - Elif - Else will define the lift direction (According to the Terminology) on each case of lift movement     
    
        if liftPath[0][0] > liftLoc:
            liftDir = 1
            
        elif liftPath[0][0] == liftLoc:
            liftPath.pop(0)
            continue
            
        else:
            liftDir = 0
        
        # Considering the case when lift is moving down        
        
        if not liftDir:
        
            # The case when lift is moving down but either user wants to go up or the lift is not going that up
            
            if urMove > liftLoc or urMove < liftPath[0][0]:
            
                # As our next location will be now the first element of {liftPath}, time it will take to reach there in ideal case can be calculated by multiplying differnce between the floors with {t_transit}
                
                time2Reach += abs(liftLoc - liftPath[0][0])*t_transit
                
                # Another While Loop
                '''
                    The loop will see if there are any other floors who called the lift in between the lift's journey
                '''
                
                j = 0
                nextLoc = liftPath[0][0] # To maintain the value of next location it is stored in {nextLoc}
                '''
                Here in the while loop instead of the flag i.e. [-1, -1] which we set up in {liftPath} we are using another flag i.e. as our destiny is {urMove} we have no direction onwards to go in lift so the direction is intentionally set up {None} hence we are using it as a flag here
                Although, if we are considering real time data input we have to use [-1, -1] term as a flag
                '''
                while liftPath[j][1] != None:
                    if liftPath[j][0] >= nextLoc and liftPath[j][0] <= liftLoc:                
                        time2Reach += t_stop
                        liftPath.pop(j)
                        continue
                    j += 1
                
                # moving on for next iteration in external while loop
                
                liftLoc = nextLoc
                continue
                
            # The case when lift is moving down and user destiny is also there 
            
            else:
            
                # Ideal case when no floor in between current journey
            
                time2Reach += abs(liftLoc - urMove)*t_transit
                
                # Another While Loop
                
                j = 0
                
                # The below condition is used because of the existence of pre-set marker flag [-1, -1] in liftPath
                
                if len(liftPath) > 2:
                    while liftPath[j][1] != None:
                        if liftPath[j][0] >= urMove and liftPath[j][0] <= liftLoc:    
                        
                            if liftPath[j][0] == urMove:
                            
                                # It is not required to add {t_stop} now, as the user has already reached the destination
                            
                                liftPath.pop(j)
                                continue                     
                                
                            time2Reach += t_stop
                            liftPath.pop(j)
                            continue
                        j += 1
                    
                    # moving out from the main loop as lift has reached user's destiny floor
                    
                    liftLoc = urMove
                    liftPath.pop(0)                
                    break
                else:
                    break
        
        # Considering the case when lift is moving up
        
        if liftDir:
        
            # The case when lift is moving up but user's destination floor location is either below or above than the next location
            
            if urMove < liftLoc or urMove > liftPath[0][0]:
                time2Reach += abs(liftLoc - liftPath[0][0])*t_transit
              
                #Another While Loop
                
                j = 0
                nextLoc = liftPath[0][0]
                while liftPath[j][1] != None:
                    if liftPath[j][0] <= nextLoc and liftPath[j][0] >= liftLoc:                
                        time2Reach += t_stop
                        liftPath.pop(j)
                        continue
                    j += 1
                
                # moving on for next iteration in external while loop
                
                liftLoc = nextLoc
                continue
            
            # The case when lift is moving up and user's destiny is also there
            
            else:
            
                # Ideal case when no floor in between current journey
            
                time2Reach += abs(liftLoc - urMove)*t_transit

                # Another While Loop
                
                j = 0
                if len(liftPath) > 2:
                    while liftPath[j][1] != None:
                        if liftPath[j][0] <= urMove and liftPath[j][0] >= liftLoc:
                        
                            if liftPath[j][0] == urMove:
                                liftPath.pop(j)
                                continue          
                                
                            time2Reach += t_stop
                            liftPath.pop(j)
                            continue
                        j += 1
                        
                    # moving out from the main loop as lift has reached user's destiny floor
                        
                    liftLoc = urMove
                    liftPath.pop(0)            
                    break
                else:
                    break

    return time2Come, time2Reach
    
 
# Driver Code


floors = int(input('total floors: '))
liftLoc = int(input('Current lift locn: '))
urLoc = int(input('You are at: '))
urMove = int(input('You want to go to: '))
redButtons = list(map(int, input().split()))
direc = list(map(int, input().split()))

a = liftSys(floors, liftLoc, urLoc, urMove, redButtons, direc)

# Final Output

if a != None:
    print('You have to wait for {} seconds and you will reach floor #{} in approx {} seconds'.format(a[0], urMove, a[0]+a[1]))


