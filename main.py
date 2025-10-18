import pygame
import sys
import time
from flower import Flower
from population import Population

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flower Evolution")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
button_rect = pygame.Rect(300, 500, 200, 50)
button_color = (0, 180, 0)

population = Population(size=8)
flower_positions = []
spacing = WIDTH // (len(population.flowers) + 1)

def draw_flowers():
    flower_positions.clear()
    for i, f in enumerate(population.flowers):
        x = spacing * (i + 1)
        y = HEIGHT // 2
        pygame.draw.circle(screen, f.genes["center_color"], (x, y), f.genes["center_size"])
        flower_positions.append((x, y, f))

def draw_button():
    pygame.draw.rect(screen, button_color, button_rect)
    text = font.render("Evolve New Generation", True, (255, 255, 255))
    screen.blit(text, (button_rect.x + 10, button_rect.y + 15))

def main():
    running = True
    last_hover = {f: 0 for f in population.flowers}

    while running:
        screen.fill((30, 30, 30))
        draw_flowers()
        draw_button()
        mouse_pos = pygame.mouse.get_pos()

        # update fitness based on hover time
        for (x, y, f) in flower_positions:
            dist = ((mouse_pos[0]-x)**2 + (mouse_pos[1]-y)**2)**0.5
            if dist <= f.genes["center_size"]:
                f.fitness += 0.1  # increase fitness while hovered

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("\n--- Evolving New Generation ---")
                    population.evolve_population()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
