"""EX06: Choose your own adventure."""
__author__ = "730516365"


player: str = ""
bunny: str = "\U0001F407"
music: str = "\U0001F3B6"
inventory: dict[str, str] = dict()
points: int = 0
attack: int = 2
hp: int = 4
max_hp: int = 12
main_weapon: str = ""
main_armor: str = ""
chapter: int = 0
boss: str = ""
boss_weapon: str = ""

def menu() -> int:
    """Show the menu of the game."""
    global chapter
    global player
    global inventory
    global points
    global attack
    global hp
    global max_hp
    global boss
    print(f"Welcome to the Wonderland Menu, {player}.")
    print(f"Inventory: {inventory}")
    print(f"Points: {points}")
    print(f"Health: {hp}/{max_hp}")
    print(f"Attack power: {attack}")
    print(f"Last Chapter: {chapter}")
    print(f"Last Boss: {boss}")
    print("-1. Exit")
    print("0. Greeting")
    print("1. Chapter 1: The White Rabbit.")
    if chapter > 1:
        print("2. Chapter 2: Down the Rabbit Hole.")
    if chapter > 2:
        print("3. Chapter 3: Welcome to Wonderland.")
    if chapter > 3:
        print("4. Chapter 4: The Duchess' House.")
    if chapter > 4:
        print("5. Chapter 5")
    menu_choice = int(input("Where would you like to go? "))
    chapter = menu_choice
    return chapter
    

def goodbye() -> None:
    """Prints goobye message for the player."""
    global chapter
    global player
    global points
    global attack
    global inventory
    global hp
    global max_hp
    global main_weapon
    global main_armor
    global boss
    print(f"Inventory: {inventory}")
    print(f"Points: {points}")
    print(f"Health: {hp}/{max_hp}")
    print(f"Attack power: {attack}")
    print(f"Last Chapter: {chapter}")
    print(f"Last Boss: {boss}")
    print(f"The End? 'Thank you {player}, for playing my game based on Alice in Wonderland by Lewis Carroll. Unfortunately, I ran out of time and couldn't code the final battle against the Queen of Hearts and her Infernal Jabberwock. I hope you still enjoyed' - Mateo Alvarez.")


def died() -> None:
    """Restarts the chapter if the player dies."""
    global chapter
    global player
    global points
    global attack
    global inventory
    global hp
    global max_hp
    global main_weapon
    global main_armor
    global boss
    global boss_weapon
    print(f"The lass thing you see is {boss} using their {boss_weapon} on you. Then, complete darkness. You wake up at the beginning of chapter {chapter}. 'Weird...Maybe it was just an odd dream', you think to yourself.")
    hp = max_hp
    return chapter


def greet() -> None:
    """Welcomes player to the game."""
    global player
    global chapter
    player = str(input("What is your name? "))
    print(f"Hello, {player}! Welcome to Adventures in Wonderland...{bunny}")
    print("Wonderland is a dangerous realm, home of the uncanny, and definitely not for the faint of heart. As you venture into this odd world you will find many wonders and friendly creatures. But be wise, for evil hides at every corner awaiting to slay, eat and behead whomever is foolish enough to cross their way.")
    input(f"Are you curious yet, {player}? ")
    print(f"Curiouser and curiouser! Let the story begin...{bunny}")
    chapter = 1
    continue_0 = str(input("Do you wish to continue to Chapter 1? (Yes or No) "))
    if continue_0 == "No":
        menu()


def white_rabbit() -> None:
    """Runs Chapter 1 of the game."""
    global chapter
    print("Chapter 1: The White Rabbit.")
    print("The Rip Van Winkle State. May 4th, 1875. You wake up from the sound of your stomach rumbling. 'What a strange dream' you say to yourself. You had dreamt of the most wonderful place, full of the oddest creatures. But your were brought back to reality by your hunger. The last time you had eaten was the morning from the day before, when the town baker had mistakenly left a freshly cooked loaf of bread alone during the matinee market. And of course, you didn't think twice before taking it for yourself. You think he is prone to make the same mistake again, so you stand up and walk off the alleyway. You hear the belltower ringing, which means the market will close soon. So you decide to take an unusual path that will take you faster, through the forest. After a few minutes, you hear the mumblings and laughter of the matinee on the distance. You are getting close! When suddenly, a strange sight catches the corner of your eye. 'A white rabbit?', you ask yourself. It can't be, there are no rabbits in the Rip Van Winkle State. They are sold in the market as a rarity...'That's it!', an idea sparkled. You decide to search for the white rabbit, so you can sell it and maybe actually buy a loaf of bread!")
    print("Follow the white rabbit?")
    print ("A. Yes.")
    input("(Write 'A') ")
    print("You start searching for the rabbit...10 min go by...then 20...the matinee market is not going to continue for much longer. 'Maybe I should go back and try to get some food before it closes.', you think to yourself. When suddenly, from the corner of you eye, you catch a glimpse of the...'Is the rabbit wearing a waistcoat?'. You are very confused. In awe really. The white rabbit starts talking to itself 'Oh dear! Oh dear! I shall be too late!', he seems to be rushing somewhere...You cannot believe your eyes. He goes through the garden gate of an enormous house. Your stomach rumbles again. You are starving. You look back to where the market sounds are coming from, and pause for a second. You decide to follow the white rabbit through the garden gate.")
    print("'This garden is huge', you say while your walking ahead. You entered what seems to be a labyrinth made out of tall and large bushes that appear to go on forever. 'Wealthy people have very odd likings', you think. But wealth is all you have every dreamed of. You find yourself at a crossing. Theres only two ways to go: Left or Right.")
    print("A. Left.")
    print("B. Right.")
    garden_choice = str(input(""))
    if garden_choice == "B":
        print("Dead end. You complain about your decision making. Then you turn back and follow the left trail.")
    print("You see the white rabbit. He is running faster now. You hear it mumbling 'too late, too late'. You run behind it. 'You are not getting away this time'. You follow the white rabbit through a conglomerate of fancy flowers and bushes, and out of the garden. The white rabbit continues to run until he reaches a hill with a singular dead tree in the middle of it and a big hole in the ground next to it. It stops in front of the dead tree, and pulls out a pocket watch. The white rabbit looks at his watch for a second, then jumps down the hole.")
    print("'No!' you scream. Your one chance to become wealthy has just gone down a hole. Literally. 'Maybe it's the rabbit's home', you think to yourself. You look back, 'I am quite far from that fancy house...and town'.You stand in front of the hole.")
    print("Do you want to revise the hole?")
    print("A. Yes.")
    print("B. No.")
    hole_choice = str(input(""))
    if hole_choice == "A":
        print("You kneel and lean to the center of the hole, placing your hands on the edges. The hole is strange...it looks almost bottomless. But a light appears to be coming from very deep within.'If I could only get a closer look'. You lean in closer and...you fall down the hole.")
    else:
        print("You notice the hole is strange...it looks almost bottomless. But a light appears to be coming from very deep within. You get startled and quickly try to move away. But you slip on one of the tree roots and...you fall down the hole.")
    chapter = 2
    continue_1 = str(input("Do you wish to continue to Chapter 2? (Yes or No): "))
    if continue_1 == "No":
        menu()


def rabbit_hole() -> None:
    """Runs Chapter 2 of the game."""
    global chapter
    global inventory
    print("Chapter 2: Down the rabbit hole.")
    print("You find yourself falling down the rabbit hole. All that sorrounds is darkness, which robs you of your vision.Then suddenly, a warm light appears from down under... 'a lamp?'. And that is not the only object that appear to be floatig in the down the hole, a piano, books, chairs, a mirror, a painting of a little blonde girl in a blue dress. You can not begin to comprehend what is happening. You seem to be going faster than the other things, which don't seem to be falling at all.")
    print("The hole sorrounding you suddenly changes from dirt and tree roots to a bright white marble. And then...you hit the ground. 'ouch'. You stand up and notice you are somewhere entirely new. A circular room with several doors of all shapes and sizes, and a singular table in the middle of the room. For some odd reason there are also puddles of water all around the room. You go towards the table in the middle of the room. There is a half-drank bottle with a label on it that says 'drink me'. You turn your head to the floor, under the table lies a small glass box with a half-eaten pastry which reads 'eat m' marked by berries. Someone must have eaten the 'e' . You stomach growls. You are starving.")
    print("A. Eat the pastry.")
    print("B. Drink from the bottle.")
    table_choice = str(input(""))
    if table_choice == "A":
        print("You don't even think before shoving the pastry into your mouth. It is delicious. You feel strange. The room is changing...'it's getting smaller?'...No...you are growing bigger. You have become the size of a giant!...a small giant. 'How am i going to fit through a door now?', you ask yourself. You turn your attention to the table once again.")
        print("A. Drink from the bottle.")
        input("")
    else:
        print("You can't think about eating right now. You still need to find the white rabbit. 'When I'm wealthy, I can focus on eating pastries all day' you think to yourself. You grab the pastry and shove it in your pocket. 'I will eat it once I find the rabbit'. You grab the bottle and drink it's content. It tastes like cherry-medicine.")
        inventory["magic pastry"] = "Turns you into a small giant. Double attack and health while in this state."
    print("You feel strange. The room seems to get a lot bigger, and you notice you've become the size of a small cat! You are ver confused by how you've changed your size. But a bright golden reflection catches the corner of your eye. You see a small golden key on the floor. Too small too open any of the doors. You approach the key, and notice a closed curtain on the wall next to it.")
    print("A. Grab the key.")
    print("B. Open the curtain.")
    key_choice = str(input(""))
    if key_choice == "B":
        print("You open it and a small white door appears from behind the curtain. Small enough for...'the key!'.")
        print("A. Grab the key.")
        input("")
    else:
        print("You grab the small key and you turn your attention to the closed curtain.'Maybe..'") 
        print("A. Open the curtain.")
        input("")
        print("A small white door appears behind the curtain. ")
    print("A. Open the door.")
    input("")
    print("You use the golden key and open the white door. A bright light blinds you for a moment. You slowly open your eyes, and gasp at the sights. You cannot believe your eyes. You are certainly not in The Rip Van Winkle State anymore.")
    chapter = 3
    continue_2 = str(input("Do you wish to continue to Chapter 3? (Yes or No): "))
    if continue_2 == "No":
        menu()


def welcome_to_wonderland() -> None:
    """Runs Chapter 3 of the game."""
    global chapter
    global player
    global points
    global attack
    global inventory
    global hp
    global max_hp
    global main_weapon
    global main_armor
    print("Chapter 3: Welcome to Wonderland.")
    print("The oddest of forests stands before you. A variety of trees in all shapes spread all throughout. They seem to grow upside down, with the roots on the top, and twist and tangle in on themselves. The grass and flowers seem to be moving in unison, almost like dancing to a symphony. But their is no breeze that moves them. A big and old gate reads 'Welcome to Wonderland'. You notice an odd stream colored smoke coming on the distance, not far from where you are.'Maybe there is someone out there that can help me find that rabbit'. As you walk past the gate, you notice there are some strange creatures flying around, but they are not mere insects. Butterflies whose wings seem to be made of bread-and-butter and rocking-horses with insect wings are flying around a large bed of flowers. As you get a closer look at the flowers, you see that they have...'faces?'. They appear to be humming and dancing with each other. They also seem quite fancy.")
    print("A. Approach the flowers")
    print("B. Head towards the stream of colored smoke.")
    forest_choice = str(input(""))
    if forest_choice == "A":
        print("You approach the flowers and hear a conversation between a tiger-lily and a rose. 'No one worth talking to has come in ages!, said the tiger-lily. 'And no one to hear our beautiful singing', cried the rose. They notice you in front of them and turn their attention to you. 'And who do we have here?', they ask." )
        print("Respond:")
        print(f"A. My name is {player}. ")
        print("B. You can talk?")
        print("C. You are beautiful.")
        flower_choice = str(input(""))
        if flower_choice == "A":
            print(f"{player}? What a weird name for a flower, says the rose.")
        elif flower_choice == "B":
                print("'Of course we can. Can YOU talk?', says the rose.")
        elif flower_choice == "C":
                print("'Belive me blossom, I know.', says the rose")
        print("Ask:")
        print("A. Do you know where to find the white rabbit?. ")
        print("B. Can I hear you singing?.")
        idx_flowers: int = 0
        while idx_flowers == 0:
            flower_choice1 = str(input(""))
            if flower_choice1 == "A":
                print("'Oh that rabbit, always running late! We don't know where he is, but there is a caterpillar who is said to know everything that can propably help you. Just follow that colored smoke. Now run along, you are blocking our sunlight.'")
            if flower_choice1 == "B":
                print("'Of course you do. Violets! Daises! it's blooming time.'")
                print("Every other flower around you open their petals to reveal that they have faces as well. Then the tiger-lily turns to you and says, 'This is 'All in the Golden Afternoon''")
                print(f"{music} 'Little bread-and-butterflies kiss the tulips / And the sun is like a toy balloon / There are get-up-in-the-morning glories / In the golden afternoon / There are dizzy daffodils on the hillside / Strings of violets are all in tune / Tiger lilies love the dandelions / In the golden afternoon / You can learn a lot of things from the flowers / For especially in the month of June / There's a wealth of happiness and romance / All in the golden afternoon / All in the golden afternoon, the golden afternoon ' {music}")
                print("You cheer,'that was incredibly beautiful', but they seem unimpressed by your praise, and they continue talking amongst them. They appear to be ignoring you You decide to head towards the stream of colorred smoke.")
                idx_flowers += 1
    print(f"As you approach the stream of smoke, you notice the forest goes from an abundace of trees and flowers, to mushrooms. Which surpisingly enough, don't seem to be able to speak. 'I guess mushrooms are odd enough as they are', you think. You finally get to the source of the smoke. A single bright blue caterpillar is sitting on a mushroom smoking a long hookah. 'Welcome human', exhales the caterpillar, accompanied with a great deal of smoke. '{player} is it?'. You are thrown off by this creature knowing your name.")
    print("Respond:")
    print("A. Yes.")
    print("B. No.")
    input("")
    print("'You must certainly are, you could not not be. Welcome to Wonderland. Full of wonders it is, not all of them necessarily good. Are you trying to find the rabbit?'")
    print("Respond:")
    print("A. Yes.")
    print("B. No.")
    input("")
    print("'Of course you are. You are trying to get something you long for, but not necessarily need. In Wonderland things work a little differently, you might get what you need, which could not necessarily be what you long for.'")
    print("Respond:")
    print("A. What?")
    print("B. Ok...")
    print("C. Please stop smoking directly to my face.")
    input("")
    print("'However if you so desesperately think finding the rabbit is what you need, just go to the Duchess' house, right outside of the forest. She can guide you to the Castle of Hearts, where the rabbit works as staff for the Queen of Hearts.'")
    print("Respond:")
    print("A. Thanks.")
    print("B. Duchess?")
    print("C. Queen?")
    idx_caterpillar: int = 0
    while idx_caterpillar == 0:
        caterpillar_choice = str(input(""))
        if caterpillar_choice == "B":
            print("'The Duchess. Big headed crone, in a much literal way. She resides on her small house with her footman, cook, baby and cat. She seems to be in an awful mood lately.'")
            idx_caterpillar += 1
        if caterpillar_choice == "C":
            print("'The Queen of a Hearts. A Queen she must certainly is, for she wears a crown on her head. However, some of her subjects might find her very unpleaseant. Maybe it has something to do with her high-pitched voice...or her ego...or her fixation on beheading whichever creature causes her displeasure.'")
            idx_caterpillar += 1
        if caterpillar_choice == "A":
            idx_caterpillar += 1
    print(f"'{player}, before you leave, there is a couple of things you need to know about Wonderland. You are most certainly going to find some evil creatures that will be looking towards battling with you.However, you have certain attributes that will help you survive. Yourself, as every creature in Wonderland has a certain amount of health and attack power. You can lower the health of a creature by attacking, and the other way around as well. Let's take a look at your attributes.'")
    print(f"Health: {hp}/{max_hp}")
    print(f"Attack power: {attack}")
    input("Press any key to continue: ")
    print("'You seem to be a little low on health, have a piece of my mushroom. It will heal you right up. As move forward the creatures you encounter will be more evil and stronger than before. There are items in Wonderland that you can use to better yourself. You attributes will always update to the best item in your posession. Here, have this mushroom bag. With this bag you will be able to keep any item on your posession. Have this mushroom knife too, it is great for cutting mushrooms.")
    inventory["mushroom knife"] = "Attack +2. Great for cutting mushrooms."
    hp = max_hp
    main_weapon = "mushroom knife"
    attack = 4
    print(f"'{main_weapon}' added to your inventory. It increases your regular attack power by 2.")
    print(f"Inventory: {inventory}")
    print(f"Health: {hp}/{max_hp}")
    print(f"Attack power: {attack}")
    input("Press any key to continue: ")
    print(f"'Another important aspect of life, {player}. Not all wonderland creatures are as generous as myself. Most items cost points. You can earn points by killing creatures, or just from mere curiosity. Here, let me provide you some of my own, I have everything an old caterpillar like me could ever long to need. Spend Wisely")
    points += 15
    print(f"Inventory: {inventory}")
    print(f"Points: {points}")
    print(f"Health: {hp}/{max_hp}")
    print(f"Attack power: {attack}")
    input("Press any key to continue: ")
    print(f"'The best of luck in your adventure, {player}!'...' and one final request. When you see everyone...please tell them the Queen has taken Alice.'" )
    print("You thank the caterpillar for his generosity and wisdom, and make way to the Duchess' house. You think of everything you've witnessed so far, and how quickly everything changed. The White Rabbit with his pocketwatch. A drink that makes you the size of a small cat. A forest that looks alive. The talking caterpillar. A Duchess and a Queen. Everythink seem so odd, but yet strangely familiar. 'Who knows what I will find next?...'")
    chapter = 4
    continue_4 = str(input("Do you wish to continue to Chapter 4? (Yes or No): "))
    if continue_4 == "No":
        menu()


def the_duchess_house()-> None:
    """Runs Chapter 4 of the game."""
    global chapter
    global player
    global points
    global attack
    global inventory
    global hp
    global max_hp
    global main_weapon
    global main_armor
    global boss
    global boss_weapon
    print("Chapter 4: The Duchess' House.")
    print(f"As your leaving the caterpillar's forest, you notice a small house on the distance. 'The Duchess' House', you proclaim. You start making your way towards it, when suddenly you hear some screaming closing in towards you. You pull out your {main_weapon}. Two figures appear from behind the trees. 'Twins?'. Two identical little fat men come screaming and running towards you. You get startled and loose your composture, but when they reach you, they hide behind your back as one of them says 'Please', and the other completes 'Help us'. Suddenly, another figure emerges from the trees, a big walrus wearing a fancy suit and standing on its tail screams, 'I will have both of you for dinner'.")
    print("A. Who are you?")
    print("B. Is that a Walrus?")
    twee_choice = input("")
    if twee_choice == "A":
        print("'I am Tweedledee', says one of the men. 'And I am Tweedlum', proclaims the other one. 'He is my brother', says Tweedlee. 'And he is mine., says Tweedlum.")
    if twee_choice == "B":
        print("'Yes and he is very angry', says one of the men. 'At us and very hungry' says the other one.")
    print("'You little boys ruined me. I will never be able to eat oysters again. You two will have to do instead.', screams the walrus. His gigantic tusks pointed at you,, and the two little men behind you.")
    boss = "The Walrus"
    boss_weapon = "Tusks"
    walrus_attack: int = 5
    walrus_hp: int = 15
    walrus_max_hp: int = 15
    while walrus_hp > 0:
        if hp < 1:
            died()
            return chapter
        print(f"{boss}")
        print(f"Health: {walrus_hp}/{walrus_max_hp}")
        print(f"Attack power: {walrus_attack}")
        print("vs")
        print(f"{player}")
        print(f"Health: {hp}/{max_hp}")
        print(f"Attack power: {attack}")
        print("A. Attack")
        print("B. Talk")
        print("C. Use Item")
        walrus_choice = input("")
        if walrus_choice == "A":
            from random import randint
            attack_accuracy = randint(1, 4)
            if attack_accuracy <= 2:
                print(f"You attack {boss} with your {main_weapon}. You cut him and he roars.")
                walrus_hp -= attack
            elif attack_accuracy == 3:
                print(f"You attack {boss} with your {main_weapon}. You stab him on his belly.")
                walrus_hp -= attack
            else: 
                 print(f"You attack {boss} with your {main_weapon}. You miss. He angrily roars at you.")
        if walrus_choice == "B":
            print(f"'Once I kill you, I will put you on a slice of bread with butter and pepper.', says {boss}'")
        if walrus_choice == "C":
            print(inventory)
            use_item = input("")
            if use_item == "magic pastry":
                attack = attack*2
                hp = hp*2
                inventory.pop("magic pastry")
            else:
                if use_item == "mushroom knife":
                    print("You are already using your best weapon.")
                else:
                    print("You can't use this item in a fight.")
        from random import randint
        walrus_accuracy = randint(1,5)
        if walrus_accuracy == 1:
            print(f"{boss} uses his tail to jump to the sky. He descends spinning towards you and smacks you with his tail")
            hp -= walrus_attack
        if walrus_accuracy == 2:
            print(f"{boss} sprints towards you, and hits you with his tusks")
            hp -= walrus_attack
        else:
            print(f"{boss} tries to head-smack you, but you dodge his attack.")
    print(f"You slice one of the {boss}'s {boss_weapon} and it falls dead on the ground. You grab the tusk, 'I could use this as a weapon'. You pick-pocket the walrus' suit and find a bag of 30 points.")
    inventory["tusk"] = "Attack +4. Belonged to a very hungry walrus."
    main_weapon = "tusk"
    attack = 6
    points += 30
    print(f"'{main_weapon}' added to your inventory. It increases your regular attack power by 5.")
    print("The little men come out of their hiding to celebrate your win. 'Hurray! Hurray! The Walrus is dead! Thank you, our heroe, who saved the day.'")
    print("Respond:")
    print("A. Why did the Walrus want to eat you?")
    print("B. Who are you?")
    twee_choice1 = str(input(""))
    idx_twee: int = 0
    while idx_twee == 0:
        if twee_choice1 == "B":
            print("'I am Tweedledee', says one of the men. 'And I am Tweedlum', proclaims the other one. 'He is my brother', says Tweedlee. 'And he is mine.', says Tweedlum.")
            idx_twee +=1
        if twee_choice1 =="A":
            print("That Walrus was always hungry', says Tweedlee. 'And he would cheat to eat.', says Tweedlum. 'He would deceive little oysters'...'Inviting them for a treat. 'But at as soon as he got hungry'...'He would devour them in a beat. 'We spread the word around'...'Beware of the walrus who cheats'. 'This he didn't like'...'for anymore he couln't cheat to eat.'")
            idx_twee +=1
    print("'He is not going to eat anyone anymore.', you say. 'Hurray! Hurray!', they say. 'Let us give you'...'A token of our gratitude.' The twins go towards the walrus, and take his skin off. They then take a pair of scissors and thread and confect a waistcoast from the walrus skin. They also grab a piece a mushroom from the ground and and it to you.'Have here'...'Heroe'.") 
    max_hp += 12
    print("You put on the walrus waistcoast. It makes you feel stronger, but you also smell like fish.")
    print("You eat the mushroom. It restores you health to the maximum.")
    inventory["walrus waistcoast"] = "Max. Health +12. Smells like fish."
    hp = max_hp
    print(f"Inventory: {inventory}")
    print(f"Points: {points}")
    print(f"Health: {hp}/{max_hp}")
    print(f"Attack power: {attack}")
    input("Press any key to continue: ")
    print("'Thank you for this amazing coat Twees'. They look a little confused. Maybe Wonderlanders are not used to nicknames. 'You are'...'Welcome'. 'Where is our'...'Brave heroe going?'")
    print("Respond:")
    print("A. I am going to see the Duchess.")
    print("B. I am looking for the white rabbit.")
    print("C. I am heading to the Queen's Castle.")
    twee_choice2 = str(input(""))
    if twee_choice2 == "A":
        print("'The Duchess?!', they both claim. 'You better be careful Heroe...'She has been very blue, for her baby turned into a pig'...'And then away he flew.', 'Best of luck'...'Beloved Heroe.' The twins proceed to hug you and send you away to The Duchess' House.")
    if twee_choice2 == "B":
        print("'The rabbit...'Works for the Queen. 'In her castle'...'Most of his time he's been.' 'However without without invitation'...'Even a heroe can't show. The Duchess could'...'Advice you how to go.' 'Best of luck'...'Beloved Heroe.' The twins proceed to hug you and send you away to The Duchess' House.")
    if twee_choice2 == "C":
        print("'The Queen of Hearts?!', they both claim. 'Without invitation'...'Even a heroe can't show. For if you do'...'your head she will have off. The Duchess could'...'Advice you how to go.' 'Best of luck'...'Beloved Heroe.' The twins proceed to hug you and send you away to The Duchess' House.")
    print(f"You finally get to the house. Outside there is a sign that reads 'MISSING: BABY', with a picture of a pig. You walk to the front door, when you notice an odd creature. What seems to be a frog-footman, with a hair powdered wig that curls over his head, stands in the front door. He appears to be staring up into the sky. There is also an extraordinary noise coming from inside the house. You approach the footman and say 'Hello?'. Without taking his eyes from the sky, he replies, 'State your name, status and purpose with the Duchess.', says the frog. 'My name is {player}, I am a Heroe, and I am here to help find the baby pig.', you respond. 'Follow me, Heroe.' says the frog. You follow him inside the house. An older woman with a extremely large head and a just as large headdress sits on a chair. Next to her, a man is utterly focused on his cooking. He is unadvertly throwing utensils over his shoulder, as he is oblivious to any other presence in the house. The house reeks of pepper and the air makes you want to sneeze. 'Duchess', begins the frog, 'I present to you, the Heroe {player}, who claims to come here to help find your Baby.' She looks at you. 'A Heroe?', she appears to be unimpressed and her face appears to be stuck in an angry expresion. 'We do not get a lot of 'Heroes' in Wonderland.'")
    print("Respond:")
    print("A. I am not from Wonderland.")
    print("B. I promise to get you your pig back.")
    print("C. Could show me the way towards the Queen's Castle?")
    duchess_choice = str(input(""))
    if duchess_choice == "A":
        print("'I don't like the idea of a foreigner touching my Baby.', she menancingly claims. 'But I am so very worried. My Baby is out there by himself.")
    if duchess_choice == "B":
        print("'And what is your word worth to me Heroe?, she menancigly claims. ")
    if duchess_choice == "C":
        print("'How dare you demand something from me?!, she angrily claims.")
    print("The Duchess stands up, 'She is quite short' you think to yourself, and yells 'Footman, get this jester out my house this instant!' The frog-footman accompanies you out. When you are both outside, he says 'Heroe, the only way she is ever going to consider helping you is if you get her Baby back. He ran off the woods years ago, and hasn't been back since. The Duchess' cat is out there looking for it as we speak. Find the cat, he might be of aid for you. Good luck.' then he closes the door. You are determined to get to the white rabbit, so you decide to find The Duchess' Baby.")
    print("You start looking in the forest. 'Come piggy, piggy!', you call out.")
    def baby_pig() -> bool:
            print("You find yourself at the beginning of of the forest where there is a left trail and a right trail. The left trail has a sign that reads 'Orange', while the sign in the right trail sign reads 'White'.")
            print("Which way would you like to go?")
            print("A. Right.")
            print("B. Left.")
            pig_choice0 = str(input(""))
            if pig_choice0 == "A":
                print("You continue right, the trees seem to have turned white. The temperature suddenly dropped, and everything in sight appears to be coverd in snow.You keep forwards, observing the odd changes that happened to the forest. You come upon another division in the forest. The left sign reads 'In', while the right sign reads 'Out'.")
            if pig_choice0 == "B":
                print("You continue left, the trees seem to have turned to warm colors. Everthing in sight appears to be covered on orange, yellow and red leaves. You keep forwards, observing the odd changes that happened to the forest. You come upon another division in the forest. The left sign reads 'Out', while the right sign reads 'In'.")
            print("Which way would you like to go?")
            print("A. Right.")
            print("B. Left.")
            pig_choice1 = str(input(""))
            if (pig_choice0 == "A" and pig_choice1 == "B") or (pig_choice0 == "B" and pig_choice1 =="A"):
                print("You reach the middle of the forest. The light here is very dim, and the sorroundings are very quiet. A figure suddenly appears on a branch of a tree. A cat with disturbing grin that goes from ear to ear stares at you with its bright green eyes.")
            else:
                print("The path you choose took you back to the begining of the forest.")
                return False
            idx_baby: int = 0
            while idx_baby == 0:
                print("Ask:")
                print("A. Who are you?")
                print("B. Are you the Duchess' Cat?")
                cheshire_cat = str(input(""))
                if cheshire_cat == "A":
                    print("'I am none more than you are. I am air. I am nothing and I am everything. But some might call me The Cheshire Cat.")
                if cheshire_cat == "B":
                    print("'Some people might say so, other might say that she is the Cat's Duchess.', it answers, with his grin growing wider.")
                    idx_baby += 1
            idx_baby = 0
            while idx_baby == 0:
                print("Say:")
                print("A. Could you tell me where to go?")
                print("B. I am looking for the Duchess' pig.")
                cheshire_cat1 = str(input(""))
                if cheshire_cat1 == "A":
                    print("'That depends a good deal on where you want to get to.', it says.")
                if cheshire_cat1 == "B":
                    print("'Ah yes, the Duchess' baby is always running around. The Duchess would not like his incessant crying, so she would spank him when he cried. But then from a human girl's touch he became a pig. Now he roams around freely.', he tells.")
                    idx_baby += 1
            idx_baby = 0
            while idx_baby == 0:
                    print("Say:")
                    print("A. Do you know where I can find the pig ?")
                    print("B. A Human Girl? Would that girl's name happen to be Alice?")
                    cheshire_cat2 = str(input(""))
                    if cheshire_cat2 == "A":
                        print("'Well, the baby was always quite hungry. So the 'pig', probably went straight ahead where food is can be found'.")
                        idx_baby += 1
                    if cheshire_cat2 == "B":
                        print("'The cat disappears into thin air, leaving only a cloud of dust behind. He then reappears floating over your head upside down, with his eyes staring straight into yours, and his smile wider than ever. 'Alice?!', he exclaims 'Are you familiar Alice?!'. 'Not personally.', you respond, 'But we have common acquantainces.' He vanishes again, and reappears on the tree branch again. 'That's too bad', he says, 'That girl is the maddest of us all.' 'I have a message about Alice', you continue, 'apparently the Queen has taken her...?. The cat's grin drops. 'My poor Alice...', he says, 'No one can save her now.'")
            print("'Thank you cat.', you say. The cat grinned at you and vanished into thin air. His grin being the last part of him to disappear. You keep straigth towards where the grinning cat had said. You find another two paths. The left one reads 'sweets', while the right one reads 'greens'. 'What would a pig fancy eating?', you think to yourself.")
            print("Which Would you like to go?")    
            print("A. Right.")
            print("B. Left.")
            pig_choice2 = str(input(""))
            if pig_choice2 == "A":
                print("The path you choose took you back to the begining of the forest.")
                return False
            if pig_choice2 == "B": 
                print("You continue left, the grim and drank forest becomes into a candy wonderland. Trees of cotton candy. Bushes of cake. A lake of chocolate. You see the little pig drinking from the chocolate lake. You grab a little cotton candy from a tree and call for it. 'Come piggy, piggy. Who is a good little piggy'. The piggy looks at you, then starts sprinting towards you. It jumps into your arms and starts eating the candy.")
                return True
    if baby_pig() != True:
        baby_pig()
    print(f"You take the pig back to the duchess house. 'I bring the pig', you exclaim. The frog-footman opens the door and announces, 'Duchess, the heroe has brought upon your baby.' The Duchess comes printing out the door and you deliver the pig to her. As soon as you let go of the pig, he trasnforms into a human baby, and starts wailing. 'My poor baby!' she wails, 'who knows what horrors you experienced oustside by yourself.' She turns at you, 'Thank you, heroe'. From behind a new creature appears, another footman, which appears to be a fish. The fish-footman announces 'For the Duchess. An invitation from the Queen to play croquet.', and then hands an envelope, almost his size, to the frog-footman. The frog-footman repeats 'From the Queen. An invitation for the Duchess to play croquet.' The fish-footman leaves the way he came. The Duchess says, 'Footman, give this invitation to our Heroe, so that they can attend this game of croquet with the Queen. Also make sure provide them with the reward.' The Duchess, with her baby, go back inside the house. The frog-footman provides you with the invitation and a bag of 55 points, 'Make way towards the Mad Hatters tea party, just follow the loud cackling, after that you will see the castle on the distance. Thank you, {player}.'")
    inventory["invitation"] = "'You have been invited to play croquet at the Queen's castle.'"
    print("'invitation' added to your inventory. It reads 'You have been invited to play croquet at the Queen's castle.")
    points += 55
    print("You say goodbye to the kind footman, and leave the Duchess' House. As you are walking away, you hear cackling and things breaking. 'To the mad tea party I go', you say.")
    chapter = 5
    continue_5 = str(input("Do you wish to continue to Chapter 4? (Yes or No): "))
    if continue_5 == "No":
        menu()


def mad_tea_party() -> None:
    """Runs Chapter 5 of the game."""
    global chapter
    global player
    global points
    global attack
    global inventory
    global hp
    global max_hp
    global main_weapon
    global main_armor
    global boss
    global boss_weapon
    print("Chapter 5: A Mad Tea Party.")
    print(f"As you arrive to the source of the cackling, you see a big dinner table with everything required for a tea party. There are plates, pastries, tea cups and tea pots. Sitting in the table is a March Hare, a Dormouse and a man wearing a very odd hat. They seem to be uncontrollaby laughing, and throwing all kinds of silverware at each other. 'This really is a mad tea party.', you say to yourself. As you approach, the hare throws a plate at you, 'You are late to the party!', he exclaims. You use your {main_weapon} and shatter it before it reaches you. 'Good reflexes', says the dormouse. 'And who would you be?' asks the man, with a smile and a crazy look on his face. 'My name is {player}, and Im a Heroe.', 'A Heroe?!' they exclaimed. 'My oh my'...'Well {player} the Heroe, would you be interested in sitting down for tea?. 'I would love to, but I'm on my way to the Queen Castle.' you respond. 'Interesting...and what business have you with that ratched woman? the man says. The March Hare and the Dormouse giggle. 'I am looking for the white rabbit.', you respond. 'That little troublemaker', the man says. 'You are so stubborn...reminds me of a little girl I once knew.'")
    idx_tea: int = 0
    while idx_tea == 0:
        print("Say:")
        print("A. Who?")
        print("B. Would that person's name happen to be Alice?")
        hatter_choice0 = str(input(""))
        if hatter_choice0 == "A":
            print("'Just a little girl, who once so innocently came. She had tea with us, she acted like such a damme. But so mad she was, that she would put us all to shame. she left looking for the white rabbit, it was such a shame.'")
        if hatter_choice0 == "B":
            print("The man stands up his seat, then gets on the table and walks to the other side where you were standing. He kneeled down, placing his face just in front of yours. He had one eye green an one blue. His hair was orange with a couple of pink specks. 'You know our Alice?', he asked with a wide smile. 'I've heard a great deal about her.', you respond. 'All odd things I presume', he laughs.")
            idx_tea += 1
    print("Say:")
    print("A. The Queen of Hearts has her.")
    print("Everything went silent. The March Hare and the dormouse stopped throwing dinnerware at each other, and stared at you. 'Hatter...' they said towards the man. The Hatter's expression went dark and his eyes truned grey. '...What did you say? he asks you. 'The caterpillar said to tell everyone.', you respond. 'The caterpillar...', exclaims the hatter with a furious tone, 'all this time...we thought she had just gone back home. But SHE had her. She's been trapped in her castle suffering. And the caterpillar KNEW! I'll go to her castle...I'll rescue Alice...I'll kill the queen...'")
    print("'You will do what to My Queen?' A figure threatening figure comes out of the shadows behind you. 'The Knave of hearts', whispers the dormouse before going into hiding in a teapot. The Knave of Hearts is a tall and robust man, he carries a sword and wears a vandyke on his face. He rides a black horse and keeps a bright white sword close to his waist. Both the Knave and his horse seem to be wearing heart-shaped armors around their bodies. 'YOU!, says the Hatter. 'You knew she had Alice!'. 'Of course I did. Why do you think I come check up on you mad people every now and then. I had to make sure you were behaving well and throwing your stupid little tea parties. I'll admit I enjoyed seeing you keep a seat for Alice next to you.' The Hatter really turned Mad. He charged against the Knave, but it was useless. The Hatter is a very small man compared to the Knave. The Knave punched the Hatter mid-air and sent him flying across the table. 'I guess I will have to kill you all now.', he says with big smile on on his face. 'Stop!', you claim. Putting yourself between the Knave and the Hatter. 'Who do we have here?, he asks, 'Doesn't matter I'll kill you too'.")
    boss = "The Knave of Hearts"
    boss_weapon = "Vorpal Sword"
    knave_attack: int = 7
    knave_hp: int = 30
    knave_max_hp: int = 30
    while knave_hp > 0:
        if hp < 1:
            died()
            return chapter
        print(f"{boss}")
        print(f"Health: {knave_hp}/{knave_max_hp}")
        print(f"Attack power: {knave_attack}")
        print("vs")
        print(f"{player}")
        print(f"Health: {hp}/{max_hp}")
        print(f"Attack power: {attack}")
        print("A. Attack")
        print("B. Talk")
        print("C. Use Item")
        knave_choice = input("")
        if knave_choice == "A":
            from random import randint
            attack_accuracy = randint(1, 4)
            if attack_accuracy <= 2:
                print(f"You attack {boss} with your {main_weapon}. You cut him on the face, he yells 'I will kill you for that.'.")
                knave_hp -= attack
            if attack_accuracy == 3:
                print(f"You attack {boss} with your {main_weapon}. You stab on the back. He falls off his horse, then gets up on it again.")
                knave_hp -= attack
            else: 
                 print(f"You attack {boss} with your {main_weapon}. You miss. He horse kick you.")
                 hp -= 1
        if knave_choice == "B":
            print(f"'This is not your fight, why are you defending them?', {boss} ask you'")
            print("You respond, 'It just seems like the right thing to do.'")
        if knave_choice == "C":
            print(inventory)
            use_item = input("")
            if use_item == "magic pastry":
                attack = attack*2
                hp = hp*2
                inventory.pop("magic pastry")
            else:
                if use_item == "mushroom knife":
                    print("You are already using your best weapon.")
                if use_item == "tusk":
                   print("You are already using your best weapon.") 
                else:
                    print("You can't use this item in a fight.")
        from random import randint
        knave_accuracy = randint(1,4)
        if knave_accuracy == 1:
            print(f"{boss} sprints towards you with his horse. He swings his {boss_weapon} and cuts you right on the leg.")
            hp -= knave_attack
        if knave_accuracy == 2:
            print(f"{boss} stabs you with his {boss_weapon}.")
            hp -= knave_attack
        else:
            print(f"{boss} tries to swing his {boss_weapon} at you, but you throw a tea cup at him and he misses.")
    print(f"You stab {boss} in the heart with your {main_weapon} and he falls dead of his horse. You grab his sword. 'This sword feels powerful'. You snatch a bag of 80 points off his armor.")
    inventory["Vorpal Sword"] = "Attack +14. Destined to kill the Jabberwock."
    main_weapon = "Vorpal Sword"
    attack = 20
    points += 80
    print(f"'{main_weapon}' added to your inventory. It increases your regular attack power by 14.")
    print("The March Hare and the Dormouse help the Hatter up. He comes to you and says, 'Heroe, I am too weak to help Alice. Please I beg of you, saver her.' You respond, 'I will.' He smiles weakly, 'However, let me warn you, the Queen probably has her infernal beast, the Jabberwock guarding her castle. If you want to get to Alice, you will have to get through the Jabberwock. That sword the Knave was carrying is called the Vorpal Sword. It is said to be destined to kill the Jabberwock.' 'I can handle whatever madness this place throws at me.', you respond. You both smile at each other. 'The March Hare can help you get better equiped. As for me, I am far too weak to help. But I wish you all the luck Wonderland has to offer.' 'Thank you Hatter. ', you say. Then the he sits down and pours himself a cup of tea. The March Hatter grabs your hand and excitedly says 'Come, Come.'. He lead you to a little cabin, (Big enough to fit a Hare), with a sign that read 'The March Hare Pawn Shop.' 'Welcome to my shop! I'm sure youll find something uself here', declares the hare with a wonky smile.")
    def hare_shop(int) -> int:
        global chapter
        global player
        global points
        global attack
        global inventory
        global hp
        global max_hp
        global main_weapon
        global main_armor
        global boss
        global boss_weapon
        done: bool = False
        print('The March Hare Pawn Shop:')
        shop: list[str] = list()
        shop.append("A. 'magic pastry = Turns you into a small giant. Double attack and health while in this state.' - 15 points")
        shop.append("B. 'stylish hat =  Max. Health +6. Made by the Mad Hatter. Very stylish indeed.' - 30 points")
        shop.append("C. 'jubjub bird gloves = Attack +5. Made from the powerful feathers of the Jubjub Bird' - 60 points")
        shop.append("D. 'blue bottoms = Max. Health +10. Resembles a blue dress you have a memory of.' - 70 points")
        shop.append("E. I am finished buying.")
        while done == False:
            print(shop)
            print(f"You have {points} points.")
            buy = str(input("What do you wish to buy? "))
            if buy == "A":
                shop.pop(0)
                inventory["magic pastry"] = "Turns you into a small giant. Double attack and health while in this state."
                points -= 15
            if buy == "B":
                shop.pop(1)
                inventory["stylish hat"] = "Max. Health +6. Made by the Mad Hatter. Very stylish indeed."
                max_hp += 6
                points -= 30
            if buy == "C":
                shop.pop(2)
                inventory["jubjub bird globes"] = "Attack +5. Made from the powerful feathers of the Jubjub Bird."
                points -= 60
            if buy == "D":
                shop.pop(3)
                inventory["blue bottoms"] = "Max. Health +10. Resembles a blue dress you have a memory of."
                points -= 70
            if buy == "E":
                done = True
        return points
    hare_shop(points)
    print("'Thank you for buying at The March Hare Pawn Shop. Good luck, Heroe.' You thank the Hare, and grab the Knaves horse. They all wave one final goodbye at you, and you set off to the castles queen.")
    print("To be continued...")
    chapter = 6


def main() -> None:
    """Main function that runs each chapter of the game."""
    global chapter
    while chapter < 6:
        if chapter == -1:
            goodbye()
        if chapter == 0:
            greet()
        if chapter == 1:
            white_rabbit()
        if chapter == 2:
            rabbit_hole()
        if chapter == 3:
            welcome_to_wonderland()
        if chapter == 4:
            the_duchess_house()
        if chapter == 5:
            mad_tea_party()
    goodbye()
    return None


if __name__ == "__main__":
    main()