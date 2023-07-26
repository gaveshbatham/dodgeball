from  threading import *
import pygame 
import time
import random
from tkinter import *




pygame.init()
pygame.mixer.init()


mouse_position = pygame.mouse.get_pos()


player_x=mouse_position[0]
player_y=mouse_position[1]
          
error=7



SCREEN_HIG =600
SCREEN_WIDTH =int(SCREEN_HIG*1.6)
SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIG))

ball_scale=45

player_scale=80

FPS=40

FPSCLOCK=pygame.time.Clock()

score=0

#_____________________________________________________________image -load-start

background_img='file\\img\\background_1.jpg'

ball_1_img=pygame.image.load('file\\img\\ball_1.png')
ball_1_img=pygame.transform.scale(ball_1_img,(ball_scale,ball_scale))

ball_2_img=pygame.image.load('file\\img\\ball_2.png')
ball_2_img=pygame.transform.scale(ball_2_img,(ball_scale,ball_scale))

ball_3_img=pygame.image.load('file\\img\\ball_4.png')
ball_3_img=pygame.transform.scale(ball_3_img,(ball_scale,ball_scale))

ball_4_img=pygame.image.load('file\\img\\ball_5.png')
ball_4_img=pygame.transform.scale(ball_4_img,(ball_scale,ball_scale))

ball_5_img=pygame.image.load('file\\img\\ball_5.png')
ball_5_img=pygame.transform.scale(ball_5_img,(ball_scale,ball_scale))
 
        #______________________________________________________________

player_1=pygame.image.load('file\\img\\player_1.png')
player_1=pygame.transform.scale(player_1,(player_scale,player_scale))

player_2=pygame.image.load('file\\img\\player_2.png')
player_2=pygame.transform.scale(player_2,(player_scale,player_scale))

player_3=pygame.image.load('file\\img\\player_3.png')
player_3=pygame.transform.scale(player_3,(player_scale,player_scale))

player_4=pygame.image.load('file\\img\\player_4.png')
player_4=pygame.transform.scale(player_4,(player_scale,player_scale))

player_5=pygame.image.load('file\\img\\player_5.png')
player_5=pygame.transform.scale(player_5,(player_scale,player_scale))



#_____________________________________________________________image -load-end



#_____________________________________________________________sound -load- start


ball_coll_sound_1='file\sound\\ball_coll_1.mp3'
ball_coll_sound_2='file\sound\\ball_coll_2.mp3'
ball_coll_sound_3='file\sound\\ball_coll_3.mp3'
ball_coll_sound_4='file\sound\\ball_coll_4.mp3'


ball_hite_player_sound_='file\sound\\ahhh.mp3'

#_____________________________________________________________sound -load- end


#_____________________________________________________________--random values -start
x_1_speed=9
y_1_speed=10.5

x_2_speed=random.randrange(9,12)
y_2_speed=random.randrange(8,12)

x_3_speed=random.randrange(9,12)
y_3_speed=random.randrange(8,12)

x_4_speed=random.randrange(9,12)
y_4_speed=random.randrange(8,12)

x_5_speed=random.randrange(9,12)
y_5_speed=random.randrange(8,12)
 
            #_____________________________________________________________

x_1_ball=random.randrange(0,int(SCREEN_WIDTH*(1/5)))
y_1_ball=random.randrange(0,int(SCREEN_HIG*(1/3)))

x_2_ball=random.randrange(int(SCREEN_WIDTH*(2/5)),int(SCREEN_WIDTH*(3/5)-ball_scale))
y_2_ball=random.randrange(0,int(SCREEN_HIG*(1/3)))

x_3_ball=random.randrange(int(SCREEN_WIDTH*(3/5)),int(SCREEN_WIDTH*(4/5)+ball_scale ))
y_3_ball=random.randrange(0,int(SCREEN_HIG*(1/3)))

x_4_ball=random.randrange(int(SCREEN_WIDTH*(1/5)),int(SCREEN_WIDTH*(2/5)+ball_scale ))
y_4_ball=random.randrange(int(SCREEN_HIG*(2/3)),int(SCREEN_HIG-ball_scale-10))

x_5_ball=random.randrange(int(SCREEN_WIDTH*(3/5)),int(SCREEN_WIDTH*(4/5)+ball_scale ))
y_5_ball=random.randrange(int(SCREEN_HIG*(2/3)),int(SCREEN_HIG-ball_scale-10))

#_____________________________________________________________--random values -end




class bgs(Thread):
    def bs():
        pass
        # pygame.mixer.music.load('file\\sound\\star war background.mp3')
        # pygame.mixer.music.play(loops=10)
        # time.sleep(0)
    bs()



def song(str):
    pygame.mixer.music.load(str)
    pygame.mixer.music.play() 

def text(size,coluer,txt,x_pos,y_pos):
    try:
        font_=pygame.font.SysFont(None,size)
        ren=font_.render(txt,True,coluer)
        SCREEN.blit(ren,(x_pos,y_pos))
        # pygame.display.update()
    except:
        print ('')
  
def moving_balls():
    global x_1_ball ,y_1_ball,x_2_ball,y_2_ball ,x_1_speed,y_1_speed,x_2_speed,y_2_speed,score,FPS
    global x_3_ball,y_3_ball,x_3_speed,y_3_speed
    global x_4_ball,y_4_ball,x_4_speed,y_4_speed
    global x_5_ball,y_5_ball,x_5_speed,y_5_speed
    
    x_1_ball+=x_1_speed   
    y_1_ball+=y_1_speed  
    
    x_2_ball+=x_2_speed   
    y_2_ball+=y_2_speed 

    x_3_ball+=x_3_speed   
    y_3_ball+=y_3_speed 

    x_4_ball+=x_4_speed   
    y_4_ball+=y_4_speed 

    x_5_ball+=x_5_speed   
    y_5_ball+=y_5_speed 


    FPS_change=3


    if y_1_ball+ball_scale>SCREEN_HIG or y_1_ball<0:
        y_1_speed*=-1
        score+=1
        if score%10==0:
            FPS+=FPS_change
            print("ok -- now FPS is --> ",FPS)
        song(ball_coll_sound_4)
    if x_1_ball+ball_scale>SCREEN_WIDTH or x_1_ball<0:
        x_1_speed*=-1
        if score%10==0:
            FPS+=FPS_change
            print("ok -- now FPS is --> ",FPS)
        score+=1
        
    if y_2_ball+ball_scale>SCREEN_HIG or y_2_ball<0:
        y_2_speed*=-1
        score+=1
        song(ball_coll_sound_3)
    if x_2_ball+ball_scale>SCREEN_WIDTH or x_2_ball<0:
        x_2_speed*=-1
        score+=1
        song(ball_coll_sound_3)

    if y_3_ball+ball_scale>SCREEN_HIG or y_3_ball<0:
        y_3_speed*=-1
        score+=1
        song(ball_coll_sound_4)
    if x_3_ball+ball_scale>SCREEN_WIDTH or x_3_ball<0:
        x_3_speed*=-1
        score+=1
        song(ball_coll_sound_4)


    if y_4_ball+ball_scale>SCREEN_HIG or y_4_ball<0:
        y_4_speed*=-1
        score+=1
        song(ball_coll_sound_4)
    if x_4_ball+ball_scale>SCREEN_WIDTH or x_4_ball<0:
        x_4_speed*=-1
        score+=1
        song(ball_coll_sound_4)

    if y_5_ball+ball_scale>SCREEN_HIG or y_5_ball<0:
        y_5_speed*=-1
        score+=1
        song(ball_coll_sound_4)
    if x_5_ball+ball_scale>SCREEN_WIDTH or x_5_ball<0:
        x_5_speed*=-1
        score+=1
        song(ball_coll_sound_4)

def game_stop():
    global score

    global x_1_ball ,y_1_ball,x_2_ball,y_2_ball ,x_1_speed,y_1_speed,x_2_speed,y_2_speed,score,FPS
    global x_3_ball,y_3_ball,x_3_speed,y_3_speed
    global x_4_ball,y_4_ball,x_4_speed,y_4_speed
    global x_5_ball,y_5_ball,x_5_speed,y_5_speed
    


    run=True

    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                run=False    
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_TAB:
                    pass
                    x_1_speed=9
                    y_1_speed=10.5

                    x_2_speed=random.randrange(9,12)
                    y_2_speed=random.randrange(8,12)

                    x_3_speed=random.randrange(9,12)
                    y_3_speed=random.randrange(8,12)

                    x_4_speed=random.randrange(9,12)
                    y_4_speed=random.randrange(8,12)

                    x_5_speed=random.randrange(9,12)
                    y_5_speed=random.randrange(8,12)



                    x_1_ball=random.randrange(0,int(SCREEN_WIDTH*(1/5)))
                    y_1_ball=random.randrange(0,int(SCREEN_HIG*(1/3)))

                    x_2_ball=random.randrange(int(SCREEN_WIDTH*(2/5)),int(SCREEN_WIDTH*(3/5)-ball_scale))
                    y_2_ball=random.randrange(0,int(SCREEN_HIG*(1/3)))

                    x_3_ball=random.randrange(int(SCREEN_WIDTH*(3/5)),int(SCREEN_WIDTH*(4/5)+ball_scale ))
                    y_3_ball=random.randrange(0,int(SCREEN_HIG*(1/3)))

                    x_4_ball=random.randrange(int(SCREEN_WIDTH*(1/5)),int(SCREEN_WIDTH*(2/5)+ball_scale ))
                    y_4_ball=random.randrange(int(SCREEN_HIG*(2/3)),int(SCREEN_HIG-ball_scale-10))

                    x_5_ball=random.randrange(int(SCREEN_WIDTH*(3/5)),int(SCREEN_WIDTH*(4/5)+ball_scale ))
                    y_5_ball=random.randrange(int(SCREEN_HIG*(2/3)),int(SCREEN_HIG-ball_scale-10))

                    score=0
                    FPS=40

                    return True




 
                    
                    
        text(40,(250,0,0),'GAME OVER',SCREEN_WIDTH/3,int(SCREEN_HIG/9))
        text(40,(250,0,0),'HIT "TAB" BUTTON TO RESTART',SCREEN_WIDTH/5,int(SCREEN_HIG/5.6))

        text(30,(0,0,0),'SCORE: ',20,10)
        text(30,(0,0,0),str(score),100,10)

        pygame.display.update()




def game_over():
    pass
    if x_1_ball>player_x+error and x_1_ball<player_x+player_scale-error and y_1_ball>player_y+error and y_1_ball<player_y+player_scale-error:
        print("game over")
        song(ball_hite_player_sound_)
        game_stop()

    if x_2_ball>player_x+error and x_2_ball<player_x+player_scale-error and y_2_ball>player_y+error and y_2_ball<player_y+player_scale-error:
        print("game over")
        song(ball_hite_player_sound_)
        game_stop()

    if x_3_ball>player_x+error and x_3_ball<player_x+player_scale-error and y_3_ball>player_y+error and y_3_ball<player_y+player_scale-error:
        print("game over")
        song(ball_hite_player_sound_)
        game_stop()


    if x_4_ball>player_x+error and x_4_ball<player_x+player_scale-error and y_4_ball>player_y+error and y_4_ball<player_y+player_scale-error:
        print("game over")
        song(ball_hite_player_sound_)
        game_stop()

    if x_5_ball>player_x+error and x_5_ball<player_x+player_scale-error and y_5_ball>player_y+error and y_5_ball<player_y+player_scale-error:
        print("game over")
        song(ball_hite_player_sound_)
        game_stop()


class main_game(Thread):
    
    def game():
        global score ,FPS ,player_y,player_x
        global ball_1_img,ball_2_img,ball_3_img,ball_4_img,ball_5_img


        pygame.init()
        pygame.mixer.init()
        
        
        
        background=pygame.image.load(background_img)
        background=pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HIG))

        

        # song('file\sound\\ahhh.mp3')


        # bordar_scale=1.2
        # bordar=pygame.image.load('file\img\\bordar_f3.png')
        # bordar=pygame.transform.scale(bordar,(int(SCREEN_WIDTH/bordar_scale),int(SCREEN_HIG) ))

        # pygame.time.wait()

        run=True

        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    run=False
        
            mouse_position = pygame.mouse.get_pos()


            player_x=mouse_position[0]
            player_y=mouse_position[1]
          
            score_chake=score



            

            SCREEN.blit(background,(0,0))
            SCREEN.blit(ball_1_img,(x_1_ball,y_1_ball))
            SCREEN.blit(ball_2_img,(x_2_ball,y_2_ball))
            SCREEN.blit(ball_3_img,(x_3_ball,y_3_ball))
            SCREEN.blit(ball_4_img,(x_4_ball,y_4_ball))
            SCREEN.blit(ball_5_img,(x_5_ball,y_5_ball))

#_____________________________________________________________ you can changr player from hear
#_____________________________________________________________ just change tha  number from 1 to 5


            SCREEN.blit(player_1,(player_x,player_y))


            # SCREEN.blit(bordar,(0,0))
            

            moving_balls()
            game_over()

            text(30,(0,0,0),'SCORE: ',20,10)
            text(30,(0,0,0),str(score),100,10)

            FPSCLOCK.tick(FPS)

            pygame.display.update()





    game()







# tk_screen =Tk()
# tk_screen.geometry('300x400')

# start=Button(tk_screen,text='Start',width=90,bg='red',fg='white',command=main_game).pack(pady=20)
# l=Label(tk_screen,text='select number of balls').pack()

# li_1=Listbox(tk_screen,height=5)

# li_1.insert(END,1)

# li_1.pack()

# l=Label(tk_screen,text='select lavel of game').pack()
# li_2=Listbox(tk_screen,height=5)
# li_2.pack()

# l=Label(tk_screen,text='select player').pack()
# li_3=Listbox(tk_screen,height=5)
# li_3.pack()


# mainloop()




# t1=bgs()
# t2=main_game()



# t1.start()
# t2.start()



