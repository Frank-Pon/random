import random 

countdict = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}

trigger = True
while trigger:
    try:
        n=0   
        m=int(input("請輸入擲骰子次數：")) 
        while n<m:
            result = random.randint(1,6)
            countdict[result]+=1
            n+=1
        print('骰子次數統計：')
        print(f'1點 {countdict[1]} 次')
        print(f'2點 {countdict[2]} 次')
        print(f'3點 {countdict[3]} 次')
        print(f'4點 {countdict[4]} 次')
        print(f'5點 {countdict[5]} 次')
        print(f'6點 {countdict[6]} 次')
        trigger = False
    except ValueError:
        print("您輸入的不是數字，請重新輸入")
