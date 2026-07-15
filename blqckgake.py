import random
user=[]
pc=[]
def choice ():
  nember=[1,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(nember)
def lestsum(v):
  r=0
  for i in v :
   r+=i
  return r
while True:
  a=input("do you want play : ")
  if a=="y":
    user.append(choice())
    user.append(choice())
    pc.append(choice())
    pc.append(choice())
    print (f"your cards {user} score={lestsum(user)}")
    print (f"pc cards {pc[0]}")
    while True:
      if lestsum(user)==21:
        print("you win")
        break
      elif lestsum(user)>21:
        print(f"your scor is {lestsum(user)}")
        print ("you lost")
        break
      else:
        get=input("do you want another card (y or n)")
        if get=="y":
          user.append(choice())
          print (f"your scor {lestsum(user)}")
        else:
          break
    if lestsum(pc)<17:
      pc.append(choice())
    if  lestsum(pc)>21:
      print (f"the scor of pc {lestsum(pc)}")
      print("you win")
    elif lestsum(pc)>lestsum(user):
      print (f"the scor of pc {lestsum(pc)}")
      print("you lost")
    else:
      print("you win")
      print (f"the scor of pc {lestsum(pc)}")
      print (f"the scor of user {lestsum(user)}")
  elif a =="n":
    break
  else:
    print("incorect")