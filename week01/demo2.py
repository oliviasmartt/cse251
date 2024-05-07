import math
import threading 
import os
from cse251turtle import *

# Include CSE 251 common Python files. 
from cse251 import *

# No global variables.

def draw_square(tur, x, y, side, color='black'):
    """Draw Square"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    for _ in range(4):
        tur.forward(side)
        tur.right(90)


def draw_circle(tur, x, y, radius, color='red'):
    """Draw Circle"""
    steps = 10
    circumference = 2 * math.pi * radius

    # Need to adjust starting position so that (x, y) is the center
    x1 = x - (circumference // steps) // 2
    y1 = y
    tur.move(x1 , y1 + radius)

    tur.setheading(0)
    tur.color(color)
    for _ in range(steps):
        tur.forward(circumference / steps)
        tur.right(360 / steps)


def draw_rectangle(tur, x, y, width, height, color='blue'):
    """Draw a rectangle"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    tur.forward(width)
    tur.right(90)
    tur.forward(height)
    tur.right(90)
    tur.forward(width)
    tur.right(90)
    tur.forward(height)
    tur.right(90)


def draw_triangle(tur, x, y, side, color='green'):
    """Draw a triangle"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    for _ in range(4):
        tur.forward(side)
        tur.left(120)


def draw_coord_system(tur, x, y, size=300, color='black'):
    """Draw corrdinate lines"""
    tur.move(x, y)
    for i in range(4):
        tur.forward(size)
        tur.backward(size)
        tur.left(90)

def draw_squares(tur, lock):
    """Draw a group of squares"""
    lock.acquire()
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            draw_square(tur, x - 50, y + 50, 100)
    lock.release()


def draw_circles(tur):
    """Draw a group of circles"""
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            draw_circle(tur, x, y-2, 50)


def draw_triangles(tur):
    """Draw a group of triangles"""
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            draw_triangle(tur, x-30, y-30+10, 60)


def draw_rectangles(tur):
    """Draw a group of Rectangles"""
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            draw_rectangle(tur, x-10, y+5, 20, 15)


def draw_square(tur, x, y, side, color='black'):
    """Draw Square"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    for _ in range(4):
        tur.forward(side)
        tur.right(90)

def draw_circle(tur, x, y, radius, color='red'):
    """Draw Circle"""
    steps = 10
    circumference = 2 * math.pi * radius

    # Need to adjust starting position so that (x, y) is the center
    x1 = x - (circumference // steps) // 2
    y1 = y
    tur.move(x1 , y1 + radius)

    tur.setheading(0)
    tur.color(color)
    for _ in range(steps):
        tur.forward(circumference / steps)
        tur.right(360 / steps)

def draw_rectangle(tur, x, y, width, height, color='blue'):
    """Draw a rectangle"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    tur.forward(width)
    tur.right(90)
    tur.forward(height)
    tur.right(90)
    tur.forward(width)
    tur.right(90)
    tur.forward(height)
    tur.right(90)

def draw_triangle(tur, x, y, side, color='green'):
    """Draw a triangle"""
    tur.move(x, y)
    tur.setheading(0)
    tur.color(color)
    for _ in range(3):
        tur.forward(side)
        tur.left(120)

def draw_coord_system(tur, x, y, size=300, color='black'):
    """Draw coordinate lines"""
    tur.move(x, y)
    for _ in range(4):
        tur.forward(size)
        tur.backward(size)
        tur.left(90)

def draw_squares(tur, lock):
    """Draw a group of squares"""
    lock.acquire()
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            draw_square(tur, x - 50, y + 50, 100)
    lock.release()

def draw_circles(tur, lock):
    """Draw a group of circles"""
    lock.acquire()
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            draw_circle(tur, x, y-2, 50)
    lock.release()

def draw_triangles(tur, lock):
    """Draw a group of triangles"""
    lock.acquire()
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            draw_triangle(tur, x-30, y-30+10, 60)
    lock.release()

def draw_rectangles(tur, lock):
    """Draw a group of Rectangles"""
    lock.acquire()
    for x in range(-300, 350, 200):
        for y in range(-300, 350, 200):
            draw_rectangle(tur, x-10, y+5, 20, 15)
    lock.release()

def run_with_threads(tur, log, main_turtle):
    """Draw different shapes using threads"""

    # Draw Coors system
    tur.pensize(0.5)
    draw_coord_system(tur, 0, 0, size=375)
    tur.pensize(4)
    log.write('-' * 50)
    log.start_timer('Start Drawing With Threads')
    tur.move(0, 0)

    # Start add your code here.
    lock = threading.Lock()

    threads = []
    
    # Thread for drawing triangles
    triangle_thread = threading.Thread(target=draw_triangles, args=(tur, lock))
    threads.append(triangle_thread)

    # Thread for drawing circles
    circle_thread = threading.Thread(target=draw_circles, args=(tur, lock))
    threads.append(circle_thread)

    # Thread for drawing squares
    square_thread = threading.Thread(target=draw_squares, args=(tur, lock))
    threads.append(square_thread)

    # Thread for rectangles
    rectangle_thread = threading.Thread(target=draw_rectangles, args=(tur, lock))
    threads.append(rectangle_thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    

    # You need to use 4 threads where each thread concurrently drawing one type of shape.
    # You are free to change any functions in this code except main()

    log.step_timer('All drawing commands have been created')

    log.write(f'Number of Drawing Commands: {tur.get_command_count()}')

    # Play the drawing commands that were created
    tur.play_commands(main_turtle)
    log.stop_timer('Total drawing time')
    tur.clear()

def main():
    """Main function - DO NOT CHANGE"""

    log = Log(show_terminal=True)

    # create a Screen Object
    screen = turtle.Screen()

    # Screen configuration
    screen.setup(800, 800)

    # Make turtle Object
    main_turtle = turtle.Turtle()
    main_turtle.speed(0)

    # Special CSE 251 Turtle Class
    turtle251 = CSE251Turtle()

    # Test 2 - Drawing with threads
    run_with_threads(turtle251, log, main_turtle)

    # Start the event loop
    turtle.mainloop()

if __name__ == "__main__":
    main()


def run_with_threads(tur, log, main_turtle):
    """Draw different shapes using threads"""

    # Draw Coors system
    tur.pensize(0.5)
    draw_coord_system(tur, 0, 0, size=375)
    tur.pensize(4)
    log.write('-' * 50)
    log.start_timer('Start Drawing With Threads')
    tur.move(0, 0)

    # TODO - Start add your code here.
    lock = threading.Lock()

    threads = []
    
    # Thread for drawing triangles
    triangle_thread = threading.Thread(target=draw_triangles, args=(tur,))
    threads.append(triangle_thread)

    # Thread for drawing circles
    circle_thread = threading.Thread(target=draw_circles, args=(tur,))
    threads.append(circle_thread)

    # Thread for drawing squares
    square_thread = threading.Thread(target=draw_squares, args=(tur,))
    threads.append(square_thread)

    # Thread for rectangles
    rectangle_thread = threading.Thread(target=draw_rectangles, args=(tur,))
    threads.append(rectangle_thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    

    # You need to use 4 threads where each thread concurrently drawing one type of shape.
    # You are free to change any functions in this code except main()

    log.step_timer('All drawing commands have been created')

    log.write(f'Number of Drawing Commands: {tur.get_command_count()}')

    # Play the drawing commands that were created
    tur.play_commands(main_turtle)
    log.stop_timer('Total drawing time')
    tur.clear()


def main():
    """Main function - DO NOT CHANGE"""

    log = Log(show_terminal=True)

    # create a Screen Object
    screen = turtle.Screen()

    # Screen configuration
    screen.setup(800, 800)

    # Make turtle Object
    main_turtle = turtle.Turtle()
    main_turtle.speed(0)

    # Special CSE 251 Turtle Class
    turtle251 = CSE251Turtle()

    # Test 1 - Drawing with no threads
    # remove the file 'drawpart1.txt' to stop drawing part 1
    if os.path.exists('drawpart1.txt'):
        run_no_threads(turtle251, log, main_turtle)
    
    main_turtle.clear()

    # Test 2 - Drawing with threads
    run_with_threads(turtle251, log, main_turtle)

    # Waiting for user to close window
    turtle.done()


if __name__ == "__main__":
    main()
