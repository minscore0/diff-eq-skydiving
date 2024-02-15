import pygame
import pygame.gfxdraw
from data import *
import math

pygame.init()
pygame.display.set_caption("Skydiving Simulation Using Differential Equations")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
font1 = pygame.font.Font("freesansbold.ttf", 15)
font2 = pygame.font.Font("freesansbold.ttf", 20)


def draw_line(screen, angle):
    start_pos = (100, 800)
    end_pos = (700, round(800 - (600 * math.tan(angle))))
    pygame.draw.aaline(screen, (255, 0, 0), start_pos, end_pos)


def update_display(screen, skydiver_height=1000, camera_angle=0, i=0):
    pygame.gfxdraw.filled_polygon(screen, [(0, 0), (0, 900), (800, 900), (800, 0)], (0, 0, 0))
    text0 = font2.render("Simulation with person (blue) and camera (red)", True, (255, 255, 255))
    rect0 = text0.get_rect()
    rect0.center = (400, 150)
    screen.blit(text0, rect0)
    text_3 = font2.render("time (s)", True, (255, 255, 255))
    rect_3 = text_3.get_rect()
    rect_3.center = (400, 850)
    screen.blit(text_3, rect_3)
    text_1 = font1.render("1000", True, (255, 255, 255))
    rect_1 = text_1.get_rect()
    rect_1.center = (730, 205)
    screen.blit(text_1, rect_1)
    text_2 = font1.render("0", True, (255, 255, 255))
    rect_2 = text_2.get_rect()
    rect_2.center = (715, 802)
    screen.blit(text_2, rect_2)
    pygame.draw.aaline(screen, (255, 255, 255), (700, 800), (700, 200))
    pygame.draw.aaline(screen, (255, 255, 255), (100, 800), (700, 800))
    for j in range(1, i):
        pygame.draw.aaline(screen, (0, 0, 255), (round(700 - 600*(i-j)/len(heights)), round(800 - 600*float(heights[j-1])/1000)), (round(700 - 600*(i-j)/len(heights)), round(800 - 600*float(heights[j])/1000)))
        if (j-1)%149 == 0:
            text_n = font1.render(str((j//149)*15), True, (255, 255, 255))
            rect_n = text_n.get_rect()
            rect_n.center = (round(700 - 600*(i-j)/len(heights)), 820)
            screen.blit(text_n, rect_n)

    draw_line(screen, camera_angle)
    pygame.gfxdraw.filled_circle(screen, 700, round(800-(600*skydiver_height/1000)), 7, (0, 0, 255))
    pygame.gfxdraw.aacircle(screen, 700, round(800-(600*skydiver_height/1000)), 7, (0, 0, 255))
    pygame.gfxdraw.filled_circle(screen, 100, 800, 7, (255, 0, 0))
    pygame.gfxdraw.aacircle(screen, 100, 800, 7, (255, 0, 0))

    text1 = font1.render("0.00", True, (255, 255, 255))
    rect1 = text1.get_rect()
    rect1.center = (870, 105)
    screen.fill((0, 0, 0), rect1)
    screen.blit(text1, rect1)
    text2 = font2.render("Camera rotation rate (radians/s)", True, (255, 255, 255))
    rect2 = text2.get_rect()
    rect2.center = (1200, 80)
    screen.fill((0, 0, 0), rect2)
    screen.blit(text2, rect2)
    text3 = font1.render("0", True, (255, 255, 255))
    rect3 = text3.get_rect()
    rect3.center = (880, 105)
    screen.fill((0, 0, 0), rect3)
    screen.blit(text3, rect3)
    text4 = font1.render("-0.025", True, (255, 255, 255))
    rect4 = text4.get_rect()
    rect4.center = (865, 400)
    screen.fill((0, 0, 0), rect4)
    screen.blit(text4, rect4)
    pygame.draw.aaline(screen, (255, 255, 255), (900, 100), (900, 400))
    pygame.draw.aaline(screen, (255, 255, 255), (900, 100), (1500, 100))

    text5 = font2.render("Velocity (meters/s)", True, (255, 255, 255))
    rect5 = text5.get_rect()
    rect5.center = (1200, 480)
    screen.fill((0, 0, 0), rect5)
    screen.blit(text5, rect5)
    text6 = font1.render("0", True, (255, 255, 255))
    rect6 = text6.get_rect()
    rect6.center = (880, 505)
    screen.fill((0, 0, 0), rect6)
    screen.blit(text6, rect6)
    text7 = font1.render("-50", True, (255, 255, 255))
    rect7 = text7.get_rect()
    rect7.center = (880, 805)
    screen.fill((0, 0, 0), rect7)
    screen.blit(text7, rect7)
    pygame.draw.aaline(screen, (255, 255, 255), (900, 500), (900, 800))
    pygame.draw.aaline(screen, (255, 255, 255), (900, 500), (1500, 500))

    pygame.display.flip()


def run_simulation(screen, heights, camera_angles):
    for i in range(len(heights)):
        clock.tick(60)
        update_display(screen, float(heights[i]), float(camera_angles[i]), i)
        if i == 0:
            continue
        pygame.draw.aaline(screen, (255, 0, 0), (round(900 + 600*(i-1)/len(heights)), round(100 + 300*float(camera_rotation_rate[i-1])/-0.025)), (round(900 + 600*i/len(heights)), round(100 + 300*float(camera_rotation_rate[i])/-0.025)))
        pygame.draw.aaline(screen, (0, 0, 255), (round(900 + 600*(i-1)/len(heights)), round(500 + 300*float(velocity[i-1])/-50)), (round(900 + 600*i/len(heights)), round(500 + 300*float(velocity[i])/-50)))


running = True
update_display(screen)
start_simulation = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_simulation = True
            if event.key == pygame.K_q:
                running = False

    if start_simulation:
        start_simulation = False
        screen.fill((0, 0, 0))
        run_simulation(screen, heights, camera_angles)

pygame.quit()
