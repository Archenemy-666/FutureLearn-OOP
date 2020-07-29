from shapes import Paper , Rectangle
paper = Paper()


rect = Rectangle()
rect.set_color('yellow')
rect.set_height(50)
rect.set_width(150)
rect.draw()
rect.set_x(0)
rect.set_y(0)


rect2 = Rectangle()
rect2.set_color('blue')
rect2.set_height(10)
rect2.set_width(10)
rect2.draw()
rect2.set_x(150)
rect2.set_y(200)



paper.display()



