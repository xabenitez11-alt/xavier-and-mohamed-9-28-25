# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Billy")


# The game starts here.

label start:
    "A kid loging into roblox"

label background:
    scene bg row

    show bill_s at right
    "A kid loging into roblox"
    "Billy" "How do I login?"
    "Computer" "Enter date of bith."
    "Billy" "(billy does not understand the concept of dates of birth or how to sign up for roblox, so he enters the biggest number he knows. )"

scene bg car
show bill_s at right
show old_s at left
"Soilder" "YOU IN AGE TO JOIN THE MILATRY!"
"Billy" "Uhhh what?"
"Soilder" "YOUR COMING WITH ME!"
show bill_s at right
hide bill_s at right
show old_s at left
hide old_s at left

"10 years later: during a war"
scene bg war
show old_s at left
show billy_old at right
"Soilder" "GREANDE GET DOWN!"
"Billy" "(sacrifices himself for save the soldier)"
"Billy" "(explodes)"
hide billy_old at right
show ex at right
"Soilder" "NO BILLY!!"
hide ex at right 
show dead at right
"Soilder" "at least hes gone."
return
