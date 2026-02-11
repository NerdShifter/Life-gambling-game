import random

name = input("What is your name, player? ")
score = 0
cash = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.min_health = 0
        self.strength = 5

class Enemy:
    def __init__(self):
        self.health = random.randint(15, 30)
        self.defense = random.randint(0, 3)
        self.attack = random.randint(3, 8)

def wait():
    input("Press Enter to continue...")

pl = Player(name)

print("Hello,", pl.name)

while pl.health > pl.min_health:

    print("-" * 30)
    print("What do you want to do?")
    print("> 1 - Fight")
    print("> 2 - Show Stats")
    print("> 3 - End Game")

    choice = input("> ")

    if choice == "1":
        enemy = Enemy()
        print("An enemy appeared!")
        print("Enemy Health:", enemy.health)

        while enemy.health > 0 and pl.health > 0:

            print("-" * 30)
            print("Your Health:", pl.health)
            print("Enemy Health:", enemy.health)
            print("> 1 - Attack")
            print("> 2 - Run")

            action = input("> ")

            if action == "1":

                damage = pl.strength - enemy.defense

                if damage < 0:
                    damage = 0

                enemy.health -= damage
                print("You dealt", damage, "damage!")

                if enemy.health > 0:
                    pl.health -= enemy.attack
                    print("Enemy hit you for", enemy.attack, "damage!")

            elif action == "2":
                print("You ran away!")
                break

            else:
                print("Invalid option")

        if enemy.health <= 0:
            print("You defeated the enemy!")
            score += 10
            cash += 5

        if pl.health <= 0:
            print("You died...")

        wait()

    elif choice == "2":
        print("Name:", pl.name)
        print("Health:", pl.health)
        print("Strength:", pl.strength)
        print("Score:", score)
        print("Cash:", cash)
        wait()

    elif choice == "3":
        break

    else:
        print("Enter a valid number.")

print("Game Over.")
print("Final Score:", score)