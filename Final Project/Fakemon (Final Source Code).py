#Fakemon.py
#This program will run a text-based adventure game. Read the introduction to learn more about the game and the various aspects of it!
#by Awais Razaque 12/18/23

def skillset_random():
    import random
    return random.choice(["Metal", "Wild", "Ocean", "Solar", "Explosive", "Shadow"]) #returns a random metal set which will be assigned to a Fakemon

def flip_coin():
    import random
    return random.choice(["Heads", "Tails"])

def introInfo(): #introduction text 
    global trainer_name
    print("In the world of Fakemon, there is a region known as Astaria, which is home to a diverse range of species and trainers. This region is known to attract trainers from all over the world with its abundance of resources for expert training of these species, known as Fakemon. The region has rugged terrain with mountains and forests for the Fakemon to receive adequate training in their skills, and it houses growing cities in this new world of Fakemon.")
    print()
    print("However, the region has advanced so much that a group of trainers known as Team Dauntless, who are some of the best trainers in the world, have claimed the region for themselves when it comes to harnessing the power of the legendary Fakemon within the region and ruling with an iron fist. The Astarian government has been unable to stop them, so it's up to a new generation of Fakemon trainers to take up the challenge and put an end to Team Dauntless's evil plans.")
    print()
    print("As a young trainer, you set out on a journey across Astaria, battling other trainers to improve your skills. Along the way, you'll encounter members of Team Dauntless and their minions, who will stop at nothing to achieve their goals. You'll need to use all of your wits, skills, and the power of your developed Fakemon to overcome them and save the region from their tyranny.")
    print()
    while True:
        ready = input("Are you ready to defend the region of Astaria from the doings of Team Dauntless? Please type y/yes or n/no to continue: ").lower()
        if ready == "y" or ready == "yes":
            while True:
                trainer_name = input("What do you want your trainer name to be? (Max Character Limit: 15) ") #trainer_name is set here with a character limit of 15
                if len(trainer_name) <= 15:
                    break
                else:
                    print("Too long of a name. Try again!")
            return trainer_name
        elif ready == "n" or ready == "no":
            return False
        else:
            print("Invalid Choice!")

def gameRules(nameofuser): #gives info on how the game works and different aspects
    import random
    
    global currentFakemon
    global fakemon_hps
    global startermoveDamage
    
    print("Welcome to the world of Fakemon " + nameofuser ,"! My name is Professor Oak and I will guide you throughout this intial process!")
    print("Before you can continue with your journey you will choose your 3 starter Fakemon and learn about some other general rules!")
    print("So lets start by choosing your 3 starter Fakemon!")
    print()
    starterFakemon()
    print("Congratulations " + nameofuser + " you have chosen your starter team of Fakemon! Your team is: ")
    print(currentFakemon)
    print()
    fakemon_hps = [200,250,325]
    print("The health's of your starter team of Fakemon is: ")
    print(fakemon_hps)
    print()
    print("Game Rules:")
    print("You are only allowed to have your 3 starter Fakemon (catching to be added)! And your Fakemon can be the same Fakemon as it is all random!")
    print("If a Fakemon dies, you will continue with the other Fakemon you have and if you run out of Fakemon before you reach the end, you will have lost!")
    print("If all your Fakemon live till the last battle (against the Leader of Team Dauntless) then you win!")
    print("After battling any trainer or any Fakemon, you will be given a random amount of xp (the higher the xp, the closer you get to leveling up your player).")
    print("You will level up at xp amounts of 250 (level 2), 1000 (level 3), 1600 (level 4) , 2100 (level 5), 2600 (level 6), 3200 (level 7), 3800 (level 8), 4400 (level 9), and 5000 (level 10).")
    print("Each move has a randomly generated damage. However, your opponents can use any move from any skillset!")
    print("You will be able to recieve one more move per Fakemon as your trainer level progresses to level 3, but for the time being lets give your new starter team some starter moves.")
    print()
    starterMove(currentFakemon)
    startermoveDamage = [random.randint(50,90), random.randint(50,90), random.randint(50,90)] #damage numbers for the users moves - slightly higher to give some advantage - 50 to 90 compared to 40 to 85 for the opponent
    print()
    print("Skillset Information:")
    print("In the metal skillset, the moves you can obtain are Meteor Mash, Steel Punch, Draco Meteor, Iron Forge, and Wrecking Ball.")
    print("In the wild skillset, the moves you can obtain are Fire Dance, Blazing Storm, Fire Circle, Magma Storm, Heat Wave, Flame Punch, and Flame Storm.")
    print("In the ocean skillset, the moves you can obtain are Hydro Pump, Tsunami, Water Bomb, and Hydro Vortex.")
    print("In the solar skillset, the moves you can obtain are Solar Beam, Solar Cooling, Bullet Seed, and Energy Ball.")
    print("In the explosive skillset, the moves you can obtain are Explosion, Bullet Bill, Power Surge, Sphere of Destruction, Blast, Detonation, Bursting Dash, and Surge.")
    print("In the shadow skillset, the moves you can obtain are Shadow Bomb, Nightmare, Shadow Blast, Shadow Ball, Creep, and Taunt.")
    print()
    print("The skillsets of each Fakemon are pre-determined, but you can figure the skillset out of your Fakemon by looking at their starter moves and when you unlock another set of new moves at level 3!")

def starterFakemon(): 
    import random
    
    global currentFakemon
    global everyFakemon
    global everyfakemonSkillset

    global metalMoves
    global wildMoves
    global oceanMoves
    global solarMoves
    global explosiveMoves
    global shadowMoves
    
    #gives the users 3 random choices from the list of all fakemon to choose between for their 3 starter Fakemon
    pokemonSelected = 0
    while pokemonSelected != 3:
        randomgenFakemon1 = random.randint(1,18)
        randomgenFakemon2 = random.randint(1,18)
        randomgenFakemon3 = random.randint(1,18)
        print("Please choose one of the following Fakemon:")
        print("1. " + everyFakemon[randomgenFakemon1 - 1])
        print("2. " + everyFakemon[randomgenFakemon2 - 1])
        print("3. " + everyFakemon[randomgenFakemon3 - 1])
        userfakemonChoice =(input("What is your choice? Please type the number of your choice: "))
        print()
        if userfakemonChoice == "1":
            currentFakemon.append(everyFakemon[randomgenFakemon1 - 1])
            pokemonSelected = pokemonSelected + 1
        elif userfakemonChoice == "2":
            currentFakemon.append(everyFakemon[randomgenFakemon2 - 1])
            pokemonSelected = pokemonSelected + 1
        elif userfakemonChoice == "3":
            currentFakemon.append(everyFakemon[randomgenFakemon3 - 1])
            pokemonSelected = pokemonSelected + 1
        else:
            print("That is an invaid choice!")

def starterMove(usersFakemon):
    import random
    global everyFakemon
    global everyfakemonSkillset
    
    global metalMoves
    global wildMoves
    global oceanMoves
    global solarMoves
    global explosiveMoves
    global shadowMoves

    global currentstarterMoves

    for i in range(len(usersFakemon)):
        index = everyFakemon.index(usersFakemon[i])
        if everyfakemonSkillset[index] == "Metal":
            movelearned = metalMoves[random.randint(0,4)]
            currentstarterMoves.insert(i, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
        elif everyfakemonSkillset[index] == "Wild":
            movelearned = wildMoves[random.randint(0,6)]
            currentstarterMoves.insert(i, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
        elif everyfakemonSkillset[index] == "Ocean":
            movelearned = oceanMoves[random.randint(0,3)]
            currentstarterMoves.insert(i, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
        elif everyfakemonSkillset[index] == "Solar":
            movelearned = solarMoves[random.randint(0,3)]
            currentstarterMoves.insert(i, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
        elif everyfakemonSkillset[index] == "Explosive":
            movelearned = explosiveMoves[random.randint(0,7)]
            currentstarterMoves.insert(i, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
        elif everyfakemonSkillset[index] == "Shadow":
            movelearned = shadowMoves[random.randint(0,5)]
            currentstarterMoves.insert(i, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
    print("Your starter teams starter moves are now:")
    print(currentstarterMoves)

def battleoneMove():
    import random
    global everyFakemon
    global currentFakemon
    global fakemon_hps
    global currentstarterMoves
    global startermoveDamage
    global combinedMoves
    global combinedDamage
    global player_xp
    
    wildFakemon = everyFakemon[random.randint(0,29)] #30 fakemon in total in the game, opponent chooses between them 
    wildfakemonHP = random.randint(175,300) #since the users hps are 200, 250, and 325, the opponents will be generated between 175 to 300, once again giving some advantage to the user
    print("A wild", wildFakemon ,"has appeared!")
    print("The", wildFakemon ,"has", wildfakemonHP ,"hp.")
    print()
    print("Your current team: ", currentFakemon)
    print("HP's: ", fakemon_hps)
    while True:
        fakemonchoice = input("What Fakemon do you want to use in this battle? Please type their position number: ")
        if len(currentFakemon) == 3:
            if fakemonchoice == "1" or fakemonchoice == "2" or fakemonchoice == "3":
                break
            else:
                print("Invalid Choice. Try again!")
        elif len(currentFakemon) == 2:
            if fakemonchoice == "1" or fakemonchoice == "2":
                break
            else:
                print("Invalid Choice. Try again!")
        elif len(currentFakemon) == 1:
            if fakemonchoice == "1":
                break
            else:
                print("Invalid Choice. Try again!")
    fakemonchoice = int(fakemonchoice)
    userfakemonName = currentFakemon[fakemonchoice - 1]
    userfakemonHP = fakemon_hps[fakemonchoice - 1]
    print("Lets now decide whos turn will come first via a coin flip! ")
    print()
    if flip_coin() == "Heads":
        while wildfakemonHP >= 0 or userfakemonHP >=0:
            print("It is your turn!")
            print(userfakemonName, "used", currentstarterMoves[fakemonchoice - 1],"and it dealt", startermoveDamage[fakemonchoice - 1], "damage!")
            wildfakemonHP = wildfakemonHP - startermoveDamage[fakemonchoice - 1]
            if wildfakemonHP <= 0:
                print("The wild", wildFakemon ,"has died!")
                xp_gain = random.randint(100, 450)
                player_xp = player_xp + xp_gain 
                print("You have gained", xp_gain, "xp!")
                print("Total XP: ", player_xp)
                print()
                break
            print("It is your opponents turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(wildFakemon, "used", combinedMoves[random_num_move_damage],"and it dealt", combinedDamage[random_num_move_damage], "damage!")
            userfakemonHP = userfakemonHP - combinedDamage[random_num_move_damage]
            if userfakemonHP <=0:
                print("Your Fakemon has died!")
                del currentFakemon[fakemonchoice - 1]
                del startermoveDamage [fakemonchoice - 1]
                del fakemon_hps [fakemonchoice - 1]
                print("Your team is now:", currentFakemon)
                print()
                break
    else:
        while wildfakemonHP >= 0 or userfakemonHP >=0:
            print("It is your opponents turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(wildFakemon, "used", combinedMoves[random_num_move_damage],"and it dealt", combinedDamage[random_num_move_damage], "damage!")
            userfakemonHP = userfakemonHP - combinedDamage[random_num_move_damage]
            if userfakemonHP <=0:
                print("Your Fakemon has died!")
                del currentFakemon[fakemonchoice - 1]
                del startermoveDamage [fakemonchoice - 1]
                del fakemon_hps [fakemonchoice - 1]
                print("Your team is now:", currentFakemon)
                print()
                break
            print("It is your turn!")
            print(userfakemonName, "used", currentstarterMoves[fakemonchoice - 1],"and it dealt", startermoveDamage[fakemonchoice - 1], "damage!")
            wildfakemonHP = wildfakemonHP - startermoveDamage[fakemonchoice - 1]
            if wildfakemonHP <= 0:
                print("The wild", wildFakemon ,"has died!")
                xp_gain = random.randint(100, 450)
                player_xp = player_xp + xp_gain 
                print("You have gained", xp_gain, "xp!")
                print("Total XP: ", player_xp)
                print()
                break

def battletwoMove(): #different battle function for when the user has two moves (at level 3)
    import random
    global everyFakemon
    global currentFakemon
    global fakemon_hps
    global currentstarterMoves
    global startermoveDamage
    
    #adds 3 new damages for the users new moves
    startermoveDamage.append(random.randint(50,90))
    startermoveDamage.append(random.randint(50,90))
    startermoveDamage.append(random.randint(50,90))
    
    global combinedMoves
    global combinedDamage
    global player_xp

    wildFakemon = everyFakemon[random.randint(0,29)]
    wildfakemonHP = random.randint(175,300)
    print("A wild", wildFakemon ,"has appeared!")
    print("The", wildFakemon ,"has", wildfakemonHP ,"hp.")
    print()
    print("Your current team: ", currentFakemon)
    print("HP's: ", fakemon_hps)
    while True:
        fakemonchoice = input("What Fakemon do you want to use in this battle? Please type their position number: ")
        if len(currentFakemon) == 3:
            if fakemonchoice == "1" or fakemonchoice == "2" or fakemonchoice == "3":
                break
            else:
                print("Invalid Choice. Try again!")
        elif len(currentFakemon) == 2:
            if fakemonchoice == "1" or fakemonchoice == "2":
                break
            else:
                print("Invalid Choice. Try again!")
        elif len(currentFakemon) == 1:
            if fakemonchoice == "1":
                break
            else:
                print("Invalid Choice. Try again!")
    fakemonchoice = int(fakemonchoice)
    userfakemonName = currentFakemon[fakemonchoice - 1]
    userfakemonHP = fakemon_hps[fakemonchoice - 1]
    print("Lets now decide whos turn will come first via a coin flip! ")
    print()
    if flip_coin() == "Heads":
        while wildfakemonHP >= 0 or userfakemonHP >= 0:
            print("It is your turn!")
            print()
            print("Moves Available: ")
            print(currentstarterMoves[fakemonchoice - 1])
            print(currentstarterMoves[(fakemonchoice - 1) +3])
            while True:
                movechoice = input("What move do you want to use? Please type 1 for the first move or 2 for the second move: ")
                if movechoice == "1" or movechoice == "2":
                    break
                else:
                    print("Invalid Choice. Try again!")
            print()
            if movechoice == "1":
                print(userfakemonName, "used", currentstarterMoves[fakemonchoice - 1],"and it dealt", startermoveDamage[fakemonchoice - 1], "damage!")
                wildfakemonHP = wildfakemonHP - startermoveDamage[fakemonchoice - 1]
                if wildfakemonHP <= 0:
                    print("The wild", wildFakemon ,"has died!")
                    xp_gain = random.randint(100, 450)
                    player_xp = player_xp + xp_gain
                    print("You have gained", xp_gain, "xp!")
                    print("Total XP: ", player_xp)
                    print()
                    break
            else:
                print(userfakemonName, "used", currentstarterMoves[(fakemonchoice - 1) + 3],"and it dealt", startermoveDamage[(fakemonchoice - 1) + 3], "damage!")
                wildfakemonHP = wildfakemonHP - startermoveDamage[(fakemonchoice - 1) + 3]
                if wildfakemonHP <= 0:
                    print("The wild", wildFakemon ,"has died!")
                    xp_gain = random.randint(100, 450)
                    player_xp = player_xp + xp_gain
                    print("You have gained", xp_gain, "xp!")
                    print("Total XP: ", player_xp)
                    print()
                    break
            print("It is your opponents turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(wildFakemon, "used", combinedMoves[random_num_move_damage],"and it dealt", combinedDamage[random_num_move_damage], "damage!")
            userfakemonHP = userfakemonHP - combinedDamage[random_num_move_damage]
            if userfakemonHP <=0:
                print("Your Fakemon has died!")
                del currentFakemon[fakemonchoice - 1]
                del startermoveDamage [fakemonchoice - 1]
                del startermoveDamage [(fakemonchoice - 1) + 3]
                del fakemon_hps [fakemonchoice - 1]
                print("Your team is now:", currentFakemon)
                print()
                break
    else:
        while wildfakemonHP >= 0 or userfakemonHP >= 0:
            print("It is your opponents turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(wildFakemon, "used", combinedMoves[random_num_move_damage],"and it dealt", combinedDamage[random_num_move_damage], "damage!")
            userfakemonHP = userfakemonHP - combinedDamage[random_num_move_damage]
            if userfakemonHP <=0:
                print("Your Fakemon has died!")
                del currentFakemon[fakemonchoice - 1]
                del startermoveDamage [fakemonchoice - 1]
                del startermoveDamage [(fakemonchoice - 1) + 3]
                del fakemon_hps [fakemonchoice - 1]
                print("Your team is now:", currentFakemon)
                print()
                break
            print("It is your turn!")
            print()
            print("Moves Available: ")
            print(currentstarterMoves[fakemonchoice - 1])
            print(currentstarterMoves[(fakemonchoice - 1) +3])
            while True:
                movechoice = input("What move do you want to use? Please type 1 for the first move or 2 for the second move: ")
                if movechoice == "1" or movechoice == "2":
                    break
                else:
                    print("Invalid Choice. Try again!")
            print()
            if movechoice == "1":
                  print(userfakemonName, "used", currentstarterMoves[fakemonchoice - 1],"and it dealt", startermoveDamage[fakemonchoice - 1], "damage!")
                  wildfakemonHP = wildfakemonHP - startermoveDamage[fakemonchoice - 1]
                  if wildfakemonHP <= 0:
                      print("The wild", wildFakemon ,"has died!")
                      xp_gain = random.randint(100, 450)
                      player_xp = player_xp + xp_gain
                      print("You have gained", xp_gain, "xp!")
                      print("Total XP: ", player_xp)
                      print()
                      break
            else:
                print(userfakemonName, "used", currentstarterMoves[(fakemonchoice - 1) + 3],"and it dealt", startermoveDamage[(fakemonchoice - 1) + 3], "damage!")
                wildfakemonHP = wildfakemonHP - startermoveDamage[(fakemonchoice - 1) + 3]
                if wildfakemonHP <= 0:
                    print("The wild", wildFakemon ,"has died!")
                    xp_gain = random.randint(100, 450)
                    player_xp = player_xp + xp_gain
                    print("You have gained", xp_gain, "xp!")
                    print("Total XP: ", player_xp)
                    print()
                    break

def secondMove(usersFakemon): #assigns second move at level 3 to each of the users Fakemon, making sure the fakemon does not recieve the same move 
    import random
    global everyFakemon
    global everyfakemonSkillset
    
    global metalMoves
    global wildMoves
    global oceanMoves
    global solarMoves
    global explosiveMoves
    global shadowMoves

    global currentstarterMoves

    global secondmoveSelected #variable used to indicte to use battletwoMove() instead of battleoneMove() in main
    
    for i in range(len(usersFakemon)):
        index = everyFakemon.index(usersFakemon[i])
        if everyfakemonSkillset[index] == "Metal":
            movelearned = metalMoves[random.randint(0,4)]
            while movelearned == currentstarterMoves[i]:
                movelearned = metalMoves[random.randint(0,4)]
            currentstarterMoves.insert(i+3, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
        elif everyfakemonSkillset[index] == "Wild":
            movelearned = wildMoves[random.randint(0,6)]
            while movelearned == currentstarterMoves[i]:
                movelearned = wildMoves[random.randint(0,6)]
            currentstarterMoves.insert(i+3, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)              
        elif everyfakemonSkillset[index] == "Ocean":
            movelearned = oceanMoves[random.randint(0,3)]
            while movelearned == currentstarterMoves[i]:
                movelearned = oceanMoves[random.randint(0,3)]
            currentstarterMoves.insert(i+3, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)                  
        elif everyfakemonSkillset[index] == "Solar":
            movelearned = solarMoves[random.randint(0,3)]
            while movelearned == currentstarterMoves[i]:
                movelearned = solarMoves[random.randint(0,3)]
            currentstarterMoves.insert(i+3, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
        elif everyfakemonSkillset[index] == "Explosive":
            movelearned = explosiveMoves[random.randint(0,7)]
            while movelearned == currentstarterMoves[i]:
                movelearned = explosiveMoves[random.randin(0,7)]
            currentstarterMoves.insert(i+3, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
        elif everyfakemonSkillset[index] == "Shadow":
            movelearned = shadowMoves[random.randint(0,5)]
            while movelearned == currentstarterMoves[i]:
                movelearned = shadowMoves[random.randint(0,5)]
            currentstarterMoves.insert(i+3, movelearned)
            print(usersFakemon[i],"has randomly learnt", movelearned)
    print("Your teams moves are now:")
    print(currentstarterMoves)
    secondmoveSelected = True
    

def minionBattle(): 
    import random
    global everyFakemon
    global currentFakemon
    global fakemon_hps
    
    for i in range(len(fakemon_hps)):
            fakemon_hps[i] = fakemon_hps[i] + random.randint(15,35)
    
    global currentstarterMoves
    global startermoveDamage
    global combinedMoves
    global combinedDamage
    global player_xp

    minions = ["Ryan Uzumaki", "Ashton Laos", "Alex Ketchum"]
    minionchoice = random.randint(0,2)

    print("Due to your rapid level advancements, you will be fighting one of Team Dauntless's minions! The minions name is: ", minions[minionchoice])
    print("The healths of your Fakemon have also increased to: ", fakemon_hps)
    print()

    wildFakemon = everyFakemon[random.randint(0,29)]
    wildfakemonHP = random.randint(200,325) #minions fakemon has higher range than wild fakemon
    print("The minions", wildFakemon ,"has appeared!")
    print("The", wildFakemon ,"has", wildfakemonHP ,"hp.")
    print()
    print("Your current team: ", currentFakemon)
    print("HP's: ", fakemon_hps)
    while True:
        fakemonchoice = input("What Fakemon do you want to use in this battle? Please type their position number: ")
        if len(currentFakemon) == 3:
            if fakemonchoice == "1" or fakemonchoice == "2" or fakemonchoice == "3":
                break
            else:
                print("Invalid Choice. Try again!")
        elif len(currentFakemon) == 2:
            if fakemonchoice == "1" or fakemonchoice == "2":
                break
            else:
                print("Invalid Choice. Try again!")
        elif len(currentFakemon) == 1:
            if fakemonchoice == "1":
                break
            else:
                print("Invalid Choice. Try again!")
    fakemonchoice = int(fakemonchoice)
    userfakemonName = currentFakemon[fakemonchoice - 1]
    userfakemonHP = fakemon_hps[fakemonchoice - 1]
    print("Lets now decide whos turn will come first via a coin flip! ")
    print()
    if flip_coin() == "Heads":
        while wildfakemonHP >= 0 or userfakemonHP >= 0:
            print("It is your turn!")
            print()
            print("Moves Available: ")
            print(currentstarterMoves[fakemonchoice - 1])
            print(currentstarterMoves[(fakemonchoice - 1) +3])
            while True:
                movechoice = input("What move do you want to use? Please type 1 for the first move or 2 for the second move: ")
                if movechoice == "1" or movechoice == "2":
                    break
                else:
                    print("Invalid Choice. Try again!")
            print()
            if movechoice == "1":
                print(userfakemonName, "used", currentstarterMoves[fakemonchoice - 1],"and it dealt", startermoveDamage[fakemonchoice - 1], "damage!")
                wildfakemonHP = wildfakemonHP - startermoveDamage[fakemonchoice - 1]
                if wildfakemonHP <= 0:
                    print("The minions", wildFakemon ,"has died!")
                    xp_gain = random.randint(150, 500) #xp gain has higher range in minion battle
                    player_xp = player_xp + xp_gain
                    print("You have gained", xp_gain, "xp!")
                    print("Total XP: ", player_xp)
                    print()
                    break
            else:
                print(userfakemonName, "used", currentstarterMoves[(fakemonchoice - 1) + 3],"and it dealt", startermoveDamage[(fakemonchoice - 1) + 3], "damage!")
                wildfakemonHP = wildfakemonHP - startermoveDamage[(fakemonchoice - 1) + 3]
                if wildfakemonHP <= 0:
                    print("The minions", wildFakemon ,"has died!")
                    xp_gain = random.randint(150, 500)
                    player_xp = player_xp + xp_gain
                    print("You have gained", xp_gain, "xp!")
                    print("Total XP: ", player_xp)
                    print()
                    break
            print("It is your opponents turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(wildFakemon, "used", combinedMoves[random_num_move_damage],"and it dealt", combinedDamage[random_num_move_damage], "damage!")
            userfakemonHP = userfakemonHP - combinedDamage[random_num_move_damage]
            if userfakemonHP <=0:
                print("Your Fakemon has died!")
                del currentFakemon[fakemonchoice - 1]
                del startermoveDamage [fakemonchoice - 1]
                del startermoveDamage [(fakemonchoice - 1) + 3]
                del fakemon_hps [fakemonchoice - 1]
                print("Your team is now:", currentFakemon)
                print()
                break
    else:
        while wildfakemonHP >= 0 or userfakemonHP >= 0:
            print("It is the minions turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(wildFakemon, "used", combinedMoves[random_num_move_damage],"and it dealt", combinedDamage[random_num_move_damage], "damage!")
            userfakemonHP = userfakemonHP - combinedDamage[random_num_move_damage]
            if userfakemonHP <=0:
                print("Your Fakemon has died!")
                del currentFakemon[fakemonchoice - 1]
                del startermoveDamage [fakemonchoice - 1]
                del startermoveDamage [(fakemonchoice - 1) + 3]
                del fakemon_hps [fakemonchoice - 1]
                print("Your team is now:", currentFakemon)
                print()
                break
            print("It is your turn!")
            print()
            print("Moves Available: ")
            print(currentstarterMoves[fakemonchoice - 1])
            print(currentstarterMoves[(fakemonchoice - 1) +3])
            while True:
                movechoice = input("What move do you want to use? Please type 1 for the first move or 2 for the second move: ")
                if movechoice == "1" or movechoice == "2":
                    break
                else:
                    print("Invalid Choice. Try again!")
            print()
            if movechoice == "1":
                  print(userfakemonName, "used", currentstarterMoves[fakemonchoice - 1],"and it dealt", startermoveDamage[fakemonchoice - 1], "damage!")
                  wildfakemonHP = wildfakemonHP - startermoveDamage[fakemonchoice - 1]
                  if wildfakemonHP <= 0:
                      print("The minions", wildFakemon ,"has died!")
                      xp_gain = random.randint(100, 450)
                      player_xp = player_xp + xp_gain
                      print("You have gained", xp_gain, "xp!")
                      print("Total XP: ", player_xp)
                      print()
                      break
            else:
                print(userfakemonName, "used", currentstarterMoves[(fakemonchoice - 1) + 3],"and it dealt", startermoveDamage[(fakemonchoice - 1) + 3], "damage!")
                wildfakemonHP = wildfakemonHP - startermoveDamage[(fakemonchoice - 1) + 3]
                if wildfakemonHP <= 0:
                    print("The minions", wildFakemon ,"has died!")
                    xp_gain = random.randint(100, 450)
                    player_xp = player_xp + xp_gain
                    print("You have gained", xp_gain, "xp!")
                    print("Total XP: ", player_xp)
                    print()
                    break
                
def leaderBattle():
    import random
    global everyFakemon
    global currentFakemon
    global fakemon_hps
    
    global currentstarterMoves
    global startermoveDamage
    global combinedMoves
    global combinedDamage
    global player_xp

    global trainer_name

    print("As you traverse through the treacherous mountains of the Astaria region, you stumble upon a mysterious cave. As you enter, you are greeted by a deafening roar that echoes through the cavern. Suddenly, the cave is illuminated by a bright light, revealing a massive figure standing before you. It's none other than the legendary Fokémon, Fakesaurus Rex! With a thunderous stomp, Fakesaurus Rex steps forward, ready to engage in an epic battle. And behind Fakesaurus Rex stands the leader of Team Dauntless, Dylan Huggies. You know that this battle will be no easy feat, but you are determined to prove your worth as a Trainer. You take a deep breath, steeling yourself for what's to come. It's time to show Fakesaurus Rex and Dylan what you and your Fakémon are made of.")
    print()
    print("However, a sudden shift in the air alerts you to the presence of another powerful Fakémon. You turn to see a legendary Fakemon, the mighty Formidsax, standing before you. Formidsax unleashes a powerful roar, ready to join the battle at a moment's notice and on your side against Dylan and Fakesaurus Rex. You also sense a newfound determination to succeed with Formidsax. With your trusted new Fakemon by your side and a fierce determination in your heart, you steel yourself for the fight to come. As Fakesaurus Rex readies itself for battle, you take a deep breath and prepare for what promises to be an epic showdown. Will you emerge victorious and prove yourself as a true master of Fakémon battles and take back the region of Astaria from Dylan, or will Fakesaurus Rex prove too much for you to handle? Only time will tell as the battle begins.")
    print()
    
    wildFakemon = "Fakesaurus Rex"
    wildfakemonHP = random.randint(500,600)

    userfakemonName = "Formidsax"
    userfakemonHP = random.randint(500,600)
    
    print("This will be the all or nothing showdown between:")
    print(trainer_name ,"and Dylan Huggies")
    print("Formidsax and Fakesaurus Rex")
    print("Since both of these Fakemon are legendary, they will have random moves from all the 6 skillsets with different random damage numbers!")
    print()
    input("Please press <Enter> to continue!") #added an input statement so that there could be a pause for the user (added after running the output)


    legendaryDamages = []
    for i in range(len(combinedDamage)):
                   legendaryDamages.append(random.randint(80,120)) #legendary fakemon range of damage

    print("Dylan's", wildFakemon ,"has", wildfakemonHP ,"hp.")
    print("Your", userfakemonName ,"has", userfakemonHP ,"hp.")
    print("Lets now decide whos turn will come first via a coin flip! ")
    print()
    if flip_coin() == "Heads":
        while wildfakemonHP >= 0 or userfakemonHP >=0:
            print("It is your turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(userfakemonName, "used", combinedMoves[random_num_move_damage],"and it dealt", legendaryDamages[random_num_move_damage], "damage!")
            wildfakemonHP = wildfakemonHP - legendaryDamages[random_num_move_damage]
            if wildfakemonHP <= 0:
                print("Dylan's", wildFakemon ,"has died!")
                xp_gain = 1000000
                player_xp = xp_gain + 1000000
                print("You have gained", xp_gain, "xp!")
                print("Total XP: ", player_xp)
                print()
                return True
            print("It is your opponents turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(wildFakemon, "used", combinedMoves[random_num_move_damage],"and it dealt", legendaryDamages[random_num_move_damage], "damage!")
            userfakemonHP = userfakemonHP - legendaryDamages[random_num_move_damage]
            if userfakemonHP <=0:
                print("Your Fakemon has died!")
                print()
                return False
    else:
        while wildfakemonHP >= 0 or userfakemonHP >=0:
            print("It is your opponents turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(wildFakemon, "used", combinedMoves[random_num_move_damage],"and it dealt", legendaryDamages[random_num_move_damage], "damage!")
            userfakemonHP = userfakemonHP - legendaryDamages[random_num_move_damage]
            if userfakemonHP <=0:
                print("Your Fakemon has died!")
                print()
                return False
            print("It is your turn!")
            random_num_move_damage = random.randint(0,33) #34 moves and 34 damage numbers that the opponent randomly chooses from
            print(userfakemonName, "used", combinedMoves[random_num_move_damage],"and it dealt", legendaryDamages[random_num_move_damage], "damage!")
            wildfakemonHP = wildfakemonHP - legendaryDamages[random_num_move_damage]
            if wildfakemonHP <= 0:
                print("Dylan's", wildFakemon ,"has died!")
                xp_gain = 1000000
                player_xp = xp_gain + 1000000
                print("You have gained", xp_gain, "xp!")
                print("Total XP: ", player_xp)
                print()
                return True
            
def main():
    repeat = "y"
    while repeat == "y" or repeat == "yes":
        import random #random.randint()

        #Global Variables
        global trainer_name #name of player

        #global fakeCoins #num of fake coins (currency to use at fake center) #not complete
        #global perfectoBalls #num of perfecto balls (catch rate: 100% - cost 3000 fake coincs) #not complete

        global currentFakemon #list of the players fakemon
        currentFakemon = [] 
        global currentstarterMoves #list of moves of the players fakemon
        currentstarterMoves = []
        global startermoveDamage #list of damages of users moves
        startermoveDamage = []

        global everyFakemon #list of every Fakemon in this game
        everyFakemon = ["Meguium", "Dolphoom", "Blastaroo", "Warpecker", "Kingray", "Dragomite", "Octopup", "Scorpike", "Ironoyote", "Venomarak", "Flamemite", "Moltena", "Wolvesion", "Pandaw", "Flacross", "Lemitar", "Hyenairy", "Doomhopper", "Chimemeleon", "Caterpixie", "Falcion", "Bonehawk", "Pigloo", "Chimpanther", "Monkeye", "Hippocross", "Rhinoth", "Voltopotamus", "Steelaby", "Ashking"]

        global everyfakemonSkillset #list of every Fakemon's skillset
        everyfakemonSkillset = []
        for i in range (len(everyFakemon)): #randomly gives each Fakemon listed above a skillset
            everyfakemonSkillset.append(skillset_random())

        global metalMoves #metal skillset moves
        metalMoves = ["Meteor Mash", "Steel Punch", "Draco Meteor", "Iron Forge", "Wrecking Ball"]
        global metalDamage
        metalDamage = []
        for i in range (len(metalMoves)): #creates damage numbers for moves
            metalDamage.append(random.randint(40,85))
        
        global wildMoves #wild skillset moves
        wildMoves = ["Fire Dance", "Blazing Storm", "Fire Circle", "Magma Storm", "Heat Wave", "Flame Punch", "Flame Storm"]
        global wildDamage
        wildDamage = []
        for i in range (len(wildMoves)): #creates damage numbers for moves
            wildDamage.append(random.randint(40,85))
        
        global oceanMoves #ocean skillset moves
        oceanMoves = ["Hydro Pump", "Tsunami", "Water Bomb", "Hydro Vortex"]
        global oceanDamage
        oceanDamage = []
        for i in range (len(oceanMoves)):#creates damage numbers for moves
            oceanDamage.append(random.randint(40,85))
        
        global solarMoves #solar skillset moves
        solarMoves = ["Solar Beam", "Solar Cooling", "Bullet Seed", "Energy Ball"]
        global solarDamage
        solarDamage = []
        for i in range (len(solarMoves)):#creates damage numbers for moves
            solarDamage.append(random.randint(40,85))
        
        global explosiveMoves #explosive skillset moves
        explosiveMoves = ["Explosion", "Bullet Bill", "Power Surge", "Sphere of Destruction", "Blast", "Detonation", "Bursting Dash", "Surge"]
        global explosiveDamage
        explosiveDamage = []
        for i in range (len(explosiveMoves)):#creates damage numbers for moves
            explosiveDamage.append(random.randint(40,85))
        
        global shadowMoves #shadow skillset moves
        shadowMoves = ["Shadow Bomb", "Nightmare", "Shadow Blast", "Shadow Ball", "Creep", "Taunt"]
        global shadowDamage
        shadowDamage = []
        for i in range (len(shadowMoves)): #creates damage numbers for moves
            shadowDamage.append(random.randint(40,85))

        global combinedMoves #all the skillset moves combined (will be used by opponents!) damage of their moves is slightly less than users to create some sort of advantage
        combinedMoves = metalMoves + wildMoves + oceanMoves + solarMoves + explosiveMoves + shadowMoves

        global combinedDamage #all the skillset moves damages combined (will be used by opponents!) damage of their moves is slightly less than users to create some sort of advantage
        combinedDamage = metalDamage + wildDamage + oceanDamage + solarDamage + explosiveDamage + shadowDamage

        global player_xp #how the player_level increases
        player_xp = 0
        
        global fakemon_hps #list of current healths of every Fakemon the user has - generated randomly

        global secondmoveSelected #used to tell main that second move has been selected or not
        secondmoveSelected = False #user only has one move per fakemon until level 3

        if introInfo() == False:
            print("Maybe you will be ready another time!")
            print()
            repeat = "q"
        else:
            print("--------------------------------------------------------------------------------------------")
            gameRules(trainer_name)
            print()
            print("Now that you are officially ready to begin your adventure, you can go into the wilderness and Battle other Fakemon or trainers! We will meet again soon", trainer_name ,"- Professor Oak")
            print("--------------------------------------------------------------------------------------------")
            while len(currentFakemon) > 0 and secondmoveSelected == False:
                battleoneMove()
                if len(currentFakemon) == 0:
                    print("All your Fakemon have died. Game over!")
                    print()
                    break
                #level checker - 250 (level 2), 1000 (level 3), 1600 (level 4) , 2100 (level 5), 2600 (level 6), 3200 (level 7), 3800 (level 8), 4400 (level 9), and 5000 (level 10).
                elif player_xp >= 250 and player_xp <= 1000:
                    print("Level 2 Achieved!")
                    print()
                elif player_xp >= 1000 and player_xp <= 1600:
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print()
                    secondMove(currentFakemon)
                    print()
                elif player_xp >= 1600 and player_xp <= 2100: #level 4
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print("Level 4 Achieved!")
                    print()
            while len(currentFakemon) > 0 and secondmoveSelected == True:
                battletwoMove()
                if len(currentFakemon) == 0:
                    print("All your Fakemon have died. Game over!")
                    print()
                    break
                elif player_xp >= 1600 and player_xp <= 2100: #level 4
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print("Level 4 Achieved!")
                    print()
                elif player_xp >= 2100 and player_xp <= 2600:
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print("Level 4 Achieved!")
                    print("Level 5 Achieved!")
                    print()
                    minionBattle()
                    print()
                elif player_xp >= 2600 and player_xp <= 3200:
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print("Level 4 Achieved!")
                    print("Level 5 Achieved!")
                    print("Level 6 Achieved!")
                    print()
                elif player_xp >= 3200 and player_xp <= 3800:
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print("Level 4 Achieved!")
                    print("Level 5 Achieved!")
                    print("Level 6 Achieved!")
                    print("Level 7 Achieved!")
                    print()
                    minionBattle()
                    print()
                elif player_xp >= 3800 and player_xp <=4400:
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print("Level 4 Achieved!")
                    print("Level 5 Achieved!")
                    print("Level 6 Acheived!")
                    print("Level 7 Achieved!")
                    print("Level 8 Achieved!")
                    print()
                elif player_xp >= 4400 and player_xp <=5000:
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print("Level 4 Achieved!")
                    print("Level 5 Achieved!")
                    print("Level 6 Achieved!")
                    print("Level 7 Achieved!")
                    print("Level 8 Achieved!")
                    print("Level 9 Achieved!")
                    print()
                    minionBattle()
                    print()
                elif player_xp >= 5000:
                    print("Level 2 Achieved")
                    print("Level 3 Achieved!")
                    print("Level 4 Achieved!")
                    print("Level 5 Achieved!")
                    print("Level 6 Achieved!")
                    print("Level 7 Achieved!")
                    print("Level 8 Achieved!")
                    print("Level 9 Achieved!")
                    print("Level 10 Achieved!")
                    print()
                    if leaderBattle() == True:
                        print("Congratulations you have won against the Leader of Team Dauntless and have taken back the region of Astaria.")
                        print()
                        print("As the sun sets over the horizon, you are approached by Professor Oak. He congratulates you on your victory and tells you that you have become a true Pokemon Master. He also hands you a new Pokedex, which he has been working on. This Pokedex has the ability to detect and track all the legendary Pokemon in the region. With your new Pokedex in hand, you set out on a new adventure to catch all the legendary Pokemon. Who knows what challenges and obstacles lie ahead, but one thing is for sure - you are ready for whatever comes your way. Is this the end... or is it just the beginning?")
                        break
                    else:
                        print("You have lost against Team Dauntless and unfortunately, this is where your journey ends!")
                        print()
                        break
                
        repeat = input("Do you want to play again? Please type y/yes or q/quit: ").lower()
        if repeat == "y" or repeat == "yes" :
            print("Restarting...")
            print("--------------------------------------------------------------------------------------------")
        elif repeat == "q" or repeat == "quit":
            print("The game and program is now over. Thank you for playing!")
            print("©2023 Awais Razaque, awaisrazaque05@gmail.com. All rights reserved.") #copyright notice is displayed when user quits
            print()
            input("Press <Enter> to quit the program!")

main()
