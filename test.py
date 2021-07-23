import pygame as pg
import sys
import random
def draw_floor():
    screen.blit(floor_surface,(floor_x,580))
    screen.blit(floor_surface,(floor_x+screen_width,580))
def create_pipe():
    pipe_height=[400,200,100]
    random_pipe_pos=random.choice(pipe_height)
    bottom_pipe= pipe_surface.get_rect(midtop=(screen_width+10,random_pipe_pos))
    top_pipe= pipe_surface.get_rect(midbottom=(screen_width+10,random_pipe_pos-200))
    return bottom_pipe,top_pipe
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom>screen_height:
            screen.blit(pipe_surface,pipe)
        else:
            screen.blit(pg.transform.flip(pipe_surface, False, True),pipe)
def check_coll(pipes):
    if bird_rect.top<-50 or bird_rect.bottom>580:
        print ('OUT OF BOUND')
        return False
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            print('colide')
            return False
    return True
def rotate_bird(bird):
    return pg.transform.rotozoom(bird,bird_movment,1)
pg.init()
#Game variable
gravity=0.5
bird_movment=0
game_active=True

screen_width=430
screen_height=650
screen=pg.display.set_mode((screen_width,screen_height))
clock=pg.time.Clock()

bg_surface=pg.transform.scale(pg.image.load('assets/sprites/background-day.png').convert(),((screen_width,screen_height)))

floor_surface=pg.transform.scale(pg.image.load('assets/sprites/base.png').convert(),(screen_width,100))
floor_x=0

bird_surface=pg.image.load('assets/sprites/bluebird-midflap.png').convert()
bird_surface=pg.transform.scale(bird_surface,(40,30))
bird_rect=bird_surface.get_rect(center=(100,325))

pipe_surface=pg.image.load('assets/sprites/pipe-green.png').convert()
pipe_surface=pg.transform.scale(pipe_surface,(80,600))
pipe_list=[]
SPAWNPIPE=pg.USEREVENT
pg.time.set_timer(SPAWNPIPE,1800)
while True:
    #image of player1
    #background image
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                bird_movment=0
                bird_movment-=7
            if game_active==False and event.key==pg.K_n:
                game_active=True
                pipe_list=[]
                bird_rect.center=(100,325)
                bird_movment=0

        if event.type==SPAWNPIPE:
            pipe_list.extend(create_pipe())



    screen.blit(bg_surface,(0,0))
    #bird
    if game_active==True:
        rotated_bird=rotate_bird(bird_surface)
        bird_movment+=gravity
        bird_rect.centery+=bird_movment
        screen.blit(rotated_bird,bird_rect)
        #pipes
        pipe_list=move_pipes(pipe_list)
        draw_pipes(pipe_list)
        game_active=check_coll(pipe_list)
    #floor
    floor_x-=1
    draw_floor()
    if floor_x<=-355:
        floor_x=0
    clock.tick(60)



    pg.display.update()