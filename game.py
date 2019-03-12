import random
moves = ["Fireball", "Lightning", "Restore Energy", "Medkit"]

"""
Create a Player Class
Holds variables for both enemy and player
"""
class Player:

    def __init__(self):
        self.health = 100.0
        self.energy = 100.0

    def fireball(self, enemy):
        if self.energy >= 25:
            self.loseEnergy(25)
            enemy.loseHealth(25)
        else:
            print("You did nothing")

    def lightning(self, enemy):
        if self.energy >= 35:
            self.loseEnergy(35)
            enemy.loseHealth(35)
        else:
            print("You did nothing")

    def medkit(self):
        if self.health < 50:
            if self.energy >= 50:
                self.loseHealth(-50)
                self.loseEnergy(50)
        else:
            print("You have too much health, You did nothing!")
    def replenishEnergy(self):
        if self.energy <= 24:
            self.energy += 50
        else:
            print("You have too much Energy and did nothing!")
    def loseHealth(self, amount):
        self.health = self.health - amount

    def loseEnergy(self, amount):
        self.energy = self.energy - amount

def printStats():
    print("Player Health: "+str(player.health) + " Player Energy " + str(player.energy) )
    print("Enemy Health: "+str(enemy.health) + " Enemy Energy " + str(enemy.energy) )

"""
This functions cotains the code for the AI 
"""
def botPick():
    options = {"fireball" : 25, "lightning" : 35, "Restore Energy" : 0, "medkit" : 50}
    if(enemy.energy <= 24):
        enemy.replenishEnergy()
        print("Enemy replenish Energy")
    elif(enemy.health < 30 and enemy.energy >= 50):
        enemy.medkit()
        print("Enemy used medkit")
    elif(enemy.energy >= 35):
        uses = ["lightning", "fireball"]
        opt = random.choice(uses)
        if opt == uses[0]:
            enemy.lightning(player)
        elif opt == uses[1]:
            enemy.fireball(player)
        print("Enemy used "+opt)
    else:
        enemy.fireball(player)
        print("Enemy used fireball")
    


player = Player()
enemy = Player()

print("====================Welcome to ______ ====================")
print("You will against a deadly enemy, Can you stop it?")
print("==============Pick Your Options Carefully=================")
print("If you pick an option and do not have enough energy then you will have to pass your go")
while True:
    printStats()
    if (player.health <= 0):
        print("You DIED\nGood Luck Next Time!")
        break
    elif(enemy.health <= 0):
        print("You Killed The ENEMY\nWELL DONE!")
        break
    else:
        pass
    
    option = input("Wwhat power would you like to use?\n\
F - Fireball - 20 Energy\n\
L - Lightning - 35 Energy\n\
R - Replenish Energy - 0 Energy\n\
M - Medkit - 50 Energy\n>>>")
    if(option.lower() == "f"):
        player.fireball(enemy)
        printStats()
    elif(option.lower() == "l"):
        player.lightning(enemy)
        printStats()    
    elif(option.lower() == "m"):
        player.medkit()
    elif(option.lower() == "r"):
        player.replenishEnergy()
    print("\n\n")
    botPick()
    
    
