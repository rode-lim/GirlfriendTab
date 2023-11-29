########################################
# Consent is important.                #
# The questions starts here.           #
#                                      #
# Intruduction:                        #
#                                      #
# Theme, Characters and much more!     #
#                                      #
########################################

label label_intruduction:

    play music background

    scene TheCity
    with fade

    "Narrator" "The year is 2077, and the sprawling metropolis of Neo-Tokyo is the epicenter of technological innovation, corporate greed, and societal division."
    "Narrator" "In the aftermath of a catastrophic cyber-war that ravaged the world, the city emerged as a beacon of hope for some and a shadowy underworld for others."
    scene DudaRoom
    with fade

##############################################################################################################--NAME

    "Narrator" "Your name is?"

menu:
    "Duda":
        play sound click
        jump label_question1

##############################################################################################################--GENDER

label label_question1:
    "Narrator" "Your gender is?"

menu:

    "Female":
        play sound click
        jump label_question2
    "WIP":
        play sound click
        $ Female = False
        jump label_end

##############################################################################################################--AGE

label label_question2:
    "Narrator" "Your age is?"

menu:
    "23 years old, you wore born in 2054.":
        play sound click
        jump label_question3
    "24 years old, you wore born in 2053.":
        play sound click
        $ Younger = False
        jump label_question3

##############################################################################################################--OCCUPATION

label label_question3:
    "Narrator" "Your occupation is?"

menu:
    "Student":
        play sound click
        jump label_question4

##############################################################################################################--DATING

label label_question4:
    "Narrator" "Yes! That's correct. You are a student at a university. The university is called Neo-Tokyo University."
    "Narrator" "Have you dated before?"
    jump label_NSFWQuestion1

label label_NSFWQuestion1:
menu:
    "Yes":
        play sound click
        $ Dated = True
        jump label_NSFWQuestion2
    "No":
        play sound click
        jump label_NSFWQuestion2

##############################################################################################################--SEXUALITY

label label_NSFWQuestion2:
    "Narrator" "What is your sexual preference?"
menu:
    "Man and woman!":
        play sound click
        $ Bissexual = True
        jump label_NSFWQuestion3
    "Man":
        play sound click
        jump label_NSFWQuestion3
    "Woman":
        play sound click
        $ Lesbian = True
        jump label_NSFWQuestion3

##############################################################################################################--SEXUAL EXPERIENCE

label label_NSFWQuestion3:
    "Narrator" "What is your sexual experience?"
menu:
    "Virgin":
        play sound click
        jump label_start
    "Experienced":
        play sound click
        $ SexualExperience = True
        jump label_start

##############################################################################################################