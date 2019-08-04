class node :
    def __init__(self):
        self.next = None

class cricket():
    def __init__(self):
        self.head = None
        self.name = []
        self.runs = []
        self.age = []
        self.average = []
    def player(self,naam,r,umar):
        if naam in self.name:
            print("following player already exist")
        else:
            self.name.append(naam)
            g = self.name.index(naam)
            self.runs.append([])
            self.runs[g].append(r)
            self.age.append(umar)

    def update(self,naam,r):
        if naam in self.name:
           g = self.name.index(naam)
           self.runs[g].append(r)
    def display(self, naam):
        if naam in self.name:
            g = self.name.index(naam)
            print("name = ", naam)
            print("runs  = ",self.runs[g])
            print("age=",self.age[g])
        else :
            print("player dosent exist")
    def remove(self,naam):
        if naam in self.name:
            g = self.name.index(naam)
            del(self.name[g])
            del(self.runs[g])
            del(self.age[g])
p = cricket()

while True:
   print("welcome to cricket stats program")
   print("enter the keyword as per below instructions \n")
   print("1: see player stats\n"
      "2: add new player and his stats\n"
      "3: update stats of existing player\n"
      "4: remove a player from stats \n ")
   s = int(input())
   if s ==1:
       print("enter the name of player you want to see")
       n = input()
       p.display(n)
   elif s==2:
       print("enter the name of player")
       z = input()
       print("enter age of player")
       a = int(input())
       print("enter the runs scored by him(note that you can only add one inning run at one time)")
       l = int(input())
       p.player(z,l,a)
       print("congrats! player added")
       p.display(z)
   elif s ==3:
       print("enrer the name of player you wanna update")
       f = input()
       print("enter runs scored by him")
       q = int(input())
       p.update(f,q)
       p.display(f)
   else:
       print("enter the name of player you wanna delete(player once deleted cant be reproduced)")
       d = input()
       p.remove(d)
       print("player deleted")

   print("press 1 for quitting the program or else press 2")
   h = int(input())
   if h ==1:
       break
