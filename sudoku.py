
#puzzle to be solved
sud = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_sud(sud):
    for i in range(len(sud)):
        if i%3 == 0 and  i!=0:
                print("\n- - - - - - - - - - - - -")
        for j in range(9):
            if j%3 == 0 and  j!=0:
                print(" | ",end=" ")
            print(sud[i][j] ,end=" ")
        if (i+1)%3 !=0:
           print("\n")
#print_sud(sud)

def check_sud(sud,index,value):
    
    #check for row

    for i in range(9):
        if value==sud[index[0]][i] and i!=index[1] :
            return False
  #for column
    for j in range(9):
        if value ==sud[j][index[1]] and j!=index[0]:
            return False
 #for a squire(block)
    x=int(int(index[0]/3)*3)
    y =int(int(index[1]/3)*3)

    for i in range(x,x+3):
        for j in range(y,y+3):
            if sud[i][j] == value and (i,j) !=index:
                return False           
    return True
#print(check_sud(sud,(0,2),5)) 

def find_emp(sud):
    for i in range(9):
        
        for j in range(9):
            if sud[i][j]==0:
                return (i,j)
                break
        if j != 8 :
            break
            
def solve(sud,pos):

    if find_emp(sud)==None:
       return True
    for g in range(1,10):
         if check_sud(sud,pos,g)==True:
             sud[pos[0]][pos[1]] =g
             
             filled =solve(sud,find_emp(sud))
             if not filled:
                  sud[pos[0]][pos[1]] =0 
             if find_emp(sud)==None:
   
                 return True
         else:
             continue
     
    return False

#    for i in range(1,10):
#        if check_sud(sud,  (pos[0],pos[1]),i):
#            sud[pos[0]][pos[1]] = i

#            if solve(sud,find_emp(sud)):
#                return True

#            sud[pos[0]][pos[1]] = 0

#    return False


print(solve(sud,find_emp(sud)))
print_sud(sud)
                