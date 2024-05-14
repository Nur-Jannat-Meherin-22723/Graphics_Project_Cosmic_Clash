import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Define the initial position of the rectangle
rect_x = 0.0

# Define bullet parameters
bullet_x = 0.0
bullet_y = 0.0
bullet_speed = 0.1
bullet_active = False

# Define alien bullet parameters
alien_bullets = []

# Define circle (alien) parameters
circle_centers = []
circle_active = []

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
    for i in range(num_circles):
        if circle_active[i]:
            glBegin(GL_TRIANGLE_FAN)
            glVertex2f(start_x, center_y)
            for angle in range(0, 361, 10):
                x = start_x + math.sin(math.radians(angle)) * radius
                y = center_y + math.cos(math.radians(angle)) * radius
                glVertex2f(x, y)
            glEnd()
        start_x += radius * 2 + gap

def draw_bullet():
    if bullet_active:
        glColor3f(1.0, 1.0, 1.0)  # White color
        glBegin(GL_LINES)
        glVertex2f(bullet_x, bullet_y)
        glVertex2f(bullet_x, bullet_y + 0.05)  # Draw bullet as a line of 5 pixels
        glEnd()

def draw_alien_bullets():
    for bullet in alien_bullets:
        glColor3f(1.0, 0.0, 0.0)  # Red color
        glBegin(GL_LINES)
        glVertex2f(bullet[0], bullet[1])
        glVertex2f(bullet[0], bullet[1] - 0.05)  # Draw bullet as a line of 5 pixels
        glEnd()

def check_collision():
    global bullet_active
    if bullet_active:
        for i, center in enumerate(circle_centers):
            if circle_active[i]:
                dist = math.sqrt((bullet_x - center[0]) ** 2 + (bullet_y - center[1]) ** 2)
                if dist < 0.05:  # Radius of circle is 0.05
                    circle_active[i] = False  # Deactivate the hit circle
                    bullet_active = False  # Deactivate bullet
                    break

def check_alien_bullet_collision():
    global rect_x
    for bullet in alien_bullets:
        if bullet[1] <= -0.9:
            if rect_x <= bullet[0] <= rect_x + 0.2:
                print("Ship hit!")
                alien_bullets.remove(bullet)

def update_bullet():
    global bullet_y, bullet_active
    if bullet_active:
        bullet_y += bullet_speed
        if bullet_y > 1.0:  # If bullet goes beyond the top boundary, deactivate it
            bullet_active = False

def update_alien_bullets():
    for bullet in alien_bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < -1.0:  # If bullet goes beyond the bottom boundary, remove it
            alien_bullets.remove(bullet)

def draw_callback(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw the rectangle (ship)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    draw_rectangle()

    # Draw the circles (aliens)
    draw_circles()

    # Draw the ship's bullet
    draw_bullet()

    # Draw the alien bullets
    draw_alien_bullets()

    # Check for collision between bullet and circles
    check_collision()

    # Check for collision between alien bullets and ship
    check_alien_bullet_collision()

    # Update bullet position
    update_bullet()

    # Update alien bullet positions
    update_alien_bullets()

    glfw.swap_buffers(window)

def alien_fire_bullet():
    active_aliens = [center for i, center in enumerate(circle_centers) if circle_active[i]]
    if active_aliens:
        shooter = random.choice(active_aliens)
        alien_bullets.append([shooter[0], shooter[1]])

def main():
    global circle_centers, circle_active
    # Initialize the GLFW library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "2D Space Invaders", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the callback functions
    glfw.set_key_callback(window, key_callback)
    glfw.set_window_size_callback(window, draw_callback)

    # Initialize circle centers and active status
    radius = 0.05  # Radius of the circle
    gap = 0.1  # Gap between circles
    num_circles = 7  # Number of circles
    center_y = 0.9  # Y coordinate of the circles
    start_x = -0.8  # Starting x position of the first circle
    for _ in range(num_circles):
        circle_centers.append((start_x + radius, center_y))
        circle_active.append(True)
        start_x += radius * 2 + gap

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Render here
        draw_callback(window)

        # Randomly fire alien bullets
        if random.random() < 0.01:  # Adjust probability as needed
            alien_fire_bullet()

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
