########################################
# The questions ends here.             #
# The game lore starts here!!!!!!      #
#                                      #
########################################

label label_start:

    D "*You wake up in your bed, you look at the clock and it's 7:00 AM. You get out of bed and get ready for the day.*"
    D "Uh... I'm so tired, I should get some coffee."
    D "*You walk to the kitchen and make some coffee.*"
    D "*You drink the coffee and feel more awake.*"
    D "I should get going to school."
    D "*You look yourself in the mirror.*"

    show DudaIdle1

    D "*You look at yourself and think...*"
    menu:
        D "Should I go to school...or...Stay at home?"

        "Go to school":
            play sound click
            jump label_school
        "Stay home":
            play sound click
            jump label_home

# Wrong choice 1.

label label_home:

    hide DudaIdle1
    "Narrator" "You decide to stay home and play some games."
    "Narrator" "You play some games and then you get bored."
    $ Nothing = True
    jump label_night1

#Correct choice 1.

label label_school:

    hide DudaIdle1
    scene school
    with fade
    D "*You decide to go to school.*"
    D "*You arrive at school and go to your classroom.*"
    D "*The day passes and nothing really happens, you feel like u have wasted another day...*"
    scene train
    with fade
    D "*You take the train home.*"
    D "*You sit down*"
    U "Hey. Mind if I sit by ur side?"
    if Lesbian:
        "*You look at her up and down.*"
        jump label_TheMeeting
    else:
        "*You look at him up and down.*"
        jump label_TheMeeting

label label_TheMeeting:

    if Lesbian:
        show LinIdle1
    else:
        show LimaIdle1
    U "So? Can I sit here?"

menu:
    "Yes":
        play sound click
        jump label_Lima
    "No":
        play sound click
        jump label_LimaGoesAway

# Intro to the character Lima.

label label_Lima:
    hide LimaIdle1
    hide LinIdle1
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    U "Thanks. My name is Lima, what's yours?"
    L "Also, I'm gender neutral so don't worry about saying he or she!"
    L "*Lima smiles at you*"
    hide LinTalking
    hide LimaTalking
    if Lesbian:
        show LinSmile
    else:
        show LimaSmile

menu:
    "Duda":
        play sound click
        jump label_Lima2
    "*Don't say anything*":
        play sound click
        jump label_LimaGoesAway

# Wrong choice 2.

label label_LimaGoesAway:
    hide LinSmile
    hide LimaSmile
    "Narrator" "He felt like he was disturbing therefore you two didn't talk anymore."
    "Narrator" "You arrive at your stop and get off the train."
    $ Nothing = True
    jump label_night1

# Correct choice 2.

label label_Lima2:
    hide LinSmile
    hide LimaSmile
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    L "Nice to meet you Duda!"
    L "So, what are you doing here?"
    hide LimaTalking
    hide LinTalking
    if Lesbian:
        show LinIdle1
    else:
        show LimaIdle1
    D "*You look at Lima and think...*"
    D "I'm going home."
    hide LimaIdle1
    hide LinIdle1
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    L "Oh, I see. I'm going home too."
    L "How old are you?"
    hide LinTalking
    hide LimaTalking
    if Lesbian:
        show LinIdle1
    else:
        show LimaIdle1
    D "*You look at Lima and think...*"

    if Younger:
        menu:
            "23 years old.":
                play sound click
                jump label_Lima3
            "Don't say anything.":
                play sound click
                jump label_LimaGoesAway
    else:
        menu:
            "24 years old.":
                play sound click
                jump label_Lima3
            "Don't say anything.":
                play sound click
                jump label_LimaGoesAway

# Correct choice 3.

label label_Lima3:
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    L "Oh, I'm 24 years old!"
    L "What do you do for a living?"
    hide LinTalking
    hide LimaTalking
    if Lesbian:
        show LinIdle1
    else:
        show LimaIdle1
    D "*You look at Lima and think...*"
    D "I'm a student. I go to Neo-Tokyo University."
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    L "Oh, I see. I left university a few years ago."
    L "I'm a programmer now."
    L "I work at a company called 'CyberLife'."
    L "Have you heard of it?"
    hide LinTalking
    hide LimaTalking
    D "No, I haven't."
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    L "Oh, okay! No worries."
    L "I could show you around the company one day. If you want ofc."
    hide LinTalking
    hide LimaTalking
    if Lesbian:
        show LinIdle1
    else:
        show LimaIdle1
    D "*You look at Lima and think...*"

menu:
    "Yes, that would be nice.":
        play sound click
        jump label_Lima4
    "No, I'm not interested.":
        play sound click
        jump label_Lima4

label label_Lima4:
    D "*You think to yourself that, that was quite fast and that you don't even know him.*"
    D "*It's not like u really interacted with him before. So you don't really have the intention to go.*"
    hide LinIdle1
    hide LimaIdle1
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    L "Oh. Don't worry about it. TBH with you, that isn't really what I do."
    L "I just wanted to get to know you better."
    L "I think you are really pretty and have a beutiful smile. I had to just say something."
    hide LinTalking
    hide LimaTalking
    if Lesbian:
        show LinIdle1
    else:
        show LimaIdle1
    D "So what do you do for a living?"
    hide LinIdle1
    hide LimaIdle1
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    L "I'd rather not say. It's a bit complicated."
    L "But I can tell you that I didn't lie about everything I am a programmer."
    L "I just don't work at CyberLife."
    hide LinTalking
    hide LimaTalking
    "Narrator" "The train arrives at Lima's stop."
    if Lesbian:
        show LinTalking
    else:
        show LimaTalking
    L "Well, this is my stop. I'll see you around."
    hide LinTalking
    hide LimaTalking
    L "*Lima gets off the train*"
    "Narrator" "You suddenly feel like this is a opportunity to get to know someone."
    "Narrator" "You don't really interact with people that much."
    "Narrator" "You don't really have friends."
    "Narrator" "You feel like you should get to know Lima better. But there's something holding you back."

menu:
    "*Go after Lima.*":
        play sound click
        jump label_Lima5
    "*Don't go after Lima.*":
        play sound click
        jump label_GoHome

label label_Lima5:
    D "*You get off the train and go after Lima.*"
    D "*You see Lima walking down the street.*"
    D "*You run after Lima.*"
    D "*You look at him in the distance.*"
    D "*He goes into a alley.*"
    D "*You go into the alley.*"
    D "*You see Lima in the distance.*"
    D "*Theres someone in the distance talking with him.*"
    if Lesbian:
        show LinIdle1 at left
    else:
        show LimaIdle1 at left
    show WeirdGuyTalking at right
    "WeirdGuy" "So, you are sure you want to do this?"
    "WeirdGuy" "You know what will happen if you do this right?"
    "WeirdGuy" "You will lose everything you have."
    "WeirdGuy" "You will lose your job, your friends, your family, your life."
    "WeirdGuy" "You will be a fugitive."
    hide WeirdGuyTalking
    show WeirdGuy at right
    D "*U start questioning yourself if this is even safe.*"
    hide LimaIdle1
    hide LinIdle1
    if Lesbian:
        show LinTalking at left
    else:
        show LimaTalking at left
    L "I know what I'm doing."
    L "I'm tired of living this life."
    L "I want to be free."
    hide LinTalking
    hide LimaTalking
    hide WeirdGuy
    show WeirdGuyTalking at right
    if Lesbian:
        show LinIdle1 at left
    else:
        show LimaIdle1 at left
    "WeirdGuy" "Okay, if you are sure."
    "WeirdGuy" "I'll do it."
    play sound gunshot
    "Narrator" "*The weird guy pulls out a gun and shoots Lima.*"
    hide LinIdle1
    hide LimaIdle1
    hide WeirdGuyTalking
    "*You are shocked and don't know what to do.*"
    show AyoSurprised
    "*You run away from the alley. Yet U hit against someone and fall to the ground*"
    jump label_Ayo

label label_Ayo:
    hide AyoSurprised
    show AyoIdle1
    "Narrator" "*The person you hit against helps you up while making a \"SHHH\" sound to not alert anyone.*"
    jump label_ayo_intrudaction

label label_GoHome:
    "Narrator" "*You arrive at your stop and get off the train.*"
    "Narrator" "*You walk home and think about what happened.*"
    "Narrator" "*You arrive at your house."
    $ Nothing = True
    jump label_night1