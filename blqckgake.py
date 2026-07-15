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
    
    if lestsum(user)==21:
      print("you win")
      break
    elif lestsum(user)>21:
      print ("you lost")
      break
    get=input("do you want another card (y or n)")
    if get=="y":
      user.append(choice())
  elif a =="n":
    break
  else:
    print("incorect")