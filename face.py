from shapes import Oval, Rectangle, Triangle,Paper
canvas = Paper()

rect1 = Rectangle()
rect1.set_width(10)
rect1.set_height(10)
rect1.set_color('red')
rect1.set_x(100)
rect1.set_y(100)

rect1.draw()

rect2 = Rectangle()
rect2.set_width(10)
rect2.set_height(10)
rect2.set_color('red')
rect2.set_x(200)
rect2.set_y(100)


tri = Triangle(160,160,170,170,150,170)
tri.set_color('green')
tri.set_x(150)
tri.set_y(150)


rect3 = Rectangle()
rect3.set_width(100)
rect3.set_height(10)
rect3.set_color('red')
rect3.set_x(100)
rect3.set_y(200)

rect1.draw()
rect2.draw()
rect3.draw()
tri.draw()



canvas.display()
