import pygame
from random import randint
from sys import exit
from time import sleep
pygame.init()
pygame.display.set_icon(pygame.transform.rotate(pygame.image.load("cup.png"), 180))
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("The Cup Game")
font = pygame.font.Font("freesansbold.ttf", 15)
def score_func():
    score_text = font.render("Score: " + str(score),True, (255,255,255))
    screen.blit(score_text, (5, 5))
state = "Cups Up"
speed = 10
range = 19
ball_list1 = []
ball_list2 = []
ball_list3 = []
ball_list4 = []
ball_list5 = []
ball_list6 = []
ball_list7 = []
ball_list8 = []
button = pygame.image.load("play.png")
button1 = pygame.image.load("restart.png")
class cup:
    def __init__(self, x, y, sector):
        self.x = x
        self.y = y
        self.count = 0
        self.sector = sector
    def cup_spawner(self):
        screen.blit(pygame.transform.rotate(pygame.image.load("cup.png"), 180), (self.x, self.y))
    def move_one(self):
        self.count += 1
        if self.count <= range:
            self.x += speed
            if self.sector == 1:
                self.sector = 2
            elif self.sector == 2:
                self.sector = 3
    def move_one_back(self):
        self.count += 1
        if self.count <= range:
            self.x -= speed
            if self.sector == 3:
                self.sector = 2
            elif self.sector == 2:
                self.sector = 1
    def move_two(self):
        self.count += 1
        if self.count <= range:
            self.x += speed * 2
            if self.sector == 1:
                self.sector = 2
            elif self.sector == 2:
                self.sector = 3
    def move_two_back(self):
        self.count += 1
        if self.count <= range:
            self.x -= speed * 2
            if self.sector == 3:
                self.sector = 2
            elif self.sector == 2:
                self.sector = 1
class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.prev_num = 1
        self.cur_num = 1
    def ball_spawner(self):
        screen.blit(pygame.image.load("round.png"), (self.x, self.y))
    def ball_random(self):
        random_num = randint(1,3)
        if self.prev_num == 1:
            if random_num == 2:
                self.cur_num = random_num
                return cup1.move_one , cup2.move_one_back 
            elif random_num == 3:
                self.cur_num = random_num
                return cup1.move_two , cup3.move_two_back 
            elif random_num == 1:
                self.cur_num = 3
                return cup1.move_two , cup3.move_two_back 
        elif self.prev_num == 2:
            if random_num == 1:
                self.cur_num = random_num
                return cup1.move_one , cup2.move_one_back 
            elif random_num == 3:
                self.cur_num = random_num
                return cup2.move_one , cup3.move_one_back 
            elif random_num == 2:
                self.cur_num = 1
                return cup2.move_one_back , cup1.move_one 
        elif self.prev_num == 3:
            if random_num == 1:
                self.cur_num = random_num
                return cup3.move_two_back , cup1.move_two 
            elif random_num == 3:
                self.cur_num = 1
                return cup1.move_two , cup3.move_two_back 
            elif random_num == 2:
                self.cur_num = random_num
                return cup3.move_one_back , cup2.move_one 
        

cup1 = cup(50,50,1)
cup2 = cup(240,50,2)
cup3 = cup(430,50,3)
ball1 = ball(85,190)
counter = 0
game = False
path1, path2 = ball1.ball_random()
game_result = "None"
click = None
score = 0
while True:
    start = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 290 and pygame.mouse.get_pos()[0] <= 340 and pygame.mouse.get_pos()[1] >= 266 and pygame.mouse.get_pos()[1] <= 313:
                end = pygame.time.get_ticks()
                if game == False:
                    game = True
                    game_result = "None"
            if state == "Cups Up":
                if pygame.mouse.get_pos()[0] >= 74 and pygame.mouse.get_pos()[0] <= 152 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 200:
                    if game == True:
                        game = False
                        click = 1
                        game_result = "Finished"
                elif pygame.mouse.get_pos()[0] >= 264 and pygame.mouse.get_pos()[0] <= 342 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 200:
                    if game == True:
                        game = False
                        click = 2
                        game_result = "Finished"
                elif pygame.mouse.get_pos()[0] >= 454 and pygame.mouse.get_pos()[0] <= 532 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 200:
                    if game == True:
                        game = False
                        click = 3
                        game_result = "Finished"




    screen.fill(color = "aqua")
    ball1.ball_spawner()
    cup1.cup_spawner()
    cup2.cup_spawner()
    cup3.cup_spawner()
    score_func()
    if game == True:
        screen.blit(button1, (270, 260))
        if start - end > 1000 and start - end < 1300:
            state = "1"
        elif start - end > 1300 and start - end < 1600:
            state = "Reset1"
        elif start - end > 1600 and start - end < 1900:
            state = "2"
        elif start - end > 1900 and start - end < 2200:
            state = "Reset2"
        elif start - end > 2200 and start - end < 2500:
            state = "3"
        elif start - end > 2500 and start - end < 2800:
            state = "Reset3"
        elif start - end > 2800 and start - end < 3100:
            state = "4"
        elif start - end > 3100 and start - end < 3400:
            state = "Reset4"
        elif start - end > 3400 and start - end < 3700:
            state = "5"
        elif start - end > 3700 and start - end < 4000:
            state = "Reset5"
        elif start - end > 4000 and start - end < 4300:
            state = "6"
        elif start - end > 4300 and start - end < 4600:
            state = "Reset6"
        elif start - end > 4600 and start - end < 4900:
            state = "7"
        elif start - end > 4900 and start - end < 5200:
            state = "Reset7"
        elif start - end > 5200 and start - end < 5500:
            state = "8"
        elif start - end > 5500 and start - end < 5800:
            state = "Reset8"
        elif start - end > 5800:
            state = "9"
    elif game == False:
        screen.blit(button, (280, 260))




    if state == "1":
        path1()
        path2()
    elif state == "Reset1":
        cup1 = cup(50, 90,1)
        cup2 = cup(240, 90,2)
        cup3 = cup(430, 90,3)
        ball_list1.append(ball1.cur_num)
        ball1.prev_num = ball_list1[0]
        path3, path4 = ball1.ball_random()
    elif state == "2":
        path3()
        path4()
    elif state == "Reset2":
        cup1 = cup(50, 90,1)
        cup2 = cup(240, 90,2)
        cup3 = cup(430, 90,3)
        ball_list2.append(ball1.cur_num)
        ball1.prev_num = ball_list2[0]
        path5, path6 = ball1.ball_random()
    elif state == "3":
        path5()
        path6()
    elif state == "Reset3":
        cup1 = cup(50, 90,1)
        cup2 = cup(240, 90,2)
        cup3 = cup(430, 90,3)
        ball_list3.append(ball1.cur_num)
        ball1.prev_num = ball_list3[0]
        path7, path8 = ball1.ball_random()
    elif state == "4":
        path7()
        path8()
    elif state == "Reset4":
        cup1 = cup(50, 90,1)
        cup2 = cup(240, 90,2)
        cup3 = cup(430, 90,3)
        ball_list4.append(ball1.cur_num)
        ball1.prev_num = ball_list4[0]
        path9, path10 = ball1.ball_random()
    elif state == "5":
        path9()
        path10()
    elif state == "Reset5":
        cup1 = cup(50, 90,1)
        cup2 = cup(240, 90,2)
        cup3 = cup(430, 90,3)
        ball_list5.append(ball1.cur_num)
        ball1.prev_num = ball_list5[0]
        path11, path12 = ball1.ball_random()
    elif state == "6":
        path11()
        path12()
    elif state == "Reset6":
        cup1 = cup(50, 90,1)
        cup2 = cup(240, 90,2)
        cup3 = cup(430, 90,3)
        ball_list6.append(ball1.cur_num)
        ball1.prev_num = ball_list6[0]
        path13, path14 = ball1.ball_random()
    elif state == "7":
        path13()
        path14()
    elif state == "Reset7":
        cup1 = cup(50, 90,1)
        cup2 = cup(240, 90,2)
        cup3 = cup(430, 90,3)
        ball_list7.append(ball1.cur_num)
        ball1.prev_num = ball_list7[0]
        path15, path16 = ball1.ball_random()
    elif state == "8":
        path15()
        path16()
    elif state == "Reset8":
        cup1 = cup(50, 90,1)
        cup2 = cup(240, 90,2)
        cup3 = cup(430, 90,3)
        ball_list8.append(ball1.cur_num)
        ball1.prev_num = ball_list8[0]
        path17, path18 = ball1.ball_random()
    elif state == "9":
        path17()
        path18()
        state = "Cups Up"
        ball_list1 = []
        ball_list2 = []
        ball_list3 = []
        ball_list4 = []
        ball_list5 = []
        ball_list6 = []
        ball_list7 = []
        ball_list8 = []
    elif state == "finished":
        game_result = "Finished"
    if game == True:
        cup1.y = 90
        cup2.y = 90
        cup3.y = 90
        ball1.y = 900
    elif game == False:
        cup1.y = 50
        cup2.y = 50
        cup3.y = 50
        ball1.y = 190
    if game_result == "Finished":
        cup1.y = 50
        cup2.y = 50
        cup3.y = 50
        ball1.y = 190
        if ball1.cur_num == 1:
            ball1.x = 85
            if click == 1:
                score += 1
                click = None
        elif ball1.cur_num == 2:
            ball1.x = 275
            if click == 2:
                score += 1
                click = None
        elif ball1.cur_num ==3:
            ball1.x = 465
            if click == 3:
                score += 1
                click = None
    pygame.display.update()
    pygame.time.Clock().tick(190)