try:
  from IPython.display import clear_output
except:
  def clear_output():
    print("\n"*100)

def Display(L):
    '''
    Input= List of value of blocks
    output=print the table on console screen
    '''
    clear_output()
    print(L[7]+"|"+L[8]+"|"+L[9])
    print(L[4]+"|"+L[5]+"|"+L[6])
    print(L[1]+"|"+L[2]+"|"+L[3])

def Input():
    '''
    take the input for the positon to put X open
    '''
    global flag
    print("Chose Player"+str(max(flag,0)+1)+"'s Next Position")
    a=int(input())
    
    while a in l or a not in list(range(1,10)):
          a=int(input())
    l.append(a)
    L[a]=symbol[max(flag,0)]
    flag*=-1

def Win():
    '''
    Check for Game end
    return true if Game ends any how else False
    '''
    flag=0 #it is local variable
    if L[7]==L[4]==L[1]==symbol[0] or L[8]==L[5]==L[2]==symbol[0] or L[9]==L[6]==L[3]==symbol[0] or L[7]==L[8]==L[9]==symbol[0] or L[4]==L[5]==L[6]==symbol[0]or L[1]==L[2]==L[3]==symbol[0] or L[7]==L[5]==L[3]==symbol[0] or L[9]==L[5]==L[1]==symbol[0]:
        print("Player 1 Wins!!")
        return True
    if L[7]==L[4]==L[1]==symbol[1] or L[8]==L[5]==L[2]==symbol[1] or L[9]==L[6]==L[3]==symbol[1] or L[7]==L[8]==L[9]==symbol[1] or L[4]==L[5]==L[6]==symbol[1]or L[1]==L[2]==L[3]==symbol[1] or L[7]==L[5]==L[3]==symbol[1] or L[9]==L[5]==L[1]==symbol[1]:
        print("Player 2 Wins!!")
        return True
    for i in range(1,10):
      try:#if there is not an integer
        if int(L[i]) in list(range(1,10)):
            flag=1
            return False
      except:
        pass
    if flag!=1:
        print("Tie")
        return True
    return False

def SYM():
    '''
    Input=directly from console screen
    output=order list of symbol for player 1 and 2
    '''
    print("Player 1's Symbol(X or O):")
    a=input().upper()
    while a!="X" and a!="O":
        a=input().upper()
    if a=="X":
        return ["X","O"]
    else:
        return ["O","X"]

Ans = True
while Ans:
    flag=-1 #control the turn of player
    L=['0','1','2','3','4','5','6','7','8','9'] #List for block values
    l=[]
    symbol=SYM()
    Display(L)
    while not Win():
        Input()
        Display(L)
    ans=input("Do you wnat to paly again(Y/N):").upper()
    if ans!="Y":
        Ans=False 
