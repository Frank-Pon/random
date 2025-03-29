import random 


conti = True
while conti:
    ans = input("是否繼續擲骰子 ( Y / N ):")
    if ans.upper() == 'Y' or ans.lower() == 'y':
        print(random.randint(1,6))
    elif ans.upper() == 'N' or ans.lower() == 'n':
        print('結束遊戲!')
        conti = False
    else:
        print('輸入無效，請輸入 Y ( 繼續遊戲 ) 或是 N ( 結束遊戲 )')

