import pygame as pg
import pygame_menu
from main import *
from new_credits import *
from object_handler import *


class Menu:
    def __init__(self,game):
        self.game = game
        self.display_value=0
        self.menu = None
        self. current_user = 'Lalit'
        

    def draw_background(self):
        self.back_image = pg.image.load('resources/backgrounds/main_menu_background.jpg')
        self.back_image = pg.transform.scale(self.back_image,(RES)).convert_alpha()
        self.game.screen.blit(self.back_image,(0,0))
    
    def play_credits(self):
        credits()
    
    def change_user(self,name):
        self.current_user = name
    def draw_main_menu(self):
        self.theme=pygame_menu.themes.THEME_DARK.copy()
        self.theme.set_background_color_opacity(0.8)
        self.submenu_theme = self.theme 
    
        #self.theme.background_color = pygame_menu.BaseImage(image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER)
        self.menu = pygame_menu.Menu(title="ShotGun3D",width=RES[0] * 0.3,height=RES[1]*0.48,theme=self.theme)
        self.menu.add.text_input('User Name :', default=self.current_user,onchange=self.change_user)
        self.menu.add.selector('Difficulty :', [('Easy', 0),('Medium', 1),('Hard', 2) ], onchange=self.set_difficulty,default=self.game.diff)
        self.menu.add.selector('Display :',[('1600x900',0),('1366x768',1),('1280x720',2)],onchange=self.set_display, default=self.display_value)
        self.menu.add.button('Play', self.start_the_game)
        self.menu.add.button('Credits', self.play_credits)
        #self.menu.add.button('Change User', self.change_user)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.set_relative_position(RES[0]*0.012//1,RES[1]*0.05//1)
        
    
    def start_the_game(self):
        self.game.current = True
        self.game.run()
    
    def set_difficulty(self,value, difficulty):
        # Do the job here !
        if difficulty == 1:
            self.game.object_handler.enemies = 30
        elif difficulty == 2:
            self.game.object_handler.enemies = 38
        self.game.diff = difficulty

    def set_display(self,sizes,value):
        if value == 0:
            RES = 1600,900
        elif value == 1:
            RES = 1366,768
        elif value == 2:
            RES = 1280,720
        else:
            RES = 1600,900

        self.game.screen=pg.display.set_mode(RES)
        #self.game.update()
        self.display_value=value
        

    def draw(self):
        self.draw_main_menu()
        self.menu.mainloop(self.game.screen,self.draw_background)
