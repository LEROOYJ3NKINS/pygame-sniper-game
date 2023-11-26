import pygame
import sys
from tkinter import messagebox, Tk

def main():
    pygame.init()

    # Set the dimensions of the window
    window_size = (1000, 400)
    screen = pygame.display.set_mode(window_size)

    # Set the title of the window
    pygame.display.set_caption('game window 1')


    # Load the images
    #image1
    image1 = pygame.image.load(r'C:\Users\danie\Desktop\python game\sprites\charecters\mission 1\target.png')
    #image2
    image2 = pygame.image.load(r'C:\Users\danie\Desktop\python game\sprites\charecters\mission 1\blue normal.png')
    #image3
    image3 = pygame.image.load(r'C:\Users\danie\Desktop\python game\sprites\charecters\mission 1\green normal.png')
    #image4
    image4 = pygame.image.load(r'C:\Users\danie\Desktop\python game\sprites\charecters\mission 1\yellow normal.png')
    # Main event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Check if the mouse is over the image
                if 500 <= mouse_x <= 500 + 20 and 200 <= mouse_y <= 200 + 27:
                    # Open a popup window
                    root = Tk()
                    root.withdraw()

        # Fill the screen with a color
        screen.fill((255, 255, 255))

        #Draw the image to the screen at the position (x, y)
        #image1
        screen.blit(image1, (500, 200))
        #image2
        screen.blit(image2, (480, 190))
        #image3
        screen.blit(image3, (419, 210))
        #image4
        screen.blit(image4, (550, 200))

        # Update the display
        pygame.display.flip()

if __name__ == '__main__':
    main()

