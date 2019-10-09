from classes.colours import bcolors
from classes.battle import Character
from classes.magic import *
from classes.inventory import *
from storytext import *
from logos import *
import random

# Print the title intro
intro_text()

# Print the logo
main_logo()

# Prompt user for name
hero = input('Welcome Hero! Please tell me your name so I may record your noble deeds! : ')
print(f'\nWelcome {hero}!\nThis is your story....\n')

quest_text()

player_spells = [study, practice, ask, handson, sleep, weekend]
enemy_spells = [exhaustion, paternity, sick, drinking, revision]
player_items = [{"item": redbull, "quantity": 15}, {"item": studysnack, "quantity": 10}, {"item": magicbean, "quantity": 5}]

# Instantiate players
player1 = Character(str(hero.ljust(40, ' ')), 9999, 600, 777, 500, player_spells, player_items)
players = [player1]
total_players = len(players)

# Instantiate enemies
enemy1 = Character(str("AWS_Solutions_Architect_Associate".ljust(40, ' ')), 2000, 1000, 300, 250, enemy_spells, [])
enemy2 = Character(str("AWS_SysOps_Associate".ljust(40, ' ')), 4000, 1000, 999, 250, enemy_spells, [])
enemy3 = Character(str("AWS_Developer_Associate".ljust(40, ' ')), 2500, 1000, 300, 250, enemy_spells, [])
enemies = [enemy1, enemy2, enemy3]
total_enemies = len(enemies)

# Set the defeated player and enemy variables to zero
defeated_enemies = 0
defeated_players = 0

running = True
i = 0

# Battle message displays
print(f'\n\n{bcolors.FAIL}{bcolors.BOLD}A VICIOUS CLOUD CERTIFICATION ATTACKS!!!{bcolors.ENDC}')
time.sleep(1)
print(f'\n\n{bcolors.FAIL}{bcolors.BOLD}You have no choice, defeat it using all the magic and powers in your arsenal!{bcolors.ENDC}')
time.sleep(1)
while running:
    print(f'\n\n============================================================\n')
    # Print the health bars of all participants
    print(f'NAME                                                     HP                                      MP')
    for player in players:
        player.get_stats()
    print(f'\n')
    for enemy in enemies:
        enemy.get_enemy_stats()

    # If battle is ongoing, proceed with turn
    for player in players:   

        player.choose_action()
        choice = input('    Choose action: ')
        index = int(choice) - 1

        # Index 0 is the "Attack" option
        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(f'\n{player.name.replace(" ", "")} attacked {enemies[enemy].name.replace(" ", "")} for {dmg} damage.')

            if enemies[enemy].get_hp() == 0:
                print(f'\n{enemies[enemy].name.replace(" ", "")} has been defeated!')
                del enemies[enemy]
                defeated_enemies += 1

        # Index 1 is the "Magic" option
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input('    Choose magic: ')) -1
                
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(f'{bcolors.FAIL}\nNot enough MP to cast that!\n{bcolors.ENDC}')
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(f'{bcolors.OKBLUE}\n{spell.name} heals for {str(magic_dmg)} HP.{bcolors.ENDC}')
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(f'{bcolors.OKBLUE}\n{player.name.replace(" ", "")} cast {spell.name} against {enemies[enemy].name.replace(" ", "")} dealing {str(magic_dmg)} damage.\n{bcolors.ENDC}')

                if enemies[enemy].get_hp() == 0:
                    print(f'{enemies[enemy].name.replace(" ", "")} has been defeated!')
                    del enemies[enemy]
                    defeated_enemies += 1

        # Index 2 is the "Item" option
        elif index == 2:
            player.choose_item()
            item_choice = int(input('    Choose item: ')) - 1

            if item_choice == -1:
                continue
                
            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(f'{bcolors.FAIL}\nNone left...{bcolors.ENDC}')
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(f'{bcolors.OKGREEN}\n{item.name} heals for {str(item.prop)} HP.{bcolors.ENDC}')
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(f'{bcolors.OKGREEN}\n{item.name} fully restores HP/MP!{bcolors.ENDC}')
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(f'{bcolors.FAIL}\n{item.name} deals {str(item.prop)} damage to {enemies[enemy].name.replace(" ", "")}.{bcolors.ENDC}')

                if enemies[enemy].get_hp() == 0:
                    print(f'{enemies[enemy].name.replace(" ", "")} has been defeated!\n')
                    del enemies[enemy]
                    defeated_enemies += 1
    
        # Check if player won
        if defeated_enemies == total_enemies:
            print(f'{bcolors.OKGREEN}\nYou have defeated the enemy!{bcolors.ENDC}')
            running = False
            break
        # Check if enemy won
        elif defeated_players == total_players:
            print(f'{bcolors.FAIL}The enemies have defeated you!{bcolors.ENDC}')
            running = False
            break
        
    time.sleep(1)

    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        if enemy_choice == 0:
            # Choose attack
            target = random.randrange(0, len(players))
            enemy_dmg = enemy.generate_damage()
        
            players[target].take_damage(enemy_dmg)
            print(f'{bcolors.FAIL}{bcolors.BOLD}\n{enemy.name.replace(" ", "")} attacks {players[target].name.replace(" ", "")} for {enemy_dmg} damage.{bcolors.ENDC}')

            if players[target].get_hp() == 0:
                print(f'{bcolors.FAIL}{bcolors.BOLD}{players[target].name.replace(" ", "")} has been defeated!{bcolors.ENDC}')
                del players[target]
                defeated_players += 1
        
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(f'{bcolors.OKBLUE}\n{enemy.name.replace(" ", "")} cast {spell.name} which heals for {str(magic_dmg)} HP.{bcolors.ENDC}')
            elif spell.type == "black":
               
                target = random.randrange(0, len(players))
                players[target].take_damage(magic_dmg)

                print(f'{bcolors.OKBLUE}\n{enemy.name.replace(" ", "")} cast {spell.name} against {players[target].name.replace(" ", "")} dealing {str(magic_dmg)} damage.{bcolors.ENDC}')

                if players[target].get_hp() == 0:
                    print(f'{bcolors.FAIL}{bcolors.BOLD}{players[target].name.replace(" ", "")} has been defeated!{bcolors.ENDC}')
                    del players[target]
                    defeated_players += 1

        # Check if player won
        if defeated_enemies == total_enemies:
            print(f'{bcolors.OKGREEN}\nYou have passed the certification(s)!\nMake sure you post about it on LinkedIn and update your Kimble capabilities!{bcolors.ENDC}')
            running = False
            break
        # Check if enemy won
        elif defeated_players == total_players:
            print(f'{bcolors.FAIL}\nOh dear, it looks like you took on too much! Maybe just try and take on an easier certification next time?!{bcolors.ENDC}')
            running = False
            break
    
    time.sleep(1)

    
