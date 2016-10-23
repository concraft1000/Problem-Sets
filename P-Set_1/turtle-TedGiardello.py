import turtle
import math as m

turtle.Screen()
t = turtle.Turtle()
bird = t

def _draw_s_(r1, r2): #r1 > r2, r1 = 3, r2 = 2
	a = (r1 * 20 * m.pi)/180
	b = (r2 * 20 * m.pi)/180
	k = 100/5.5
	t.right(180)
	t.right(20)
	for i in range(180):
		t.left(1)
		t.forward(a)
	for i in range(180):
		t.right(1)
		t.forward(b)
	t.right(90)
	t.back(k)
	t.right(90)
	for i in range(180):
		t.left(1)
		t.forward(a)
	for i in range(180):
		t.right(1)
		t.forward(b)
	t.right(90)
	t.back(k)
	t.left(20)

bird.up()
bird.back(225)
bird.left(90)
bird.forward(100)
bird.right(90)
bird.down()

if 1: #draws the letter 'S' curve form
	_draw_s_(3, 2)

	bird.up()
	bird.left(90)
	bird.forward(30)
	bird.right(90)
	bird.forward(200)
	bird.left(90)
	bird.forward(30)
	bird.down()

if 0: #draws the letter 'S' block form
	t.forward(100)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(40)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(40)
	t.left(90)
	t.forward(100)

	bird.up()
	bird.forward(50)
	bird.down()

if 1: #draws the letter 'F'
	t.left(90)
	t.forward(200)
	t.right(90)
	t.forward(100)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(60)
	t.left(90)
	t.forward(40)
	t.left(90)
	t.forward(60)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(60)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.back(40)
	t.forward(40)

bird.up()
bird.forward(110)
bird.down()

if 1: #draws the letter 'H'
	t.left(90)
	t.forward(200)
	t.right(90)
	t.forward(33)
	t.right(90)
	t.forward(80)
	t.left(90)
	t.forward(34)
	t.left(90)
	t.forward(80)
	t.right(90)
	t.forward(33)
	t.right(90)
	t.forward(200)
	t.right(90)
	t.forward(33)
	t.right(90)
	t.forward(80)
	t.left(90)
	t.forward(34)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.back(33)

if 1: #draws the letter 'S' curve form
	bird.up()
	bird.forward(147)
	bird.left(90)
	bird.forward(190)
	bird.right(310)
	bird.down()

	_draw_s_(3, 2)

if 0: #draws the letter 'S' block form
	bird.up()
	bird.forward(117)
	bird.down()

	t.forward(100)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(40)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(40)
	t.left(90)
	t.forward(100)