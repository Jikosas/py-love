def draw_love_with_stars():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
    pen.forward(112)
    pen.end_fill()

draw_love_with_stars()
