from mod import role_create,warrior,mage,assasin

def game():
    character = int(input("請選擇您的職業 ( 1.戰士 2.法師 3.刺客 )："))
    player=role_create(character)
    if character == 1:
        warrior(player)
    elif character == 2:
        mage(player)
    else:
        assasin(player)
    
game()