import random

def role_create():
    done = False
    while not done:
        try:
            role_class = {1:'戰士',2:'法師',3:'刺客'}
            skill = {1:'您習得 [蓄力一擊]，按下A可施放',2:'您習得 [火球術]，按下A可施放',3:'您習得 [連擊]，按下A可施放'}
            role = int(input("請選擇您的職業 ( 1.戰士 2.法師 3.刺客 )："))
            class_data = role_data(role)
            if role in role_class:
                print('============================')
                print(f'您選擇的職業是 [{role_class[role]}]')
                print('============================')
                print(f'{skill[role]}') if role in skill else None
                print('============================')
                print(f'[{role_class[role]}] 的基礎數值：')
                print(f'攻擊力：{class_data['dmg']} 生命值：{class_data['HP']}')
                print('============================')
                done = True
                return class_data
            else:
                print("請輸入1~3的數字來選擇職業")
        except ValueError:
            print("輸入錯誤，請輸入1~3的數字來選擇職業")

def role_data(n):
    if n == 1:
        return {
            'class':1,
            'damage':random.randint(18,20),
            'dmg':'18 ~ 20',
            'skill_dmg': 35,
            'HP':125,
        }
    elif n ==2:
        return {
            'class':2,
            'damage':15,
            'skill_dmg': 30,
            'dmg':15,
            'HP':90,
        }
    else:
        return {
            'class':3,
            'damage':random.randint(5,15),
            'skill_dmg': random.randint(15,20),
            'dmg':'5 ~ 15',
            'HP':100,
        }
def game():
    player = role_create()
    Boss_life = 100 #Boss血量
    hit = 0
    
    drop_chance = random.random()
    if player['class'] == 1:
        item = ['長柄巨斧','精鋼鎖子甲']
        while Boss_life > 0:
            crit_chance = random.random() #0~1隨機數 (判斷暴擊機率)
            crit = int(player['damage'] * 1.2) #暴擊倍率
            drop = random.choice(item) #隨機掉落物品            
            hit_type = input("按下 Enter 鍵進行攻擊或是按下 A 施放技能!")
            if hit_type == '':
                if crit_chance <= 0.1: #暴擊機率 10%
                    hit += 1
                    Boss_life -= crit                    
                    print(f'您對Boss造成了 {crit} 點暴擊傷害!!! Boss剩餘血量：{max(Boss_life,0)}')
                else:
                    hit += 1
                    Boss_life -= player['damage']                    
                    print(f'您對Boss造成了 {player['damage']} 點傷害!       Boss剩餘血量：{max(Boss_life,0)}')
            elif hit_type.lower() == 'a':
                hit += 1
                Boss_life -= player['skill_dmg']                
                print(f'您 [蓄力一擊] 對 Boss 造成了 {player['skill_dmg']} 點傷害!       Boss剩餘血量：{max(Boss_life,0)}')                
        print(f'恭喜您! Boss承受了 {hit} 次攻擊後，已被擊敗')
        if drop_chance <= 0.4:  #40%掉落率          
            print(f'Boss掉落道具 [{drop}]')
    elif player['class'] == 2: #法師無暴擊機制,也無傷害浮動
        item = ['水晶法杖','星光長袍']
        while Boss_life > 0:
            drop = random.choice(item) #隨機掉落物品           
            hit_type = input("按下 Enter 鍵進行攻擊或是按下 A 施放技能!")
            if hit_type == '':
                hit += 1
                Boss_life -= player['damage']                
                print(f'您對Boss造成了 {player['damage']} 點傷害!       Boss剩餘血量：{max(Boss_life,0)}')
            elif hit_type.lower() == 'a':
                hit += 1
                Boss_life -= player['skill_dmg']                
                print(f'您發動 [火球術] 對 Boss 造成了 {player['skill_dmg']} 點傷害!       Boss剩餘血量：{max(Boss_life,0)}')                
        print(f'恭喜您! Boss承受了 {hit} 次攻擊後，已被擊敗')
        if drop_chance <= 0.4:            
            print(f'Boss掉落道具 [{drop}]')
    elif player['class'] == 3:
        item = ['斥侯短刀','巨獸皮衣']
        while Boss_life > 0:
            crit_chance = random.random() #暴擊機率
            crit = int(player['damage'] * 1.5) #暴擊倍率
            drop = random.choice(item)            
            hit_type = input("按下 Enter 鍵進行攻擊或是按下 A 施放技能!")
            if hit_type == '':
                if crit_chance <= 0.25:
                    hit += 1
                    Boss_life -= crit                    
                    print(f'您對Boss造成了 {crit} 點暴擊傷害!!! Boss剩餘血量：{max(Boss_life,0)}')
                else:
                    hit += 1
                    Boss_life -= player['damage']                    
                    print(f'您對Boss造成了 {player['damage']} 點傷害!       Boss剩餘血量：{max(Boss_life,0)}')
            elif hit_type.lower() == 'a':
                hit += 1
                first = player['skill_dmg']
                second = player['skill_dmg']
                Boss_life -= (first + second)                
                print(f'您 [連擊] Boss 造成了 {first} 及 {second}  點傷害!       Boss剩餘血量：{max(Boss_life,0)}')                
        print(f'恭喜您! Boss承受了 {hit} 次攻擊後，已被擊敗')
        if drop_chance <= 0.65:            
            print(f'Boss掉落道具 [{drop}]')

game()