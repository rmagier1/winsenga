"""

Problem 4: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors.
The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is
open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time,
every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door. Using a python program;

a) what state are the doors in after the last pass? Which are open, which are closed?

"""

def main():
    doors = [[i,False] for i in range(1,101)]
    #false for closed, true for open

    doors_passes(doors)
    open, close = stateofdoors(doors)
    print "Open doors (%d): %s" %(len(open), open)
    print "Closed doors (%d): %s" %(len(close), close)

def doors_passes(doors):
    """perform the 100 iterations"""
    print len(doors)
    for i in range(len(doors)):
        for j in range(i,len(doors),i+1):
            if doors[j][0] % (i+1) == 0:
                doors[j][1] = not doors[j][1]

def stateofdoors(doors):
    """figure out how many doors are open or closed"""
    open = []
    close = []
    for item in doors:
        if item[1]: open.append(item[0])
        else: close.append(item[0])

    return open,close

main()