# St. Justice Youngblood
# 7/10/25 - 7/12/25
# P5HW
# Desc: This program will allow a user to choose a character class to fight a boss,
# along with being supported by two AI teammates. 

import random

#-- Hello and Goodbye Statements. Status: Done
def welcomeStatement():
    # Welcoming statement
    print("\nWelcome to <Get Lucky>")
    
    # Explain the game to the user and allow them to pick a class.
    print("\n----------------------------------------------------------------------------------------------------------------")
    print("You are tasked with fighting a boss.")
    print("You will be assisted by two other squadmates. Defeat the boss to win the game.")

    return

def victoryStatement(boss):
    # Checks to see if the boss is dead
    if boss["Health"] < 1:
        boss["Status"]  = "Dead"
        print("✅Congratulations! The boss has been defeated.")
        print("🥂You Win: ")
        print("💵$8000 Charge in property damage!")
        print("🦺 An Osha Complaint!")
        print("🪜 A broken ladder!")
        print()
    return

def failureStatement():
    print("How the mighty have fallen...")
    print("You and your team return back to base to recuperate...")
    return

def farewellStatement():
    print("Thank you for playing Get Lucky. God Bless and Farewell.")
    return

#-- User and Team Attributes / Info. Status: Done
def classAttributes(userClass):
    
    userClassInfo = userClass

    # Class Attributes and Info 
    
    brusierAttributes = {
        # Unavailable for DEMO
        "Name": "Brusier",
        "Health": "160",
        "Attack": "60",
        "InfoUsage": "Energy-Reliant [Attacks require energy usage. Starting energy is 15, increases every turn.]",
        "InfoAttack": "Short variety of attacks."
    }
    healerAttributes = {
        # Unavailable for DEMO
        "Name": "Healer",
        "Health": "150",
        "Attack": "20",
        "InfoUsage": "Knowledge-Reliant [To use any ability, you must answer a random question.]",
        "InfoAttack": "Able to heal and buff team stats and deal minor damage."
    }
    luckyAttributes = {
        "Name": "Lucky",
        "Health": 77,
        "Attack": "RNG Based",
        "Info": "Luck-Reliant [Rolls a random number, your attack damage will depend on the number's range.]",
        "InfoAttack": "Attacks rely solely on RNG (Random chance)."
    }

    # Returns classes for variable assignment

    if userClass == 1: # FOR LUCKY
        return {
        "Name": "Lucky",
        "Health": 77,
        "Attack": "RNG Based",
        "Info": "Luck-Reliant [Rolls a random number, your attack damage will depend on the number's range.]",
        "InfoAttack": "Attacks rely solely on RNG (Random chance).",
        "Status": "Alive"
    }

    # Checks to see if user input is valid to check the class
    if userClass >= 0 and userClass <= 3:
        return
    
    # Displays class information
    if userClassInfo == 4:
        # For Lucky
        print(f"Name:  {luckyAttributes['Name']}")
        print(f"Usage: {luckyAttributes['Info']}")
        print(f"------ {luckyAttributes['InfoAttack']}")
        print(f"Health stat: {luckyAttributes['Health']}")
        print(f"Attack stat: {luckyAttributes['Attack']}")

    return

def teamAttributes():
    
    # Medic Attributes
    medicAttributes = {
        "Name": "Medic",
        "Health": 100,
        "Attack": 20,
       
        "Info General": "[Can heal a selected party member (Only one at a time)]",
        "Info Attack": "[Deals small damage]",
        "Info Fail": "[Runs away if last member standing]",
        
        "Move #1": "+20 HP For a single teammate",
        "Move #2": "20 DMG - Inconvenient appointment scheduling",
        "Status": "Alive"
    }
    # Soldier Attributes
    soldierAttributes = {
        "Name": "Soldier",
        "Health": 150,
        "Attack": 50,
        "Info Attack": "Mid damage output",
        "Move #2": "Activates a rocket launcher upon gaining enough energy. Requires a coin flip to use.",
        "Info #2": "Heads the rocket hits, dealing large scale damage. Tails, the rocket doesn't fire.",
        "Move #1": "50 DMG - Basic Training",
        "Status": "Alive"
    }

    # Sets up team layout
    teamCall = {
        "medic": medicAttributes,
        "soldier": soldierAttributes
    }

    # Display info for teammates
    print("Here is your team's information.")
    print("--------------------------------")
    # For Medic
    print(f"Name: {medicAttributes['Name']}")

    print(f"Usage: {medicAttributes['Info General']}")
    print(f"-----: {medicAttributes['Info Attack']}")
    
    print(f"Health stat: {medicAttributes['Health']}")
    print(f"Attack stat: {medicAttributes['Attack']}")
    print()

    # For Soldier 
    print(f"Name: {soldierAttributes['Name']}")
    print(f"Usage: {soldierAttributes['Info Attack']}")
    
    print(f"Ultimate: {soldierAttributes['Move #2']}")
    print(f"--------: {soldierAttributes['Info #2']}")
    print(f"Normal Attack: {soldierAttributes['Move #1']}")

    print(f"Health stat: {soldierAttributes['Health']}")
    print(f"Attack stat: {soldierAttributes['Attack']}")

    print()

    return teamCall

# Teammate stat returns (ATTACHED TO ATTRIBUTES)
def medicReturn():
    return {
        "Name": "Medic",
        "Health": 100,
        "Attack": 20,
        "Info General": "[Can heal a selected party member (Only one at a time)]",
        "Info Attack": "[Deals small damage]",
        "Info Fail": "[Runs away if last member standing]",
        "Move #1": "+20 HP For a single teammate",
        "Move #2": "20 DMG - Inconvenient appointment scheduling",
        "Status": "Alive"
    }

def soldierReturn():
        return {
        "Name": "Soldier",
        "Health": 150,
        "Attack BasicTraining": 50,
        "Attack RocketLauncher": 200, 
        "Info Attack": "Mid damage output",
        "Move #2": "Activates a rocket launcher upon gaining enough energy. Requires a coin flip to use.",
        "Info #2": "Heads the rocket hits, dealing large scale damage. Tails, the rocket doesn't fire.",
        "Move #1": "50 DMG - Basic Training",
        "Status": "Alive"
    }

    
#-- Boss Info   
def bossAttributes():

    return {
        "Name": "8 ft. Fiberglass Step Ladder",
        "Health": 500,
        "Attack Ladder Fold": 20,
        "Attack Finger Jam": 30, 
        "Defense": "OSHA Approved Safety Ladder: -10 Incoming DMG", # - Subtracts incoming damage
        "Status": "Alive"
    }

#-- Class Select - Done
def classSelectStatement():
    # Displays available classes and an exit option (Attached to classSelect).
    print("\nEnter 0 if you wish to end the program.")
    print("---------------------------------------")
    print("1) Lucky [77 HP, RNG ATK, Luck-Reliant] (Enter '4' for more info)")
    print("2) [DEMO]")
    print("3) [DEMO]")
    print()
    print("Type 1 select available classes. Type 4 to check info.")    

    return 
def classSelect():
    # Get the user's input.
    userClass = int(input("Enter your selection: "))
    print()
    if (userClass == 0):
        # End's classSelect function if user input is 0.
        return userClass  
    while (userClass != 1) and (userClass != 4): 
        if (userClass != 1) and (userClass != 4):
            # Asks for a new input if the user's input is out of range. 
            print("Invalid selection, please re-enter your selection.")
            userClass = int(input("Enter your selection again: "))
            print()

    
    return userClass    

#-- Battle: Introduction 
def battleIntroStatement():
    print("As you approach the target's destination, a sense of unease sets in.")
    print("Neither you or your teammates know what lies ahead, and victory is uncertain.")
    print()
    print("Without warning, the boss appears.")
    print("You and your teammates prepare to fight.")
    print()

#-- Battle: Turns

def luckyTurn(userChar, boss):
    name = userChar["Name"]
    bossName = boss["Name"]

    # Checks to see if the boss or character is dead
    if userChar["Health"] <= 0:
        userChar["Status"] = "Dead"
        return userChar["Status"]
    
    if boss["Health"] <= 0:
        boss["Status"] = "Dead"
        return boss["Status"]

    # Current character turn intro
    print(f"\n{name} is up to bat.")
    
    # User attacks the boss
    print("Your HP: ", userChar["Health"])
    print("What do you wish to do?")
    print("1 (Coin Throw) - Roll For Attack")
    print("2 (Walk it off) - Roll For Health")
    print()

    userAction = int(input("Im feeling lucky number... "))
    if userAction > 2 or userAction < 0:
        print("Hmm...That ain't a good number, let's try 1 or 2...")
        print("1 (Coin Throw) - Roll For Attack")
        print("2 (Walk it off) - Roll For Health")
        print()
        userAction = int(input("Im feeling lucky number... "))
    print("-----------------------------------------")
    print()
    if userAction == 1:
        rollAttack = random.randint(1, 1500)
        if rollAttack == 1:
            print(f"You rolled a . . . {rollAttack}")
            print(f"You rolled a 1 out of 1500. Honestly, I don't even know what to say. That is very unfortunate.")
            print()

        elif rollAttack <= 499 and rollAttack >= 2:
            print(f"You rolled: {rollAttack}")
            print(f"Sadly, you lost your lucky coin. Luckily, it hit the boss (Who is now angry).")
            print()
            boss["Attack Ladder Fold"] += 20
            boss["Attack Finger Jam"] += 20
            boss["Health"] -= 50

        elif rollAttack >= 500 and rollAttack <= 999:
            print(f"You rolled: {rollAttack}")
            print(f"You give the boss a winning lottery ticket, but taxes takes away a good majority of it.")
            print(f"You deal 100 (Emotional) DMG.")
            print()
            boss["Health"] -= 100
        
        elif rollAttack >= 1000 and rollAttack <= 1449:
            print(f"You rolled: {rollAttack}")
            print(f"Your coin lands a direct hit on the boss, you deal 200 DMG")
            print()
            boss["Health"] -= 200

        elif rollAttack >= 1450:
            print(f"You rolled: {rollAttack}")
            print(f"Must be your lucky day, you deal 500 DMG to the {bossName}")
            print()
            boss["Health"] -= 1000
            
    elif userAction == 2:
        rollHealth = random.randint(1, 1100)
        if rollHealth == 1:
            print(f"You rolled: {rollHealth}")
            print("You rolled a 1 out of 1100. Honestly, I don't even know what to say. That is very unfortunate.")
            print("You heal: ...1 HP")
            print("It's the thought that counts.")
            print()
            userChar["Health: 1 HP"]

        
        elif rollHealth <= 499 and rollHealth >= 2:
            print(f"You rolled: {rollHealth}")
            print("This is but a scratch. You toughen up through the pain.")
            print("You heal: 50 HP")
            print()
            userChar["Health"] += 50

        elif rollHealth >= 500 and rollHealth <= 749:
            print(f"You rolled: {rollHealth}")
            print("You drink some water and get back into the fray.")
            print("You heal: 100 HP.")
            print()
            userChar["Health"] += 100

        elif rollHealth >= 750 and rollHealth <= 999:
            print(f"You rolled: {rollHealth}")
            print("Tylenol really does fix everything...")
            print("You heal: 200 HP")
            print()
            userChar["Health"] += 200

        elif rollHealth >= 1000:
            print(f"You rolled: {rollHealth}")
            print("Sticks and stones may break my bones, but I refuse to pay a medical bill. You walk it off.")
            print("You heal: 300 HP")
            print()
            userChar["Health"] += 300

        

    # Boss HP View
    print(f"The Boss's HP is now {boss['Health']}")
    print("----------------------------------------------")
    
    return

def medicTurn(medic, boss, userChar, soldier):
    name = medic["Name"]


    # Checks to see if the boss or character is dead
    if medic["Health"] <= 0:
        medic["Status"] = "Dead"
        return medic["Status"]
    
    if boss["Health"] <= 0:
        boss["Status"] = "Dead"
        return boss["Status"]

    
    # Check for surrender
    if userChar["Status"] == "Dead" and soldier["Status"] == "Dead":
        print("The medic doesn't even bother, they return to base.")
        return

    # Current character turn intro
    print(f"\n{name} is up to bat.")
    print("Medic HP:", medic["Health"])
    # Healing abilities
    militaryStimShot = 20
    bandAid = 50

    # Create a random roll for the medic move
    
    medicRoll = random.randint(1, 3)
    if medicRoll == 1:
        # Random choice for healing the team
        healDecision = random.randint(1, 2)
        if healDecision == 1:
            # Chooses who to heal (using a random number)
            if soldier["Status"] == "Alive":

                medic["Health"] += bandAid
                soldier["Health"] += bandAid
                print("The medic healed themself and the soldier with a smiley face band-aid.")
                print("Soldier HP is now", soldier["Health"])
                print("Medic HP is now", medic["Health"])
                print()

            elif userChar["Status"] == "Alive":

                medic["Health"] += bandAid
                userChar["Health"] += bandAid
                print("The medic healed themself and", userChar["Name"], "with a smiley face band-aid.")
                print(userChar["Name"], "'s HP is now", userChar["Health"])
                print("Medic HP is now", medic["Health"])
                print()
                


        elif healDecision == 2:
            # Chooses who to heal. If both teammates are alive, the party is healed. (using a random number)
            if userChar["Status"] == "Alive" and soldier["Status"] == "Alive":
            # If full party is alive
                medic["Health"] += militaryStimShot
                userChar["Health"] += militaryStimShot
                soldier["Health"] += militaryStimShot
                print("The medic healed the full party with a stim-shot.")
                print("Soldier,", userChar["Name"], ", and the Medic gain 50 HP")
                print()
            
            elif userChar["Status"] == "Alive":
            # If User and Medic are alive
                medic["Health"] += militaryStimShot
                userChar["Health"] += militaryStimShot
                print("The medic healed themself and", userChar["Name"], "with a stim-shot.")
                print(userChar["Name"], "and the Medic gain 50 HP")
                print("Medic HP is now", medic["Health"])
                print()
                
            
            elif soldier["Status"] == "Alive":
            # If Soldier and Medic are alive
                medic["Health"] += militaryStimShot
                soldier["Health"] += militaryStimShot
                print("The medic healed themself and the soldier with a stim-shot.")
                print("Soldier and the Medic gain 50 HP")
                print("Medic HP is now", medic["Health"])
                print()

                
            
    elif medicRoll == 2:
        print("The medic casts: Inconvenient appointment scheduling.")
        print("Dealing 20 DMG")
        print()
        boss["Health"] -= 20

    elif medicRoll == 3:
        print("The medic is busy with an appointment, they will be back next turn. (Maybe)")
        print()


    # Boss HP View
    print(f"The Boss's HP is now {boss['Health']}")
    print("----------------------------------------------")
    
    return

def soldierTurn(soldier, boss):
    name = soldier["Name"]
    
    # Checks to see if the boss or character is dead
    if soldier["Health"] <= 0:
        soldier["Status"] = "Dead"
        return soldier["Status"]
    
    if boss["Health"] <= 0:
        boss["Status"] = "Dead"
        return boss["Status"]


    # Current character turn intro
    print(f"\n{name} is up to bat.")
    print("Soldier HP:", soldier["Health"])

    # Create a random roll for soldier move
    
    soldierRoll = random.randint(1, 2)
    if soldierRoll == 1:

        attackDecision = random.randint(1, 2)
        print(f"{name} prepares to fire a rocket launcher...")

        if attackDecision == 1:
            print("The soldier hits the boss dead-center.")
            print("Dealing ", soldier["Attack RocketLauncher"])
            print()
            boss["Health"] -= soldier["Attack RocketLauncher"]
            

        elif attackDecision == 2:
            print("The soldier completely misses.")
            print("The soldier now has a meeting with their commanding officer and will skip this turn.")
            print()
            
    elif soldierRoll == 2:
        print("The soldier uses: Basic Training.")
        print("Dealing 50 DMG")
        print()
        boss["Health"] -= soldier["Attack BasicTraining"]
        

    # Boss HP View
    print(f"The Boss's HP is now {boss['Health']}")
    print()
    print("----------------------------------------------")

    return

def bossLadderTurn(medic, boss, userChar, soldier):
    name = boss["Name"]

    # Checks to see if the boss is still alive
    if boss["Health"] <= 0:
        boss["Status"] = "Dead"
        return boss["Status"]
    
    # Current character turn intro
    print(f"{name} stands menacingly.")


    # Create a random roll for the attack move
    
    attackRoll = random.randint(1, 3)
    if attackRoll == 1:
        attackDecision = random.randint(1, 3)
        if attackDecision == 1:
            soldier["Health"] -= boss["Attack Ladder Fold"]
            print("The ladder folds and falls on top of the soldier")
            print("Soldier looses ", {boss["Attack Ladder Fold"]}, " HP!")
            print()

            # Checks to see if the character is dead from an attack
            if soldier["Health"] <= 0:
                soldier["Status"] = "Dead"
                return soldier["Status"]
            return
            

        elif attackDecision == 2:
            userChar["Health"] -= boss["Attack Ladder Fold"]
            print("The ladder folds and falls on top of ", userChar["Name"])
            print({userChar["Name"]}, " looses ", {boss["Attack Ladder Fold"]}, " HP!")
            print()
            # Checks to see if the character is dead from an attack
            if userChar["Health"] <= 0:
                userChar["Status"] = "Dead"
                return userChar["Status"]
            return

        elif attackDecision == 3:
            medic["Health"] -= boss["Attack Ladder Fold"]
            print("The ladder folds and falls on top of the Medic")
            print("Medic looses ", {boss["Attack Ladder Fold"]}, " HP!")
            # Checks to see if the character is dead from an attack
            if medic["Health"] <= 0:
                medic["Status"] = "Dead"
                return medic["Status"]
            return
            
    elif attackRoll == 2:
        attackDecision = random.randint(1, 3)
        if attackDecision == 1:
            soldier["Health"] -= boss["Attack Finger Jam"]
            print("Soldier tried to pick up the ladder without gloves and jammed their finger.")
            print("Soldier looses ", {boss["Attack Finger Jam"]}, " HP!")
            print()
            # Checks to see if the character is dead from an attack
            if soldier["Health"] <= 0:
                soldier["Status"] = "Dead"
                return soldier["Status"]
            return

        elif attackDecision == 2:
            userChar["Health"] -= boss["Attack Finger Jam"]
            print(userChar["Name"], " tried to pick up the ladder without gloves and jammed their finger.")
            print({userChar["Name"]}, " looses ", {boss["Attack Finger Jam"]}, " HP!")
            print()
            # Checks to see if the character is dead from an attack
            if userChar["Health"] <= 0:
                userChar["Status"] = "Dead"
                return userChar["Status"]
            return

        elif attackDecision == 3:
            medic["Health"] -= boss["Attack Finger Jam"]
            print("Medic tried to pick up the ladder without gloves and jammed their finger.")
            print("Medic looses ", {boss["Attack Finger Jam"]}, " HP!")
            print()
            # Checks to see if the character is dead from an attack
            if medic["Health"] <= 0:
                medic["Status"] = "Dead"
                return medic["Status"]
            return

    elif attackRoll == 3:
        print("The Boss charges for this turn...")
        print("Their health and attack power rises...")
        boss["Attack Finger Jam"] += 10
        boss["Attack Ladder Fold"] += 10 
        boss["Health"] += 100
        print()
        return

    return

#-- Battle: Boss Fight, Ladder

def bossFight(userChar, userChoice, medic, soldier, boss):
    # Boss Fight
    turnCounter = 1


    while (boss["Status"] == "Alive") and ((userChar["Status"] == "Alive") or (medic["Status"] == "Alive") or (soldier["Status"] == "Alive")):
        if boss["Health"] <= 0:
            boss["Status"] = "Dead"
            return boss["Status"]
        else: 
            print()
            print(f"The boss has...")
            print(boss["Health"], "HP remaining.")
            print()
            
            if boss["Health"] <= 0:
                boss["Status"] == "Dead"

            print(f"It is now turn {turnCounter}.")
            print("------------------------------")
            print()
            print("Team's turn")
            print("-----------")
            turnCounter = turnCounter + 1
            # -- Team's turn -- #
            if userChar["Health"] <= 0:
                userChar["Status"] = "Dead"
                print("Theres always next time (I think.)")
                print()
            else:
                if userChoice == 1:
                    luckyTurn(userChar, boss)

            if medic["Health"] <= 0:
                medic["Status"] = "Dead"
                print("The medic was too close to an apple and is no longer available for battle.")
                print()
            else:
                medicTurn(medic, boss, userChar, soldier)

            if soldier["Health"] <= 0:
                soldier["Status"] = "Dead"
                print("The soldier has firewatch and will no longer be in battle.")
                print()
            else:
                soldierTurn(soldier, boss)
            # -- Boss Turn -- #
            print()
            if boss["Health"] <= 0:
                boss["Status"] = "Dead"
                return boss["Status"] == "Dead"
            else:
                bossLadderTurn(medic, boss, userChar, soldier)
            print("Boss turn")
            print("---------")


    
    return

#-- Main - Done
def main():
    #       Opening statements        #
    # --------------------------------
    welcomeStatement()
    classSelectStatement()

    # User selects input.
    userClass = classSelect()
    userCurrentChar = classAttributes(userClass)
    
    #  Class select decision statements  #
    # --- For the user to get information and return to class, select --- #
    if userClass >= 4 and userClass <= 6:
        # Retrieves and displays class information from the attributes function
        classReturn = input("\nReturn to class select? (y/n): ")
        if classReturn == "y":
            # Allows the user to select their class or view more information. 
            classSelectStatement()
            userClass = classSelect()
            userCurrentChar = classAttributes(userClass)
        elif classReturn == "n": 
            print("Oh. Well bye then.")
            return 
    elif userClass == 0:
        # Ends the program, prints a goodbye message.
        farewellStatement()
        return


    #          Game starts             #
    # -------------------------------- #
    while userClass > 0 and userClass < 4:
        # Setting up Team
        medic = medicReturn()
        soldier = soldierReturn()
        boss = bossAttributes()
        userChoice = userClass

        # Introduction to the battle
        teamAttributes()
        battleIntroStatement()
        # Battle Sim Demo
        while (boss["Status"] == "Alive") and ((userCurrentChar["Status"] == "Alive") or (medic["Status"] == "Alive") or (soldier["Status"] == "Alive")):
            bossFight(userCurrentChar, userChoice, medic, soldier, boss)

        if (boss["Status"] == "Alive") and ((userCurrentChar["Status"] == "Dead") and (medic["Status"] == "Dead") and (soldier["Status"] == "Dead")):
            failureStatement() # Fail Statement if the team is fully defeated
            userClass = -1 # Exits the loop

        if (boss["Status"] == "Dead") and ((userCurrentChar["Status"] == "Alive") or (medic["Status"] == "Alive") or (soldier["Status"] == "Alive")):
            victoryStatement(boss)  # Victory Statement if the boss if defeated
            userClass = 777 # Exits the loop

    #           Game Ends              #
    # -------------------------------- #
    farewellStatement()




# End of program :D 
main()
