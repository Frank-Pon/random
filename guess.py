import random

target = random.randint(1,10)
count = 0

while count < 10:
    try:
        ans = int(input('請輸入數字：'))
        count += 1
        if ans == target:
            print(f'恭喜你在第 {count} 次猜中了!')
            break
        else:
            print(f'猜錯了,還有 {10-count} 次機會')
    except ValueError:
        print("請輸入正確數字 (不扣次數)")