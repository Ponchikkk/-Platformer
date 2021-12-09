import pygame

def main():
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    running = True
    color_start = (0, 255, 0)
    color_exit = (255, 0, 0)
    btn_start = pygame.Rect(350, 200, 100, 50)
    btn_exit = pygame.Rect(350, 260, 100, 50)
    while running:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color_start, btn_start)
        pygame.draw.rect(screen, color_exit, btn_exit)
        font = pygame.font.Font(None, 50)
        text = font.render("Welcome!", True, (100, 255, 100))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 4 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.collidepoint(event.pos):
                    color_start = (0, 155, 0)
                elif btn_exit.collidepoint(event.pos):
                    color_exit = (155, 0, 0)
            if event.type == pygame.MOUSEBUTTONUP:
                if btn_start.collidepoint(event.pos):
                    color_start = (0, 255, 0)
                elif btn_exit.collidepoint(event.pos):
                    color_exit = (255, 0, 0)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
