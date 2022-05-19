def game():
  diskNumber = [] # create an empty list for the ideal list disk order
  stackA = [] # create left post
  stackB = [] # create middle post
  stackC = [] # create right post
  disks = input("How many disks are there?") # ask how many disks the user is playing with
  minimumMoves = 0 # create the minimum moves
  try:
    if int(disks) > 0:
      for x in range (0, int(disks)):
        minimumMoves = minimumMoves*2 + 1 # calculate the minimum moves
      print("Minimum moves is",minimumMoves) # print out the minimum moves
    else:
      print("Invalid Number.") # if user input is less than 0
  except:
    print("Invalid Number.") #if user did not input a number
  numberCount = 1 # must be at least one disk
  for x in range (0, int(disks)): # repeat for the amount of disks in the game
    diskNumber.append(numberCount) # add each number number starting from one to a list
    numberCount +=1 # increases the number each time
  stackA.extend(diskNumber) # place the disks on the left post list
  
  if int(disks)%2 == 0: # if there is an even amount of disks, use this method
    while stackC != diskNumber: # while the game is not finished
      if len(stackB) and len(stackA) != 0:
        if int(stackA[-1]) < int(stackB[-1]):
          print("Move disk",stackB[-1],"to the left stack.")
          stackA.append(stackB[-1])
          stackB.pop(-1)
        elif stackA[-1] > stackB[-1]:
          print("Move disk",stackA[-1],"to the middle stack.")
          stackB.append(stackA[-1])
          stackA.pop(-1)
      elif len(stackB) == 0:
        print("Move disk",stackA[-1],"to the middle stack.")
        stackB.append(stackA[-1])
        stackA.pop(-1)
      elif len(stackA) == 0:
        print("Move disk",stackB[-1],"to the left stack.")
        stackA.append(stackB[-1])
        stackB.pop(-1)
      if stackC != diskNumber:
        if len(stackA) and len(stackC) != 0:
          if int(stackA[-1]) < int(stackC[-1]):
            print("Move disk",stackC[-1],"to the left stack")
            stackA.append(stackC[-1])
            stackC.pop(-1)
          elif int(stackA[-1]) > int(stackC[-1]):
            print("Move disk",stackA[-1],"to the right stack")
            stackC.append(stackA[-1])
            stackA.pop(-1)
        elif len(stackC) == 0:
          print("Move disk",stackA[-1],"to the right stack")
          stackC.append(stackA[-1])
          stackA.pop(-1) 
        elif len(stackA) == 0:
          print("Move disk",stackC[-1],"to the left stack")
          stackA.append(stackC[-1])
          stackC.pop(-1)
      if stackC != diskNumber:  
        if len(stackB) and len(stackC) != 0:
          if int(stackB[-1]) > int(stackC[-1]):
            print("Move disk",stackB[-1],"to the right stack")
            stackC.append(stackB[-1])
            stackB.pop(-1)
          elif int(stackB[-1]) < int(stackC[-1]):
            print("Move disk",stackC[-1],"to the middle stack")
            stackB.append(stackC[-1])
            stackC.pop(-1)
        elif len(stackC) == 0:
          print("Move disk",stackB[-1],"to the right stack")
          stackC.append(stackB[-1])
          stackB.pop(-1)
        elif len(stackB) == 0:
          print("Move disk",stackC[-1],"to the middle stack")
          stackB.append(stackC[-1])
          stackC.pop(-1)
    
  else: # if there is an odd number of disks
    while stackC != diskNumber:
      if len(stackA) and len(stackC) != 0:
        if int(stackA[-1]) < int(stackC[-1]):
          print("Move disk",stackC[-1],"to the left stack")
          stackA.append(stackC[-1])
          stackC.pop(-1)
        elif int(stackA[-1]) > int(stackC[-1]):
          print("Move disk",stackA[-1],"to the right stack")
          stackC.append(stackA[-1])
          stackA.pop(-1)
      elif len(stackC) == 0:
        print("Move disk",stackA[-1],"to the right stack")
        stackC.append(stackA[-1])
        stackA.pop(-1) 
      elif len(stackA) == 0:
        print("Move disk",stackC[-1],"to the left stack")
        stackA.append(stackC[-1])
        stackC.pop(-1)
      if stackC != diskNumber:
        if len(stackB) and len(stackA) != 0:
          if int(stackA[-1]) < int(stackB[-1]):
            print("Move disk",stackB[-1],"to the left stack.")
            stackA.append(stackB[-1])
            stackB.pop(-1)
          elif stackA[-1] > stackB[-1]:
            print("Move disk",stackA[-1],"to the middle stack.")
            stackB.append(stackA[-1])
            stackA.pop(-1)
        elif len(stackA) == 0:
          print("Move disk",stackB[-1],"to the left stack.")
          stackA.append(stackB[-1])
          stackB.pop(-1)
        elif len(stackB) == 0:
          print("Move disk",stackA[-1],"to the middle stack.")
          stackB.append(stackA[-1])
          stackA.pop(-1)
      if stackC != diskNumber:
        if len(stackB) and len(stackC) != 0:
          if int(stackB[-1]) > int(stackC[-1]):
            print("Move disk",stackB[-1],"to the right stack")
            stackC.append(stackB[-1])
            stackB.pop(-1)
          elif int(stackB[-1]) < int(stackC[-1]):
            print("Move disk",stackC[-1],"to the middle stack")
            stackB.append(stackC[-1])
            stackC.pop(-1)
        elif len(stackC) == 0:
          print("Move disk",stackB[-1],"to the right stack")
          stackC.append(stackB[-1])
          stackB.pop(-1)
        elif len(stackB) == 0:
          print("Move disk",stackC[-1],"to the middle stack")
          stackB.append(stackC[-1])
          stackC.pop(-1)
  print("The tower is finished!")
def main(): 
    game()
    while input("Would you like to solve another game? (Y/N)").upper() == "Y":  
      game()

if (__name__ == "__main__"):
  main()