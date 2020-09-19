import pygame
import sys

img_bg = pygame.image.load("hello/jra.jpg")

bg_y = 0

def main():
    global bg_y

    pygame.init()
    pygame.display.set_caption("シューティングゲームの背景")
    screen = pygame.display.set_mode((648,486))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg_y = (bg_y+8)%486
        screen.blit(img_bg,[0,bg_y-486])
        screen.blit(img_bg,[0,bg_y])

        pygame.display.update()
        clock.tick()
        pygame.time.wait(10)
if __name__ == "__main__":
    main()