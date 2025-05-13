import time
from timedinput import timedinput
import random
from pyfiglet import Figlet

# enemy class
class Slime:
    species = "Slime"
    def __init__(self, level: int):
        self.level = level
        self.hp = level * 5
        self.attack = (level / 2) * 4
        self.atkspeed = level * 1
        self.value = 5

# enemy class
class Skeleton:
    species = "Skeleton"
    def __init__(self, level: int):
        self.level = level
        self.hp = level * 5
        self.attack = (level / 2) * 6
        self.atkspeed = level * 2
        self.value = 6

# boss class
class Boss_SlimeQueen:
    species = "Slime Queen"
    def __init__(self, level: int):
        self.level = level
        self.hp = level * 18
        self.attack = (level / 2) * 10
        self.atkspeed = level * 1
        self.value = 11

# boss class
class Boss_SkeletonKing:
    species = "Skeleton King"
    def __init__(self, level: int):
        self.level = level
        self.hp = level * 16
        self.attack = (level / 2) * 14
        self.atkspeed = level * 4
        self.value = 12

# class for Player
class Player:
    species = "Human"
    def __init__(self):
        self.hp = 15
        self.atk = 1
        self.defense = 1
        self.atkspeed = 1
        self.gold = 0


def main():
    font = Figlet(font="cricket")
    print(font.renderText("Type Castle",))
    print("****************************************************************")
    main_menu = {}
    main_menu["[1]"]="Play"
    main_menu["[2]"]="Exit"
    while True:
        options = main_menu.keys()
        for entry in options:
            print(entry, main_menu[entry])
        print("")
        selection = input("Action: ")
        if selection == "1":
            floor1()
            break
        elif selection == "2":
            exit()


# begins floor 1 dungeon
def floor1():
    player1 = Player()
    print("Welcome to the castle level 1.\n")
    time.sleep(2)

    print("Floor 1 - Room 1")
    print("***************** \n")
    time.sleep(2)

    player1 = floor1_battle(player1)

    print("Floor 1 - Room 2 - Shop")
    print("************************ \n")
    time.sleep(2)

    player1 = floor1_shop(player1)

    print("Floor 1 - Room 3 - Battle")
    print("************************** \n")
    time.sleep(2)

    player1 = floor1_battle(player1)

    print("Floor 1 - Boss Battle")
    print("********************** \n")
    time.sleep(2)

    player1 = boss_battle(player1)

    print("Floor 1 - Blacksmith")
    print("********************* \n")
    time.sleep(2)

    player1 = blacksmith(player1)


# menu called when it is the user's turn to act in a battle
def battle_menu():
    battle_menu = {}
    battle_menu["[A]"]="Attack"
    battle_menu["[D]"]="Defend"
    battle_menu["[S]"]="Stats"
    while True:
        options = battle_menu.keys()
        for entry in options:
            print(entry, battle_menu[entry])
        print("")
        selection = input("Action: ")
        if selection == "A":
            return "Attack"
        elif selection == "D":
            return "Defend"
        elif selection == "S":
            return "Stats"
        else:
            pass


# battle loop for floor 1 battles
def floor1_battle(player1):
    enemy_pool = ["Slime", "Skeleton"]
    enemy = random.choice(enemy_pool)
    if enemy == "Slime":
        enemy1 = Slime(1)
    elif enemy == "Skeleton":
        enemy1 = Skeleton(1)
    player = player1
    print(f"Watch out! You bumped into a {enemy1.species} and entered battle!")
    print("")
    time.sleep(2)

    # loop continues battle until enemy1 is dead
    while enemy1.hp > 0:
        print(f"{enemy1.species}: {enemy1.hp} HP")
        print(f"Your HP: {player.hp} HP")
        print("")


        # if enemy has higher atk speed, they act before the player
        if enemy1.atkspeed > player.atkspeed:
            print(f"The {enemy1.species} prepares to attack you...")
            time.sleep(2)
            print("")
            got_hit = qte(enemy1.species)
            if got_hit == "hit":
                player.hp = enemy_damage(enemy1.attack, player.hp)
            if player.hp < 0:
                break
            else:
                pass

            print(f"{enemy1.species}: {enemy1.hp} HP")
            print(f"Your HP: {player.hp} HP")
            print("")

            while True:
                selection = battle_menu()
                print("")
                if selection == "Attack":
                    enemy1.hp -= player.atk * 2
                    if enemy1.hp < 0:
                        break
                    else:
                        print(f"You hit the {enemy1.species}")
                        print("")
                        time.sleep(2)
                        break
                if selection == "Stats":
                    print(f"{enemy1.species} \nHP: {enemy1.hp} \nATK: {enemy1.attack} \nATK SPD: {enemy1.atkspeed}")
                    print("")
                    print(f"Player \nHP: {player.hp} \nATK: {player.atk} \nATK SPD: {player.atkspeed} \nDEF: {player.defense}")
                    print("")
                    pass
            if enemy1.hp < 0:
                break

            if player.hp < 0:
                game_over()


        # if player atk speed is higher, the user acts first
        elif enemy1.atkspeed <= player.atkspeed:
            while True:
                selection = battle_menu()
                print("")
                if selection == "Attack":
                    enemy1.hp -= player.atk * 2
                    if enemy1.hp < 0:
                        break
                    else:
                        print(f"You hit the {enemy1.species}")
                        print("")
                        time.sleep(2)
                        break
                if selection == "Stats":
                    print(f"{enemy1.species} \nHP: {enemy1.hp} \nATK: {enemy1.attack} \nATK SPD: {enemy1.atkspeed}")
                    print("")
                    print(f"Player \nHP: {player.hp} \nATK: {player.atk} \nATK SPD: {player.atkspeed} \nDEF: {player.defense}")
                    print("")
                    pass

            if enemy1.hp < 0:
                break

            print(f"The {enemy1.species} prepares to attack you...")
            time.sleep(2)
            print("")
            got_hit = qte(enemy1.species)
            if got_hit == "hit":
                player.hp = enemy_damage(enemy1.attack, player.hp)
            if player.hp < 0:
                break
            else:
                pass

    if player.hp < 0:
        game_over()

    player.gold = player.gold + enemy1.value
    print(f"Congratualations! You defeated the {enemy1.species}!")
    time.sleep(2)
    return player

# battle loop for boss rooms
def boss_battle(player1):
    boss_pool = ["Slime Queen", "Skeleton King"]
    boss = random.choice(boss_pool)
    if boss == "Slime Queen":
        boss1 = Boss_SlimeQueen(1)
    elif boss == "Skeleton King":
        boss1 = Boss_SkeletonKing(1)
    player = player1
    print("Beware. You are entering the Boss floor. A dangerous opponent approaches...")
    print(f"You bump into a {boss1.species}.")
    print("")
    time.sleep(2)

    while boss1.hp > 0:
        print(f"{boss1.species}: {boss1.hp} HP")
        print(f"Your HP: {player.hp} HP")
        print("")

        if boss1.atkspeed > player.atkspeed:
            print(f"The {boss1.species} prepares to attack you...")
            time.sleep(2)
            print("")
            got_hit = boss_qte(boss1.species)
            if got_hit == "hit":
                player.hp = enemy_damage(boss1.attack, player.hp)
            if player.hp < 0:
                break
            else:
                pass

            print(f"{boss1.species}: {boss1.hp} HP")
            print(f"Your HP: {player.hp} HP")
            print("")

            while True:
                selection = battle_menu()
                print("")
                if selection == "Attack":
                    boss1.hp -= player.atk * 2
                    if boss1.hp < 0:
                        break
                    else:
                        print(f"You hit the {boss1.species}")
                        print("")
                        time.sleep(2)
                        break
                if selection == "Stats":
                    print(f"{boss1.species} \nHP: {boss1.hp} \nATK: {boss1.attack} \nATK SPD: {boss1.atkspeed}")
                    print("")
                    print(f"Player \nHP: {player.hp} \nATK: {player.atk} \nATK SPD: {player.atkspeed} \nDEF: {player.defense}")
                    print("")
                    pass
            if boss1.hp < 0:
                break

            if player.hp < 0:
                game_over()


        # if player atk speed is higher, you act first
        elif boss1.atkspeed <= player.atkspeed:
            while True:
                selection = battle_menu()
                print("")
                if selection == "Attack":
                    boss1.hp -= player.atk * 2
                    if boss1.hp < 0:
                        break
                    else:
                        print(f"You hit the {boss1.species}")
                        print("")
                        time.sleep(2)
                        break
                if selection == "Stats":
                    print(f"{boss1.species} \nHP: {boss1.hp} \nATK: {boss1.attack} \nATK SPD: {boss1.atkspeed}")
                    print("")
                    print(f"Player \nHP: {player.hp} \nATK: {player.atk} \nATK SPD: {player.atkspeed} \nDEF: {player.defense}")
                    print("")
                    pass

            if boss1.hp < 0:
                break

            print(f"The {boss1.species} prepares to attack you...")
            time.sleep(2)
            print("")
            got_hit = qte(boss1.species)
            if got_hit == "hit":
                player.hp = enemy_damage(boss1.attack, player.hp)
            if player.hp < 0:
                break
            else:
                pass

    if player.hp < 0:
        game_over()


    player.gold = player.gold + boss1.value
    print(f"Congratualations! You defeated the {boss1.species}!")
    time.sleep(2)
    return player

# shop menu and loop for shop rooms
def floor1_shop(player1):

    shop_menu = {}
    shop_menu["[1]"]="2G - Health Potion (+2 HP)"
    shop_menu["[2]"]="3G - Speed Boots (+1 ATK SPD)"
    shop_menu["[3]"]="3G - Dumbbels (+1 ATK)"
    shop_menu["[4]"] = "Exit Shop"

    player = player1

    print("Welcome to the shop.")
    print("")
    time.sleep(1)
    while True:

        print(f"Your gold: {player.gold}G")
        print("")

        options = shop_menu.keys()
        for entry in options:
            print(entry, shop_menu[entry])

        print("")
        selection = input("Purchase: ")
        if selection == "1":
            if player.gold >= 2:
                player.hp += 2
                player.gold -= 2
            else:
                print("Not enough gold. \n")

        elif selection == "2":
            if player.gold >= 3:
                player.atkspeed += 1
                player.gold -= 3
            else:
                print("Not enough gold.")
        elif selection == "3":
            if player.gold >= 3:
                player.atk += 1
                player.gold -= 3
            else:
                print("Not enough gold.")
        elif selection == "4":
            break
        else:
            pass
    print("")
    print("Thanks for shopping!")
    print("")
    time.sleep(2)
    return player


# shop loop and menu after boss fight
def blacksmith(player1):

    shop_menu = {}
    shop_menu["[1]"]="8G - 13-Hour Clock (Adds 1 second to dodge timer)"
    shop_menu["[2]"]="14G - Big Red Shoes (Ignore any non-boss enemy's ATK SPD; you'll always act before them)"
    shop_menu["[3]"]="20G - Shield of Hylia (Dodge prompts are no longer case-sensitive)"
    shop_menu["[4]"] = "Exit Shop"

    player = player1

    print("Welcome to the blacksmith.")
    print("")
    time.sleep(1)
    while True:

        print(f"Your gold: {player.gold}G")
        print("")

        options = shop_menu.keys()
        for entry in options:
            print(entry, shop_menu[entry])


        selection = input("Purchase: ")
        if selection == "1":
            if player.gold >= 2:
                player.hp += 2
                player.gold -= 2
            else:
                print("Not enough gold.")

        elif selection == "2":
            if player.gold >= 3:
                player.atkspeed += 1
                player.gold -= 3
            else:
                print("Not enough gold.")
        elif selection == "3":
            if player.gold >= 3:
                player.atk += 1
                player.gold -= 3
            else:
                print("Not enough gold.")
        elif selection == "4":
            break
        else:
            pass
    print("")
    print("Thanks for shopping!")
    print("")
    time.sleep(2)
    return player




# if qte is failed, calculates damage taken and returns players new hp
def enemy_damage(enemy_atk, player_hp):
    player_hp = player_hp - enemy_atk
    return player_hp


# qte when an enemy attacks the player
def qte(enemy):
    enemy_type = enemy

    slime_prompts = [
        "parry",
        "PARRY",
        "dodge",
        "DODGE",
    ]

    skeleton_prompts = [
        "pARRy",
        "bLOCk",
        "dODGe",
    ]

    if enemy_type == "Slime":
        prompt = random.choice(slime_prompts)
    elif enemy_type == "Skeleton":
        prompt = random.choice(skeleton_prompts)

    print(f"{prompt}")
    answer = timedinput("Input : ", timeout=3, default="Times up!")
    answer = answer.strip()
    if answer == prompt:
        print("")
        print("* You dodged the attack!")
        print("")
        time.sleep(2)
        return "dodged"
    elif answer == "Times up!":
        print("")
        print("* You got hit!")
        print("")
        time.sleep(2)
        return "hit"
    else:
        print("")
        print("* You got hit!")
        print("")
        time.sleep(2)
        return "hit"

# qte when a boss attacks the player
def boss_qte(boss):
    boss_type = boss

    slimequeen_prompts = [
        "PARRRY",
        "DODDGE",
        "BLOOOCK"
    ]

    skeletonking_prompts = [
        "P A r R Y",
        "p-a-r-r-y",
        "d-o-d-g-e",
        "D O d G E",
        "b-l-o-c-k",
        "B L o C K"
    ]

    if boss_type == "Slime Queen":
        prompt = random.choice(slimequeen_prompts)
        font = Figlet(font="bulbhead")
        print(font.renderText(prompt))
    elif boss_type == "Skeleton King":
        prompt = random.choice(skeletonking_prompts)
        print(f"{prompt}")

    answer = timedinput("Input: ", timeout=5, default="Times up!")
    answer = answer.strip()
    if answer == prompt:
        print("")
        print("* You dodged the attack!")
        print("")
        time.sleep(2)
        return "dodged"
    elif answer == "Times up!":
        print("")
        print("* You got hit!")
        print("")
        time.sleep(2)
        return "hit"
    else:
        print("")
        print("* You got hit!")
        print("")
        time.sleep(2)
        return "hit"

# exits the program when user's HP reaches 0
def game_over():
    print("")
    print("You died :(")
    print("")
    time.sleep(3)
    exit()



main()

