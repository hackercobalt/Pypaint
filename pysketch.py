import pygame, random, sys

screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

pygame.mouse.set_cursor(pygame.cursors.diamond)

drawMouse, eraseMouse= 0, 0
brushSize, counter = 16, 1

color, colorPath = "Black", "Brushes/pencilBlack.png"
pygame.display.set_caption('pysketch - Brush Size: 16 - Selected Colour: Black')
pygame.display.set_icon(pygame.image.load("icon.png"))
draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
erase = pygame.transform.scale(pygame.image.load("Brushes/eraser.png"), (brushSize, brushSize))

pygame.display.update()

while True:

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 2:

                counter = counter + 1

                if counter == 1:

                    color, colorPath = "Black", "Brushes/pencilBlack.png"
                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

                elif counter == 2:

                    color, colorPath = "Red", "Brushes/pencilRed.png"
                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

                elif counter == 3:

                    color, colorPath = "Green", "Brushes/pencilGreen.png"
                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

                elif counter == 4:

                    color, colorPath = "Blue", "Brushes/pencilBlue.png"
                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

                elif counter == 5:

                    color, colorPath = "Yellow", "Brushes/pencilYellow.png"
                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

                elif counter == 6:

                    color, colorPath = "Orange", "Brushes/pencilOrange.png"
                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

                elif counter == 7:

                    color, colorPath = "Puprle", "Brushes/pencilPurple.png"
                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

                elif counter == 8:
                    counter = 1

                    color, colorPath = "Black", "Brushes/pencilBlack.png"
                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

            if event.button == 4:
                brushSize = brushSize + 2

                draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                erase = pygame.transform.scale(pygame.image.load("Brushes/eraser.png"), (brushSize, brushSize))
                pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

            elif event.button == 5:
                brushSize = brushSize - 2
                if brushSize == 0:
                    brushSize = 2

                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    erase = pygame.transform.scale(pygame.image.load("eraser.png"), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

                else:

                    draw = pygame.transform.scale(pygame.image.load(colorPath), (brushSize, brushSize))
                    erase = pygame.transform.scale(pygame.image.load("eraser.png"), (brushSize, brushSize))
                    pygame.display.set_caption(f'pysketch - Brush Size: {brushSize} - Selected Colour: {color}')

            pygame.display.update()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            screen.fill((255, 255, 255))

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            pygame.image.save(screen, f"image{random.randint(1,999)}.jpg")

        pygame.display.update()

    if pygame.mouse.get_pressed(3)[0]:
        drawMouse = 1
    else:
        drawMouse = 0

    if pygame.mouse.get_pressed(3)[2]:
        eraseMouse = 1
    else:
        eraseMouse = 0

    if drawMouse == 1:
        screen.blit(draw, (x - brushSize / 2, y - brushSize / 2))

    if eraseMouse == 1:
        screen.blit(erase, (x - brushSize / 2, y - brushSize / 2))

    pygame.display.update()
