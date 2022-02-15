from importlib.util import set_loader
from tkinter import Grid
import numpy as np
#import Pygame
import operator
import random as rd
from datetime import datetime
import matplotlib.pyplot as plt


class world:
    def __init__(self):
        self.height = 20
        self.width = 20
        self.randomize_counter = 0 #  فقط برای اینکه هر دست بیشتر از یکبار رندوم نزنه جاهارو
        self.grid = np.zeros(( self.height, self.width))
        self.foods = np.zeros((2,8)) #لوکیشن همه غذاها
        self.agents = np.zeros((2,4)) #لوکیشن همه‌ی ایجنت ها
        
        #جای تصادفیاولیه غذا
    def make_food(self):   
    #random loc for foods
        for i in range (0,8):
            x=np.random.randint(0,19)
            rd.seed(datetime.now())
            y=np.random.randint(0,19)
            #چک کردن روی هم نیوفتادن غذا ها
            for j in range(0,i-1):
                if self.foods[0][j]== self.foods[0][i] and self.foods[1][j]== self.foods[1][i] :
                    x=np.random.randint(0,19)
                    rd.seed(datetime.now())
                    y=np.random.randint(0,19)
                    
            self.grid[x][y] = 1
            self.foods[0][i]= x
            self.foods[1][i]= y
            
    
    # جای اولیه ایجنت ها
    def agent_rand_loc(self):
        if self.randomize_counter > 1: # بررسی اینکه یه بار بیشتر باز نشه
            print("Can't randomize agent again namusan...")
        else:    
            self.randomize_counter = self.randomize_counter + 1
            for i in range (0,4):
                x=np.random.randint(0,19)
                rd.seed(datetime.now())
                y=np.random.randint(0,19)
                for j in range(0,i-1):
                    if self.agents[0][j]== self.agents[0][i] and self.agents[1][j]== self.agents[1][i] :
                        x=np.random.randint(0,19)
                        rd.seed(datetime.now())
                        y=np.random.randint(0,19)
                if self.grid[x][y]!=1 :
                    self.grid[x][y] = 2
                    self.agents[0][i]= x
                    self.agents[1][i]= y
                else:
                    rd.seed(datetime.now())
                    self.grid[x][np.random.randint(0,19)] = 2
                    self.agents[0][i]= x
                    self.agents[1][i]= np.random.randint(0,19)
    
        #وارد کردن اخرین تغییرات در ماتریس نقشه و برگردوندنش
    def matrix_world(self):
        virtual_space = np.zeros((20,20))
        if self.randomize_counter <=  1: # بررسی اینکه یه بار بیشتر رندوم نزنه 
            self.agent_rand_loc()
            self.make_food()
            self.randomize_counter = self.randomize_counter + 1
            for i in range (0,8):
                x= int(self.foods[0][i])
                y= int(self.foods[1][i])
                virtual_space[x][y] = 1
            for i in range (0,4):
                x= int(self.agents[0][i])
                y= int(self.agents[1][i])
                virtual_space[x][y] = 2
        else:
            for i in range (0,8):
                x= int(self.foods[0][i])
                y= int(self.foods[1][i])
                virtual_space[x][y] = 1
            for i in range (0,4):
                x= int(self.agents[0][i])
                y= int(self.agents[1][i])
                virtual_space[x][y] = 2
        self.grid = virtual_space
        return virtual_space
    
    
   # def get_available_act(????)

    #def end_game