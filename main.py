import pygame
from fractal_region import FractalRegion
from fractal_generator import MandelbrotSetGenerator


def main():
    pygame.init()
    resolution = (200, 200)
    screen = pygame.display.set_mode(resolution)
    mandelbrot_generator = MandelbrotSetGenerator(max_iterations=256)
    mandelbrot_region = FractalRegion(-1 / 2, 0, mandelbrot_generator, 3, 3,
                                      resolution)
    mandelbrot_region.queue_calculate()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed(3)
                if click[0] and not click[2]:
                    mandelbrot_region.zoom(mouse_x, mouse_y, 0.9)
                    mandelbrot_region.queue_calculate()
                elif not click[0] and click[2]:
                    mandelbrot_region.zoom(mouse_x, mouse_y, 1.1)
                    mandelbrot_region.queue_calculate()

        screen.fill((255, 255, 255))
        mandelbrot_region.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
