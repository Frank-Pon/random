⭐Random 庫練習

簡介:

除了基本的擲骰子、猜數字等等，還延伸出一個額外的小型遊戲模擬專案RPG_simulator

內容包含模擬戰鬥、技能施放、攻擊、暴擊、裝備隨機掉落等機制的遊戲系統

👉 詳情請見 RPG_simulator 內附的 README.md！


功能使用說明:

擲骰子：每次擲出一顆骰子 隨機輸出 1 ~ 6

擲多次骰子：使用者可輸入骰幾次，結束後統計 1 ~ 6 出現次數

猜數字：使用者可以猜 1 ~ 10 的數字，總共 10 次機會


✔️Random

專案結構:

```
Random
  ├─ dice.py (擲骰子)
  ├─ dicecount.py (擲骰子計算點數出現次數)
  ├─ guess.py (猜數字)
  ├─ README.md (程式簡介)
  └─ RPG_simulator/ (Random庫RPG小遊戲)
           ├─ crit_mod.py (RPG小遊戲 - 無拆版)
           ├─ crit_mod2.py (RPG小遊戲 - 拆分主程式)
           ├─ mod.py (RPG小遊戲 - 拆分模組)
           └─ README.md (程式簡介)
```

使用方法:

( Git Clone用網址 https://github.com/Frank-Pon/random.git ) clone之後 -> cd random -> 在終端機輸入 python dice.py -> 執行✅


專案學習心得:

👉 詳情請見 RPG_simulator 內附的 README.md！