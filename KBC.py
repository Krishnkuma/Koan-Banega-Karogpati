import random
import time
for i in range(80):
    print("*",end="")
    time.sleep(0)
print("\n\t\t\t WELCOME TO")
print("\t\t     KOAN BANEGA KARAGPATI")
for i in range(80):
    print("*",end="")
    time.sleep(0)
a=input("\n\t enter your name-")
for i in range(80):
    print("*",end="")
    time.sleep(0)
print("\n\tOK,",a,"let's start the game")
time.sleep(1)
questions=["Who is the PM of india","In Which Country Area 51 is located","which one is the largest continent in the world","what is the latest version of windows","which one of these is not a software company","how many mb makes 1 GB","facebook was firstly developed by","founder of apple is","________ is one of the founder of google","big boss season 13 starts in _____& ends in _____","apple's laptop is also known as","first apple computer is known as","joystick is used for","____ is used to encrypt drives in computer"]
answer=["narendra modi","united states","asia","windows 10","honda","1024","mark zuckenberg","steve jobs","larry pags","2019-2020","macbook","mactonish","playing games","bitlocker"]
wronganswers=[["aditya nath","ashok gahlot","amit shah"],["india","china","rus"],["usa","africa","urope"],["windows 7","windows 8","windows 9"],["oracal","google","ms"],["1002","512","2024"],["bill gates","larry page","sunder pichai"],["azhar","charles","sunder pichai"],["larry","sunder pichai","bill gates"],["2020-2021","22-23","coming soon"],["thin book","note book","chrome book"],["apple v.1","apple computer","appbook"],["input","output","all"],["keyguard","windows secure","no software like this"]]
attempquestion=[]
count=1
amount=0
while True:
    while True:
        selectquestion=random.choice(questions)
        if selectquestion in attempquestion:
            pass
        elif selectquestion not in attempquestion:
            attempquestion.append(selectquestion)
            questionindex=questions.index(selectquestion)
            correctanswer=answer[questionindex]
            break
    optionlist=[]
    inoptionlist=[]
    optioncount=1
    while optioncount<4:
        optionselection=random.choice(wronganswers[questionindex])
        if optionselection in optionlist:
            pass
        elif optionselection not in optionlist:
            optionlist.append(optionselection)
            inoptionlist.append(optionselection)
            optioncount+=1
    optionlist.append(correctanswer)
    alreadydisplay=[]
    optiontodisplay=[]
    a1=True
    while a1:
        a=random.choice(optionlist)
        if a in alreadydisplay:
            pass
        else:
            alreadydisplay.append(a)
            optiontodisplay.append(a)
            a1=not True
    a1=True
    while a1:
        b=random.choice(optionlist)
        if b in alreadydisplay:
            pass
        else:
            alreadydisplay.append(b)
            optiontodisplay.append(b)
            a1=not True
    a1=True
    while a1:
        c=random.choice(optionlist)
        if c in alreadydisplay:
            pass
        else:
            alreadydisplay.append(c)
            optiontodisplay.append(c)
            a1=not True
    a1=True
    while a1:
        d=random.choice(optionlist)
        if d in alreadydisplay:
            pass
        else:
            alreadydisplay.append(d)
            optiontodisplay.append(d)
            a1=not True
    rightanswer=""
    if correctanswer==a:
        right_answer='a'
    elif correctanswer==b:
        right_answer='b'
    elif correctanswer==c:
        right_answer="c"
    elif correctanswer==d:
        right_answer="d"
    print("--------------------------------------------------------------------------------------")
    print("\n\t\tAmount win=",amount)
    print("--------------------------------------------------------------------------------------")
    time.sleep(1)
    print("\n\t Question",count,"on your screen")
    print("--------------------------------------------------------------------------------------")
    time.sleep(1)
    print(" | Question-",selectquestion)
    print("--------------------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|A",a)
    print("--------------------------------------------------------------------------------------")
    print("\t|B",b)
    print("--------------------------------------------------------------------------------------")
    print("\t|C",c)
    print("--------------------------------------------------------------------------------------")
    print("\t|D",d)
    print("--------------------------------------------------------------------------------------")
    useranswer=input("\t\tEnter Correct Option\t   or \t press Q to quit.\n\t\t\t...")
    if useranswer==right_answer:
        if count==1:
            amount=1000
        elif count==2:
            amount=2000
        elif count==3:
            amount=5000
        elif count==4:
            amount=10000
        elif count==5:
            amount=40000
        elif count==6:
            amount=80000
        elif count==7:
            amount=160000
        elif count==8:
            amount=320000
        elif count==9:
            amount=640000
        elif count==10:
            amount=1500000
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("*********************************************************************************")
            print("\t\t\t \\\\\\\\\\ Congratulations! //////////")
            print("\t\t\t|||||||||| You Won The Game ||||||||||")
            print("*********************************************************************************")
            print("\n\n\t\t You Won Rs. ",amount)
            print()
            break
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("*********************************************************************************")
        print("\t\t\t \\\\\\\\\\ Congratulations! //////////")
        print("\t\t\t|||||||||| Right Answer ||||||||||")
        print("*********************************************************************************")
        count+=1
    elif useranswer=="q":
            print("\n\n\t\t You Won Rs. ",amount)
            break
    else:
        print("*********************************************************************************")
        print("\t\t\tWrong Answer")
        print("*********************************************************************************")
        print("\n\n\t\t \tYou Won Rs. ",amount)
        print("*********************************************************************************")

        break

    
    
    
