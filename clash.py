'''  
#---------(1)--------------make the spaceship-----------------------------#
import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the initial position of the rectangle
rect_x = 0.0

def key_callback(window, key, scancode, action, mods):
    global rect_x
    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        rect_x -= 0.1
    elif key == glfw.KEY_RIGHT and action == glfw.PRESS:
        rect_x += 0.1

def draw_rectangle():
    glBegin(GL_QUADS)
    glVertex2f(rect_x, -0.9)
    glVertex2f(rect_x + 0.2, -0.9)
    glVertex2f(rect_x + 0.2, -1.0)
    glVertex2f(rect_x, -1.0)
    glEnd()

def draw_callback(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw the rectangle
    glColor3f(1.0, 0.0, 0.0)  # Red color
    draw_rectangle()

    glfw.swap_buffers(window)

def main():
    # Initialize the GLFW library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "Move Rectangle with Arrow Keys", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the callback functions
    glfw.set_key_callback(window, key_callback)
    glfw.set_window_size_callback(window, draw_callback)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Render here
        draw_callback(window)

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()

'''         
###################################################################################################################################################

#-------------(2)-------------make the aliens (stand still)   ----------------------------#
'''
import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Define the initial position of the rectangle
rect_x = 0.0

def key_callback(window, key, scancode, action, mods):
    global rect_x
    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        rect_x -= 0.1
    elif key == glfw.KEY_RIGHT and action == glfw.PRESS:
        rect_x += 0.1

def draw_rectangle():
    glBegin(GL_QUADS)
    glVertex2f(rect_x, -0.9)
    glVertex2f(rect_x + 0.2, -0.9)
    glVertex2f(rect_x + 0.2, -1.0)
    glVertex2f(rect_x, -1.0)
    glEnd()

def draw_circles():
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    radius = 0.05  # Radius of the circle
    gap = 0.1  # Gap between circles
    num_circles = 7  # Number of circles
    center_y = 0.9  # Y coordinate of the circles

    # Calculate the positions of circles
    start_x = -0.8  # Starting x position of the first circle
    for _ in range(num_circles):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(start_x, center_y)
        for angle in range(0, 361, 10):
            x = start_x + math.sin(math.radians(angle)) * radius
            y = center_y + math.cos(math.radians(angle)) * radius
            glVertex2f(x, y)
        glEnd()
        start_x += radius * 2 + gap

def draw_callback(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw the rectangle
    glColor3f(1.0, 0.0, 0.0)  # Red color
    draw_rectangle()

    # Draw the circles
    draw_circles()

    glfw.swap_buffers(window)

def main():
    # Initialize the GLFW library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "Move Rectangle with Arrow Keys", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the callback functions
    glfw.set_key_callback(window, key_callback)
    glfw.set_window_size_callback(window, draw_callback)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Render here
        draw_callback(window)

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()

'''
##########################################################################################################################################

#---------(3)----------------------Make Bullet---------------------------------------------------------------------------

import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Define the initial position of the rectangle
rect_x = 0.0

# Define bullet parameters
bullet_x = 0.0
bullet_y = 0.0
bullet_speed = 0.1
bullet_active = False

# Define circle parameters
circle_centers = []

def key_callback(window, key, scancode, action, mods):
    global rect_x, bullet_active, bullet_x, bullet_y
    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        rect_x -= 0.1
    elif key == glfw.KEY_RIGHT and action == glfw.PRESS:
        rect_x += 0.1
    elif key == glfw.KEY_SPACE and action == glfw.PRESS:
        if not bullet_active:
            bullet_active = True
            bullet_x = rect_x + 0.1  # Set bullet starting position
            bullet_y = -0.8  # Set bullet starting y position

def draw_rectangle():
    glBegin(GL_QUADS)
    glVertex2f(rect_x, -0.9)
    glVertex2f(rect_x + 0.2, -0.9)
    glVertex2f(rect_x + 0.2, -1.0)
    glVertex2f(rect_x, -1.0)
    glEnd()

def draw_circles():
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    radius = 0.05  # Radius of the circle
    gap = 0.1  # Gap between circles
    num_circles = 7  # Number of circles
    center_y = 0.9  # Y coordinate of the circles

    # Calculate the positions of circles
    start_x = -0.8  # Starting x position of the first circle
    for _ in range(num_circles):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(start_x, center_y)
        for angle in range(0, 361, 10):
            x = start_x + math.sin(math.radians(angle)) * radius
            y = center_y + math.cos(math.radians(angle)) * radius
            glVertex2f(x, y)
        glEnd()
        circle_centers.append((start_x + radius, center_y))  # Store circle centers
        start_x += radius * 2 + gap

def draw_bullet():
    if bullet_active:
        glColor3f(1.0, 1.0, 1.0)  # White color
        glBegin(GL_LINES)
        glVertex2f(bullet_x, bullet_y)
        glVertex2f(bullet_x, bullet_y + 0.05)  # Draw bullet as a line of 5 pixels
        glEnd()

def check_collision():
    global bullet_active
    if bullet_active:
        for center in circle_centers:
            dist = math.sqrt((bullet_x - center[0]) ** 2 + (bullet_y - center[1]) ** 2)
            if dist < 0.05:  # Radius of circle is 0.05
                circle_centers.remove(center)  # Remove the hit circle
                bullet_active = False  # Deactivate bullet
                break

def update_bullet():
    global bullet_y, bullet_active
    if bullet_active:
        bullet_y += bullet_speed
        if bullet_y > 1.0:  # If bullet goes beyond the top boundary, deactivate it
            bullet_active = False

def draw_callback(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw the rectangle
    glColor3f(1.0, 0.0, 0.0)  # Red color
    draw_rectangle()

    # Draw the circles
    draw_circles()

    # Draw the bullet
    draw_bullet()

    # Check for collision between bullet and circles
    check_collision()

    # Update bullet position
    update_bullet()

    glfw.swap_buffers(window)

def main():
    # Initialize the GLFW library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "Move Rectangle with Arrow Keys", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the callback functions
    glfw.set_key_callback(window, key_callback)
    glfw.set_window_size_callback(window, draw_callback)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Render here
        draw_callback(window)

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()

