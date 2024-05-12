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

