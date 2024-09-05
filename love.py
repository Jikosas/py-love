import turtle

# Inisialisasi layar dan turtle
screen = turtle.Screen()
pen = turtle.Turtle()

# Menggambar bentuk love
def curve():
    for _ in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def display_text():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')
    pen.write('I Love You', font=("Verdana", 12, "bold"))

heart()
display_text()
pen.hideturtle()

# Tampilkan hasil
screen.mainloop()
