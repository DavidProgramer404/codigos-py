import pygame
import sys

def main():
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pac-Man")

    pacman_image = pygame.image.load("pacman.png")
    pacman_rect = pacman_image.get_rect()
    pacman_rect.center = (screen_width // 2, screen_height // 2)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Lógica del juego aquí (movimiento, colisiones, etc.)

        # Dibuja el fondo y el personaje Pac-Man
        screen.fill((0, 0, 0))  # Fondo negro
        screen.blit(pacman_image, pacman_rect)

        pygame.display.flip()
        clock.tick(60)  # Limita la velocidad de fotogramas a 60 FPS

if __name__ == "__main__":
    main()
