import pygame, random, sys

screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

pygame.display.set_caption('PySketch - Brush Size: 16')
pygame.display.set_icon(pygame.image.load("icon.png"))

pygame.display.update()
pygame.mouse.set_cursor(pygame.cursors.diamond)

drawMouse, eraseMouse= 0, 0
brushSize = 16

draw = pygame.transform.scale(pygame.image.load("pencil.png"), (brushSize, brushSize))
erase = pygame.transform.scale(pygame.image.load("eraser.png"), (brushSize, brushSize))

pygame.display.update()

while True:

    x, y = pygame.mouse.get_pos()
    pygame.display.set_caption(f'PySketch - Brush Size: {brushSize} {x, y}')

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 4:
                brushSize = brushSize + 2

                draw = pygame.transform.scale(pygame.image.load("pencil.png"), (brushSize, brushSize))
                erase = pygame.transform.scale(pygame.image.load("eraser.png"), (brushSize, brushSize))

                pygame.display.set_caption(f'PySketch - Brush Size: {brushSize}')

            elif event.button == 5:
                brushSize = brushSize - 2
                if brushSize == 0:
                    brushSize = 2

                    draw = pygame.transform.scale(pygame.image.load("pencil.png"), (brushSize, brushSize))
                    erase = pygame.transform.scale(pygame.image.load("eraser.png"), (brushSize, brushSize))

                else:

                    draw = pygame.transform.scale(pygame.image.load("pencil.png"), (brushSize, brushSize))
                    erase = pygame.transform.scale(pygame.image.load("eraser.png"), (brushSize, brushSize))

                pygame.display.set_caption(f'PySketch - Brush Size: {brushSize}')
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
        screen.blit(draw, (x - brushSize / 2  , y - brushSize / 2))

    if eraseMouse == 1:
        screen.blit(erase, (x - brushSize / 2 , y - brushSize / 2))

    pygame.display.update()
