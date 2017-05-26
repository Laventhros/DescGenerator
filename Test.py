# I want to Define what descriptors can be used with each weapon.
# I'll start with first, opening, and reading a file
# with a weapon and its damage type on it.
import sys

wepfile = "Weapons.txt"

# Define the 'Weapon' Class, which will be how the weapon information is stored.

class WeaponObj(object):
    def  __init__(self):
        self.name = "I'm a Weapon"
        self.dmg = "I do Damage"

    def swing(self):
        print (" " +self.name+ " & " + self.dmg)
# Define the fluff text that goes with everything.
class DescripObj(object):
    def __init__(self):
        self.subject = "Bandit"
        self.verb = "Attacks"
        
        

# Testing the creation of this object
FirstWep = WeaponObj()
FirstWep.swing()

# Now we want to open the file, and split it into a variable.
words = []
with open(wepfile) as opf:
    for line in opf:
        words.append([word for word in line.strip().split(',')])
    for pair in words:
        try:
            FirstWep.name , FirstWep.dmg = pair[0],pair[1]
            #Do some other things
        except IndexError:
            print("A line in the file doesn't have enough entries.")
    
    
  
# Test again
FirstWep.swing()

# Now we check if we can make a list of Weapons
# First we grab the Martial weapon file

mfile = "Martial.txt"

# Count how many lines in the file.
with open(mfile) as mf:
    count = sum(1 for line in mf if line.rstrip('\n'))

# Create a List of Instances
WeaponList = [ WeaponObj() for i in range(count)]


# Now we'll duplicate some of the work above and put that information in the instances.
myWeapons = []
n = 0
with open(mfile) as mf:
    for line in mf:
        myWeapons.append([word for word in line.strip().split(',')])
    for pair in myWeapons:
        try:
            WeaponList[n].name , WeaponList[n].dmg = pair[0],pair[1]
            n += 1
        except IndexError:
            print("A line in the file doesn't have enough entries.")


for i in range(count):
    WeaponList[i].swing()
    
        
    
