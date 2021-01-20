import pygame, random, sys

BLACK, BLUE, LIGHTBLUE, BROWN, GRAY, GREEN, ORANGE, PINK, PURPLE, RED, WHITE, YELLOW = (0,0,0),(0,0,255),(173,216,230),(150,75,0),(128,128,128),(0,255,0),(255,165,0),(255,192,203),(160,32,240),(255,0,0),(255,255,255),(255,255,0)

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
                brushMode, brushName = pygame.draw.polygon, "Triangle"

            elif modeCounter == 4:
                modeCounter = 1
                brushMode, brushName = pygame.draw.circle, "Circle"

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            colorCounter = colorCounter + 1

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            colorCounter = colorCounter - 1

            if colorCounter == 0:
                colorCounter = 8

        if colorCounter == 1:
            colorName, colorCode = "Black", BLACK

        elif colorCounter == 2:
            colorName, colorCode = "Gray", GRAY

        elif colorCounter == 3:
            colorName, colorCode = "Red", RED

        elif colorCounter == 4:
            colorName, colorCode = "Brown", BROWN

        elif colorCounter == 5:
            colorName, colorCode = "Orange", ORANGE

        elif colorCounter == 6:
            colorName, colorCode = "Yellow", YELLOW

        elif colorCounter == 7:
            colorName, colorCode = "Green", GREEN

        elif colorCounter == 8:
            colorName, colorCode = "Light Blue", LIGHTBLUE

        elif colorCounter == 9:
            colorName, colorCode = "Blue", BLUE

        elif colorCounter == 10:
            colorName, colorCode = "Pink", PINK

        elif colorCounter == 11:
            colorName, colorCode = "Purple", PURPLE

        elif colorCounter == 12:
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
        elif brushMode == pygame.draw.polygon:
            brushMode(screen, colorCode, ((x, y - brushSize),(x - brushSize, y + brushSize),(x + brushSize, y + brushSize)))

    if erasing == 1:
        if brushMode == pygame.draw.circle:
            brushMode(screen, WHITE, (x,y), brushSize)
        elif brushMode == pygame.draw.rect:
            brushMode(screen, WHITE, (pygame.Rect(x - brushSize / 2, y - brushSize / 2, brushSize, brushSize)))
        elif brushMode == pygame.draw.polygon:
            brushMode(screen, WHITE, ((x, y - brushSize),(x - brushSize, y + brushSize),(x + brushSize, y + brushSize)))

    pygame.display.set_caption(f'pypaint - Brush Size: {brushSize} - Brush Color: {colorName} - Brush Shape: {brushName}')
    pygame.display.update()
