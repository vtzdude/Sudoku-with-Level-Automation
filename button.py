import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, bg, (x, y, w , h))
    print(screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y)) 

def start(s):
    print(s)
    return s

def menu(s):
    """ This is the menu that waits you to click the s key to start """
    # b0 contains the rect coordinates of the button
    b0 = button(screen, (10, 10), "Here comes the buttons", 55, "red on yellow")
    b1 = button(screen, (400, 100), "Quit me", 50, "red on yellow")
    b2 = button(screen, (100, 100), "Easy", 50, "white on green")
    b3 = button(screen, (100, 200), "Medium", 50, "white on yellow")
    b4 = button(screen, (100, 300), "Hard", 50, "white on Red")
    if(s!=""):
        b5 = button(screen, (100, 500), s, 50, "white on Blue")
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                print(event.key)    
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check when you click if the coordinates of the pointer are in the rectangle of the buttons
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    return -1
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    return "Easy"
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    return "Medium"
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    return "Hard"
                elif b5.collidepoint(pygame.mouse.get_pos()):
                    return s  
        pygame.display.update()
    pygame.quit()
