import time
import os
import turtle



#启动
print("欢迎使用智能聊天机器人！系统启动中")
print("Loading",end = "")
for i in range(6):
    print(".",end = '',flush = True)
    time.sleep(0.4)
print("""
系统目前仅支持包含“笑话”，“你好”，“时间”，“退出”等的对话哦
详细的使用指南请输入“帮助”
部分版本使用完成后务必输入“退出”后再关闭窗口，以免影响到第二次使用""")
#定义函数
def printer(text, delay=0.1):
    """打字机效果"""
    
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)

def hart_arc():

    for i in range(200):

        turtle.right(1)

        turtle.forward(2)

  
def move_pen_position(x, y):

    turtle.hideturtle()    
    turtle.up()     
    turtle.goto(x, y)   
    turtle.down()  
    turtle.showturtle()  
#核心

while True:
    a=input("""请输入你的回答？
——""")
    if "你好" in a:
        printer("""——你好!
——""")


    elif "笑话" in a:
        b=input("""——有3个笑话，请选择（1；2；3）
——""")
        b=int(b)
        if b==1:
            printer("""——有一天奥特曼去学校上课，课上老师提问,
奥特曼一举手，老师就受伤了……
——""")
            printer("""是不是很搞笑!
——""")
        elif b==2:
            printer("""——护士看到一病人在病房喝酒，就走过去,
小声地对他说：“小心肝！”病人微笑着说：“小宝贝。”
——""")
            printer("""是不是很搞笑!
——""")
        elif b==3:
            printer("""——办公室的鱼缸里养了几只透明的虾, 
领导没看出来，问一位职员养了什么，职员回答道，“虾(瞎)啊，真是虾(瞎)！”
领导愣了，走了。职员还补充道：“领导，虾(瞎)啊，是真虾(瞎)啊！”
——""")
            printer("""是不是很搞笑!
——""")
        else:
            printer:("""——抱歉，暂无此笑话！
——""")


    elif "时间" in a :
        printer("——现在的时间是")
        printer(time.strftime('%Y/%m/%d %H:%M:%S'))
        printer("""
——""")


    elif "谜语" in a:
        d=input("""——共有5个谜语，请选择（1；2；3；4；5）
——""")
        d=int(d)
        if d==1:
            谜语1=input("""——两人前功尽弃，猜一个字
——""")
            if "伤" in 谜语1:
                printer("""——答对啦！
——""")
            else:
                printer("""——答错了，答案是 伤
——""")
        elif d==2:
            谜语2=input("""——一百减一，猜一个字
——""")
            if "白" in 谜语2:
                printer("""——答对啦！
——""")
            else:
                printer("""——答错了，答案是 白
——""")
        elif d==3:
            谜语3=input("""——一只牛，猜一个字
——""")
            if "生" in 谜语3:
                printer("""——答对啦！
——""")
            else:
                printer("""——答错了，答案是 生
——""")
        elif d==4:
            谜语4= input("""——七十二小时，猜一个字
——""")
            if "晶" in 谜语4:
                printer("""——答对啦！
——""")
            else:
                printer("""——答错了，答案是 晶
——""")
        elif d==5:
            谜语5=input("""——有耳能听话，猜一个字
——""")
            if "门" in 谜语5:
                printer("""——答对啦！
——""")
            else:
                printer("""——答错了，答案是 生
——""")
        else:
            printer("抱歉，选项无效！")


    elif "画画" in a:
        e=input("""——请选择（仅输入数字）
1.三角形
2.五角星
3.爱心
4.月亮
完成选择后请注意turtle库的弹窗
关闭弹窗即可回到聊天界面
部分版本不能连续运行！
——""")
        e=int(e)
        if e==1:
            turtle.pencolor("blue")
            turtle.pensize(10)
            turtle.backward(100)
            turtle.left(60)
            turtle.forward(200)
            for __count in range(2):
                turtle.right(120)
                turtle.forward(200)
            turtle.done()
        elif e==2:
            turtle.pensize(10)
            turtle.pencolor("blue")
            turtle.fillcolor("red")
            turtle.begin_fill()
            for __count in range(5):
                turtle.forward(200)
                turtle.right(144)
            turtle.end_fill()
            turtle.done()
        elif e==3:
            turtle.color('red', 'hotpink')     
            turtle.pensize(3) 
            turtle.speed(4) 
            move_pen_position(x=0,y=-180)
            turtle.left(140)
            turtle.begin_fill()
            turtle.forward(224)     
            hart_arc()      
            turtle.left(120)    
            hart_arc()      
            turtle.forward(224)
            turtle.end_fill()
            turtle.done()
        elif e == 4:
            
            turtle.speed(1)
            turtle.pencolor("blue")
            turtle.fillcolor("blue")
            turtle.begin_fill()
            turtle.back(200)
            turtle.forward(400)
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(400)
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.end_fill()
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.forward(150)
            turtle.circle(100)
            turtle.end_fill()
            turtle.fillcolor("blue")
            turtle.begin_fill()
            turtle.forward(80)
            turtle.circle(100)
            turtle.end_fill()
            turtle.done()

        else:
            printer("抱歉，选项无效")
            



    elif "帅" in a:
        printer("""——当然是你了！
——""")
    elif "美" in a:
        printer("""——当然是你了！
——""")
    elif "身份" in a:
        os.system('python 身份识别.py')



    elif "退出" in a:
        printer("——好的，退出中！")
        time.sleep(0.1)
        os._exit(0) 
    elif "帮助" in a:
        print("""使用指南：
仅支持包含“笑话”“谜语”“时间”“帮助”
“你好”“画画”“谁最帅（美）”“退出”的对话！
设定了3个笑话，5个谜语，4个图画

""")
    else:
        printer("""——我暂时还听不懂！我目前仅支持“笑话”，“你好”，“退出”等
其他的内容请输入“帮助”查看。
——""")
