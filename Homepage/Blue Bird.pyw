'''
Blue Bird
'''
import pygame
import time
import random
import sys
import os
from pygame.locals import *

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (450, 200)

pygame.init()


class Window():
    
    def __init__(self):
        self.size = (700, 500)
        self.GUI = pygame.display.set_mode(self.size, 1, 32)
        pygame.display.set_caption('Blue Bird')
        self.bg_image = pygame.image.load('forest_landscape_klein.png')
        self.icon = pygame.image.load('flat-flying-bird-icon.jpg')
        pygame.display.set_icon(self.icon)
        
    def background(self):
        self.GUI.fill((0, 0, 0))
        self.GUI.blit(self.bg_image, (0, 0))
                

class Bird():
    
    def __init__(self, GUI):
        self.pos_x = 80
        self.pos_y = 360
        self.ascend = 25
        self.fall = 5
        self.GUI = GUI
        self.bird_flying = pygame.image.load('Figur_Flügel_unten_klein.png')
        self.bird_sinking = pygame.image.load('Figur_Flügel_oben_klein.png')
        
    def update(self):
        if pygame.event.peek(MOUSEBUTTONDOWN):
            self.pos_y -= self.ascend
            self.GUI.GUI.blit(self.bird_flying, (self.pos_x - 25, self.pos_y - 25))
        else:
            self.pos_y += self.fall
            self.GUI.GUI.blit(self.bird_sinking, (self.pos_x - 25, self.pos_y - 25))
        pygame.event.clear()
        

class Obstacle():
    
    def __init__(self, GUI, x_pos):
        self.GUI = GUI
        self.pos_x = x_pos
        self.narrow_top = random.randrange(200, 350)
        self.narrow_bottom = self.narrow_top + 100
        self.width = 25
        self.color = (139, 69, 19)
        
    def set(self):
        pygame.draw.rect(self.GUI.GUI, self.color,
                         (self.pos_x, 0, self.width, self.narrow_top))
        pygame.draw.rect(self.GUI.GUI, self.color,
                         (self.pos_x, self.narrow_bottom, self.width, 500))
        
    def move(self):
        self.pos_x -= 5


def check_collision(bird, obstacle ):
    if (bird.pos_x + 25 > obstacle.pos_x and
            bird.pos_x - 25 < obstacle.pos_x + obstacle.width and
            (bird.pos_y - 25 < obstacle.narrow_top or
            bird.pos_y + 25 > obstacle.narrow_bottom)):
        return True
    elif bird.pos_y - 25 < 0 or bird.pos_y + 25 >  500:
        return True
    else:
        return False


def game_over(start, end, Interface):
    played_time = int(end - start)
    font1 = pygame.font.SysFont('Arial', 35)
    font2 = pygame.font.SysFont('Arial', 25)
    bg_image = pygame.image.load('laurel-wreath-297040_1280.png')
    Interface.GUI.fill((255, 255, 255))
    Interface.GUI.blit(bg_image, (0, 0))
    text = font1.render('Sie haben {} Sekunden geschaft!'. format(played_time),
                        1, (255,215,0))
    text2 = font2.render('klicken Sie um erneut zu spielen.', 1, (0, 0, 0))
    Interface.GUI.blit(text, (130, 200))
    Interface.GUI.blit(text2, (200, 300))
    pygame.display.update()
    while True:
        if pygame.event.peek(QUIT):
            pygame.quit()
            sys.exit()
        elif pygame.event.peek(MOUSEBUTTONDOWN):
            game()
        time.sleep(0.05)
           

def game():
    global Bird
    GUI = Window()
    bird = Bird(GUI)

    obstacles = []
    positions = {0}
    
    for number in range(1, 151):
        position = set((random.randrange(500, 8000, 200), 0))
        positions = positions ^ position
        
    positions = list(positions)
    positions.pop(0)
    positions.sort()
    
    for position in positions:
        obstacles.append(Obstacle(GUI, position))

    pygame.mixer.init()
    pygame.mixer.music.load('a_brilliant_idea_terrasound.mp3')
    pygame.mixer.music.play(loops = -1, start = 0.0)

    Font_time = pygame.font.SysFont('Arial', 30)

    start_time = time.time()
        
    while True:
        if pygame.event.peek(QUIT):
            pygame.quit()
            sys.exit()
        GUI.background()
        bird.update()
        for obstacle in obstacles:
            obstacle.move()
            if obstacle.pos_x < 700 and obstacle.pos_x > 0:
                obstacle.set()
                if check_collision(bird, obstacle):
                    #print('collision')
                    end_time = time.time()
                    game_over(start_time, end_time, GUI)
        if obstacles[len(obstacles) - 1].pos_x < 0:
            end_time = time.time()
            pygame.quit()
            game_over(start_time, end_time, GUI)

        runned_time = Font_time.render('%d sek' % (time.time() - start_time),
                                       1, (0, 0, 0))
        GUI.GUI.blit(runned_time, (20, 20))
        pygame.display.update()
        time.sleep(0.05)


if __name__ == '__main__':
    game()
