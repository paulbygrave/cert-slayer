from classes.game import Person, bcolors

magic = [{"name": "Study", "cost": 20, "dmg": 120},
         {"name": "ExamDump", "cost": 10, "dmg": 20},
         {"name": "PracticeTest", "cost": 15, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("==============================")
    try:
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) -1
            
            spell = player.get_spell_name(magic_choice)
            cost = player.get_spell_mp_cost(magic_choice)

            current_mp = player.get_mp()

            if cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP to cast that!\n" + bcolors.ENDC)
                continue

            player.reduce_mp(cost)
            magic_dmg = player.generate_spell_damage(magic_choice)
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage." + bcolors.ENDC)
            

        enemy_choice = 1

        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacks for", enemy_dmg, "points of damage.")

        print("==============================")
        print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
        print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
        print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

        if enemy.get_hp() == 0:
            print(bcolors.OKGREEN + "You have defeated the enemy!" + bcolors.ENDC)
            running = False
        elif player.get_hp() == 0:
            print(bcolors.FAIL + "The enemy has defeated you!" + bcolors.ENDC)
            running = False

    except ValueError as err:
        print("Please choose a valid action!")
