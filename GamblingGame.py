import random

name = input("What is your name, player? ")
score = 0
score_multiplier = 1
Cash = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.min_health = 0

    def take_dmg(self, amount):
        self.health -= amount
        if self.health < self.min_health:
            self.health = self.min_health

        print("You took", amount, "damage! Current health:", self.health)

        if self.health == self.min_health:
            print("Game ended.")

    def regen_health(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

        print("You healed", amount, "health! Current health:", self.health)


pl = Player(name)
print("Hello,", pl.name)
print("You have currently", pl.health, "life")

while pl.health > pl.min_health:
    print("Current Score:", int(score))
    print("-" * 32)
    print("What do you want to do?")
    print("> 1 - Play")
    print("> 2 - Enter the Shop")
    print("> 3 - Travel")
    print("> 4 - Get Player Stats")
    print("> 5 - End the game")

    question = input("> ").strip()

    if question == "1":
        dmg_or_health = random.randint(1, 50)
        chances = random.randint(1, 2)
        print("Deciding your fate...")
        score += 10 * score_multiplier
        score_multiplier *= 1.1

        if chances == 1:
            pl.take_dmg(dmg_or_health)
        else:
            pl.regen_health(dmg_or_health)

    elif question == "2":
        print("Shop is not implemented yet.")

    elif question == "3":
        print("Travelling isn't implemented yet' .")
        
    elif question == "4":
    	print("Current Health:", pl.health)
    	print("MaxHealth:", pl.max_health)

    elif question == "5":
        break

    else:
        print("Enter a number")

print("Your score is", int(score))