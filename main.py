import turtle as t
import keyboard 
import time



#window size
window_width = 960
window_height = 640

#screen setup

screen = t.Screen()

screen.setup(window_width, window_height)
screen.bgcolor("black")
screen.tracer(0)

t.pencolor("red")
t.pensize(0.5)
t.speed(0)
t.ht()

#Camera position

camX = 0
camY = 0
camZ = 0

#FOV
fov_val = 30
fov = max(30, min(fov_val, 120))


class draw:

    #goto function

    @staticmethod
    def goto(x=0,y=0,z=1):
        #math
        t.goto((0.5 * fov_val) * ((x + camX) / (z + 0.1 * camZ)),
               (0.5 * fov_val) * ((y + camY) / (z + 0.1 * camZ)))
        t.ht()

    #does what its called

    @staticmethod
    def clear():
        t.clear()
        
#shapes class
class shape:

    #cube
    @staticmethod
    #dont worry about this
    def cube(x=0, y=0, z=0, size=20):
        draw.goto(x + size, y + size, z + 1)
        draw.goto(x - size, y + size, z + 1)
        draw.goto(x - size, y - size, z + 1)
        draw.goto(x + size, y - size, z + 1)
        draw.goto(x + size, y + size, z + 1)
        draw.goto(x + size, y + size, z + 5)
        draw.goto(x - size, y + size, z + 5)
        draw.goto(x - size, y - size, z + 5)
        draw.goto(x + size, y - size, z + 5)
        draw.goto(x + size, y + size, z + 5)
        draw.goto(x + size, y - size, z + 5) 
        draw.goto(x + size, y - size, z + 1)  
        draw.goto(x - size, y - size, z + 1) 
        draw.goto(x - size, y - size, z + 5) 
        draw.goto(x - size, y + size, z + 5)
        draw.goto(x - size, y + size, z + 1)


    #square
    @staticmethod
    def square(size = 20):
        draw.goto(0, 0)
        draw.goto(size, 0)
        draw.goto(size, size)
        draw.goto(0, size)
        draw.goto(0, 0)

    @staticmethod
    def triangle(size = 10):
        draw.goto(0, 0)
        draw.goto(size * 2, 0)
        draw.goto(size, 8.66 * 2)
        draw.goto(0, 0)

#update funtion
def update():
    global camX
    global camY
    global camZ
    while (True):
        #keyboard input
        draw.clear()
        if keyboard.is_pressed('w'):
            camZ -= 1
        if keyboard.is_pressed('s'):
            camZ += 1
        if keyboard.is_pressed('a'):
            camX += 1
        if keyboard.is_pressed('d'):
            camX -= 1

        if keyboard.is_pressed('space'):
            camY -= 1
        if keyboard.is_pressed('shift'):
            camY += 1

        #fixes division by 0 error
        if (camZ < 0.2):
            camZ = 0.2

        shape.cube()
        screen.update()
        time.sleep(0.01)


update()
t.done()
