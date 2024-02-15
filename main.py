import pygame
import pygame.gfxdraw
from data import *
import math

pygame.init()
pygame.display.set_caption("Skydiving Simulation Using Differential Equations")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))


def draw_line(screen, angle):
    start_pos = (100, 800)
    end_pos = (700, round(800 - (600 * math.tan(angle))))
    pygame.draw.aaline(screen, (255, 0, 0), start_pos, end_pos)


def update_display(screen, skydiver_height=1000, camera_angle=0):
    screen.fill((0, 0, 0))
    pygame.draw.aaline(screen, (255, 255, 255), (700, 800), (700, 200))
    pygame.draw.aaline(screen, (255, 255, 255), (100, 800), (700, 800))
    pygame.gfxdraw.filled_circle(screen, 700, round(800-(600*skydiver_height/1000)), 7, (0, 0, 255))
    pygame.gfxdraw.aacircle(screen, 700, round(800-(600*skydiver_height/1000)), 7, (0, 0, 255))
    draw_line(screen, camera_angle)
    pygame.gfxdraw.filled_circle(screen, 100, 800, 7, (255, 0, 0))
    pygame.gfxdraw.aacircle(screen, 100, 800, 7, (255, 0, 0))

    pygame.display.flip()


def run_simulation(screen, heights, camera_angles):
    for i in range(len(heights)):
        clock.tick(90)
        update_display(screen, float(heights[i]), float(camera_angles[i]))


running = True
update_display(screen)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                run_simulation(screen, heights, camera_angles)
            if event.key == pygame.K_q:
                running = False

    #update_display(screen)

pygame.quit()
