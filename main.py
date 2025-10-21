import pygame
import sys
import math
from flower import Flower
from population import Population

pygame.init()
WIDTH, HEIGHT = 1300, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flower Evolution")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
button_rect = pygame.Rect(300, 520, 200, 50)
button_color = (0, 180, 0)

population = Population(size=8)
flower_positions = []
spacing = WIDTH // (len(population.flowers) + 1)

def draw_flower(x, y, f):
    """Draw full flower: stem, petals, and center."""
    g = f.genes

    # Draw stem
    stem_height = 100
    pygame.draw.rect(
        screen,
        g["stem_color"],
        (x - 5, y, 10, stem_height)
    )

    # Draw petals
    petal_count = g["num_petals"]
    petal_color = g["petal_color"]
    petal_radius = g["center_size"] // 2
    petal_distance = g["center_size"] * 1.5

    if petal_count > 0:
        for i in range(petal_count):
            angle = (2 * math.pi / petal_count) * i
            px = x + math.cos(angle) * petal_distance
            py = y + math.sin(angle) * petal_distance
            pygame.draw.circle(screen, petal_color, (int(px), int(py)), petal_radius)

    # Draw center
    pygame.draw.circle(screen, g["center_color"], (x, y), g["center_size"])

def draw_flowers():
    flower_positions.clear()

    # Find maximum possible horizontal width of a flower (center + petals)
    max_flower_width = max(
        f.genes["center_size"] * 2 for f in population.flowers
    )

    # Add padding between flowers
    spacing = max_flower_width + 62
    total_width = spacing * len(population.flowers)
    start_x = (WIDTH - total_width) // 2 + spacing // 2

    for i, f in enumerate(population.flowers):
        x = start_x + i * spacing
        y = HEIGHT // 2
        draw_flower(x, y, f)
        flower_positions.append((x, y, f))


# Centered button dimensions
button_width, button_height = 300, 60
button_rect = pygame.Rect(0, 0, button_width, button_height)
button_rect.center = (WIDTH // 2, HEIGHT - 80)  # horizontally centered, near bottom


def draw_button():
    base_color = (0, 150, 0)
    hover_color = (0, 200, 0)
    mouse_pos = pygame.mouse.get_pos()

    # Highlight on hover
    color = hover_color if button_rect.collidepoint(mouse_pos) else base_color

    # Draw centered button
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    # Render text and ensure it's centered fully inside the box
    text = font.render("Evolve New Generation", True, (255, 255, 255))
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)



def main():
    running = True
    generation = 0  # start from generation 0

    while running:
        screen.fill((30, 30, 30))
        draw_flowers()
        draw_button()

        # Draw generation text in bottom-left
        generation_text = font.render(f"Generation: {generation}", True, (255, 255, 255))
        screen.blit(generation_text, (20, HEIGHT - 40))  # 20 px from left, near bottom

        mouse_pos = pygame.mouse.get_pos()

        # Update fitness based on hover time
        for (x, y, f) in flower_positions:
            dist = ((mouse_pos[0] - x)**2 + (mouse_pos[1] - y)**2)**0.5
            if dist <= f.genes["center_size"]:
                f.fitness += 0.1
                print(f"Flower hovered: {f}, fitness increased to {f.fitness:.2f}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("\n--- Evolving New Generation ---")
                    population.evolve_population()
                    generation += 1  # increment generation number

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
