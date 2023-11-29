label label_night1:
    scene DudaRoom
    with fade
    "Narrator" "It's night time. You're in your room, and you're about to go to sleep."
    "Narrator" "You're not sure what to do."
    "Narrator" "You could go to sleep, or you could stay up and do something."
    "Narrator" "In the end u just decide to go to sleep."
    if Nothing:
        jump label_NothingHappened
    else:
        jump check1

label check1:
    if Lima:
        jump label_limaEnd
    else:
        jump check2

label check2:
    if Lin:
        jump label_linEnd
    else:
        jump check3

label check3:
    if Ayo:
        jump label_ayoEnd
    else:
        jump check4

label check4:
    if Kira:
        jump label_kiraEnd
    else:
        jump check5

label check5:
    if HookUps:
        jump label_hookUpsEnd
    else:
        jump check6

label check6:
        jump label_morning2

