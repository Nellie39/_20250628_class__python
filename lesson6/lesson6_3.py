import argparse
import random
# 猜數字遊戲
# 這是一個簡單的猜數字遊戲，玩家需要猜一個隨機生成的數字
# 在每次遊戲中，玩家可以輸入一個範圍內的數字，直到猜中為止
# 遊戲會提示玩家猜的數字是大了還是小了  
# 玩家可以選擇是否繼續遊戲
# 如果沒有輸入姓名，則使用預設值

playCount = 1
parser = argparse.ArgumentParser(description="猜數字遊戲")
parser.add_argument("-n", "--name",type=str, help = "姓名")
args = parser.parse_args()

if not args.name:
    name = input("請輸入姓名:")
else:
    name = args.name
min = 1
max = 100
count = 0
target = random.randint(min,max)
print(f"========猜數字遊戲第{playCount}次=========\n\n")
while(True):
    keyin = int(input(f"猜數字範圍{min}~{max}:"))
    count += 1
    if(keyin>=min and keyin<=max):
        if target == keyin:
            print(f"賓果!猜對了, 答案是:{target}")
            print(f"你共猜了{count}次\n")
            again = input("要繼續嗎?(y,n)")
            if again == "y":
                playCount += 1
                min = 1
                max = 100
                count = 0
                target = random.randint(min,max)
                print(f"========猜數字遊戲第{playCount}次=========\n\n")
                continue
            else:
                break 
        elif(keyin > target):
            print(f"猜錯了!再小一點")
            max = keyin - 1
        else:
            print(f"猜錯了!再大一點")
            min = keyin + 1
            print(f"{name}已經猜{count}次\n")
    else:
        print("請輸入提示範圍內的數字\n")

print(f"遊戲結束,{name}共玩了{playCount}次")
