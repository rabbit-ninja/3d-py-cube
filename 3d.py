# Import required libraries
import sys

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

# Define vertices for a cube
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Define edges connecting the vertices
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

# Function to draw the cube using defined vertices and edges
def draw_cube():
    # Start drawing lines
    glBegin(GL_LINES)
    # For each edge
    for edge in edges:
        # For each vertex in the edge
        for vertex in edge:
            # Draw a line to the vertex
            glVertex3fv(vertices[vertex])
    # End drawing lines
    glEnd()

# Function to draw a grid
def draw_grid():
    # Start drawing lines
    glBegin(GL_LINES)
    # Set line color to green
    glColor3f(0.0, 1.0, 0.0)
    # Draw lines for x-axis and y-axis
    for i in range(-10, 11):
        glVertex3fv((i, -10, 0))
        glVertex3fv((i, 10, 0))
        glVertex3fv((-10, i, 0))
        glVertex3fv((10, i, 0))
    # End drawing lines
    glEnd()


def main():
    # Initialize pygame library
    pygame.init()
    # Initialize the video system
    pygame.display.init()
    # Set display size to 800x600
    display = (800, 600)
    # Set display mode to double buffer and opengl
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # Set window caption
    pygame.display.set_caption("3D cube example")
    # Load window icon from favicon.ico
    icon = pygame.image.load("favicon.ico")
    # Set window icon
    pygame.display.set_icon(icon)
    # Set perspective for 3D rendering
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    # Translate the object along the z-axis
    glTranslatef(0.0, 0.0, -5)

    running = True
    while running:
        # Get events
        for event in pygame.event.get():
            # If the quit event is triggered
            if event.type == pygame.QUIT:
                # Quit pygame
                running = False
                # POI: if below line is not commented it gives an error "pygame.error: video system not initialized" after closing the main window.
                # pygame.quit()
        # Get the state of all keyboard keys
        keys = pygame.key.get_pressed()
        # Check if key 1 is pressed, rotate the cube along x axis by 1 degree
        if keys[K_1]:
            glRotatef(1, 1, 0, 0)

        # Check if key 2 is pressed, rotate the cube along y axis by 1 degree
        if keys[K_2]:
            glRotatef(1, 0, 1, 0)

        # Check if key 3 is pressed, rotate the cube along z axis by 1 degree
        if keys[K_3]:
            glRotatef(1, 0, 0, 1)

        # Check if key 4 is pressed, rotate the cube along -x axis by 1 degree
        if keys[K_4]:
            glRotatef(-1, 1, 0, 0)

        # Check if key 5 is pressed, rotate the cube along -y axis by 1 degree
        if keys[K_5]:
            glRotatef(-1, 0, 1, 0)

        # Check if key 6 is pressed, rotate the cube along -z axis by 1 degree
        if keys[K_6]:
            glRotatef(-1, 0, 0, 1)

        # Clear the color and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the grid
        draw_grid()

        # Set the color of the cube to red
        glColor3f(1.0, 0.0, 0.0)

        # Draw the cube
        draw_cube()

        # Update the screen with the latest changes
        pygame.display.flip()

        # Wait for 10 milliseconds
        pygame.time.wait(10)

# Run the main function if the script is run as the main program
if __name__ == '__main__':
    main()

