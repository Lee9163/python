#input 取得使用者輸入

name=input("請輸入名字")
print(f"你的名字是{name}")

#練習一 填詞遊戲
adj_1=input("請輸入第一個形容詞")
noun=input("請輸入一個名詞")
adj_2=input("請輸入第二個形容詞")
verb=input("請輸入一個動詞")
adj_3=input("請輸入第三個形容詞")

print(f"今天去一個{adj_1}的動物園，看到一隻{noun}，有隻{noun}很{adj_2}，正在{verb}，我感到{adj_3}")

#計算矩形面積
length=float(input(f"請輸入矩形長度"))
width=float(input(f"請輸入矩形寬度"))

area=length*width
print(f"面積為{area}")

#購物車程式
item=input("你想要什麼物品")
price=float(input("價格多少"))
quantity=int(input("要買幾件"))

total=price*quantity
print(f"你買了{quantity}個{item}，總價{total}元")
