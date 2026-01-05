import random

Name = input("What is your name, player? ")
Score = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.Health = 100
        self.MaxHealth = 100
        self.MinHealth = 0

    def take_dmg(self, amount):
        self.Health -= amount
        if self.Health < self.MinHealth:
            self.Health = self.MinHealth
        print("You took", amount, "damage! Current health:", self.Health)
        if self.Health == self.MinHealth:
            print("You lost!")

    def regen_Health(self, amount):
        self.Health += amount
        if self.Health > self.MaxHealth:
            self.Health = self.MaxHealth
        print("You healed", amount, "health! Current health:", self.Health)

Pl = Player(Name)
print("Hello,", Pl.name)
print("You have currently", Pl.Health, "life")

while Pl.Health > Pl.MinHealth:
    question = input("Would you like to play? (Yes/No) ").lower()  # input is case-insensitive
    
    if question == "yes":
        Dmg_or_Health = random.randint(1, 50)
        Chances = random.randint(1, 2)
        print("Deciding your fate...")
        Score += 10

        if Chances == 1:
            Pl.take_dmg(Dmg_or_Health)
        else:
            Pl.regen_Health(Dmg_or_Health)

    elif question == "no":
        break
    else:
        print("Please answer Yes or No.")

print("Your score is", Score)
