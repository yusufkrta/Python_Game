import turtle
import random

ekran=turtle.Screen()
ekran.bgcolor("light blue")
ekran.title("Game")
skor_kalem = turtle.Turtle()
geri_Sayım = turtle.Turtle()
FONT = ("AriaL",40,"normal")
x = ekran.window_height() / 2
y = x * 0.8
score = 0
game_over = False  # oyun bitmedi değişkeni
# turtle List
turtleList = []
def skor_yazdırma():
    skor_kalem.penup()
    skor_kalem.setpos(0,y)
    skor_kalem.hideturtle()
    skor_kalem.write(arg="Skor: 0" , move=False , align="center", font=FONT)

YER_SAYISI = 10

def oyunTurple(a,b):
    t = turtle.Turtle()

    def tıklamaFunc(x,y):
        global score
        score = score + 1
        skor_kalem.clear()
        skor_kalem.write(arg=f"Score: {score}", move=False, align="center", font=FONT)
    t.onclick(tıklamaFunc)
    t.turtlesize(3)
    t.penup()
    t.color("green")
    t.goto(a * YER_SAYISI , b * YER_SAYISI )
    t.shape("turtle")
    turtleList.append(t)


xKordinati = [-20,-10,0,10,20]
yKordinati = [-20,-10,0,10]

def for_exe():
    for a in xKordinati:
        for b in yKordinati:
            oyunTurple(a,b)

def turtle_gizleme():
    for g in turtleList:
        g.hideturtle()

def rastgele_turple_gosterme():
    if not game_over: # oyun bitmediyse
        turtle_gizleme()
        random.choice(turtleList).showturtle()
        ekran.ontimer(rastgele_turple_gosterme,500)
    else:
        turtle_gizleme()

def geriSayım(time):
    global game_over
    geri_Sayım.penup()
    geri_Sayım.setpos(0, y-50)
    geri_Sayım.hideturtle()
    geri_Sayım.clear()
    if time > 0:
        geri_Sayım.clear()
        turtle_gizleme()
        geri_Sayım.write(arg=f"Time {time}", move=False, align="center", font=FONT)
        ekran.ontimer(lambda: geriSayım(time-1),1000)
    else:
        game_over = True
        geri_Sayım.clear()
        geri_Sayım.write(arg="Game Over", move=False, align="center", font=FONT)






turtle.tracer(0)

for_exe()
skor_yazdırma()
geriSayım(20)
turtle_gizleme()
rastgele_turple_gosterme()

turtle.tracer(1)

turtle.mainloop()




