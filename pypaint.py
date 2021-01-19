import pygame, random, sys

BLACK, WHITE, RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255)

screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)

drawing, erasing= 0, 0
brushSize, colorCounter, modeCounter = 8, 1, 1

brushMode, brushName = pygame.draw.circle, "Circle"
colorName, colorCode = "Black", BLACK

pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.mouse.set_cursor(pygame.cursors.diamond)

while True:

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 4:
                brushSize = brushSize + 2

            elif event.button == 5:
                brushSize = brushSize - 2

                if brushSize == 0:
                    brushSize = 2

                else:
                    pass

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            screen.fill(WHITE)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            pygame.image.save(screen, f"image{random.randint(1,999)}.jpg")

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            screen.fill(colorCode)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:

            modeCounter = modeCounter + 1

            if modeCounter == 1:
                brushMode, brushName = pygame.draw.circle, "Circle"

            elif modeCounter == 2:
                brushMode, brushName = pygame.draw.rect, "Square"

            elif modeCounter == 3:
                modeCounter = 1
                brushMode, brushName = pygame.draw.circle, "Circle"

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            colorCounter = colorCounter + 1

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            colorCounter = colorCounter - 1

            if colorCounter == 0:
                colorCounter = 8

        if colorCounter == 1:
            colorName, colorCode = "Black", BLACK

        elif colorCounter == 2:
            colorName, colorCode = "Red", RED

        elif colorCounter == 3:
            colorName, colorCode = "Orange", ORANGE

        elif colorCounter == 4:
            colorName, colorCode = "Yellow", YELLOW

        elif colorCounter == 5:
            colorName, colorCode = "Green", GREEN

        elif colorCounter == 6:
            colorName, colorCode = "Cyan", CYAN

        elif colorCounter == 7:
            colorName, colorCode = "Blue", BLUE

        elif colorCounter == 8:
            colorName, colorCode = "Purple", PURPLE

        elif colorCounter == 9:
            colorCounter = 1
            colorName, colorCode = "Black", BLACK

    if pygame.mouse.get_pressed(3)[0]:
        drawing = 1
    else:
        drawing = 0

    if pygame.mouse.get_pressed(3)[2]:
        erasing = 1
    else:
        erasing = 0

    if drawing == 1:
        if brushMode == pygame.draw.circle:
            brushMode(screen, colorCode, (x,y), brushSize)
        elif brushMode == pygame.draw.rect:
            brushMode(screen, colorCode, (pygame.Rect(x - brushSize / 2, y - brushSize / 2, brushSize, brushSize)))

    if erasing == 1:
        if brushMode == pygame.draw.circle:
            brushMode(screen, WHITE, (x,y), brushSize)
        elif brushMode == pygame.draw.rect:
            brushMode(screen, WHITE, (pygame.Rect(x - brushSize / 2, y - brushSize / 2, brushSize, brushSize)))

    pygame.display.set_caption(f'pypaint - Brush Size: {brushSize} - Brush Color: {colorName} - Brush Shape: {brushName}')
    pygame.display.update()
