from importlib.util import set_loader
from tkinter import Grid
import numpy as np
#import Pygame
import operator
import random as rd
from datetime import datetime
import matplotlib.pyplot as plt
from world import world
from agent import agent


# play game :::::::

#when click start ...

gameset = world()           
gameset.agent_rand_loc()  # فقط یک بار ران میشه که تصادفی به ایجنت جا بده                     
                            #معرفی ایجنت ها به کلاس agent
                            #وارد کردن لوکیشن و امتیاز اولیه هر کدام
for j in range(0,4):
    if j==0:
        agent1 = agent(0,gameset.agents[0][j],gameset.agents[1][j])
    elif j==1:
        agent2 = agent(0,gameset.agents[0][j],gameset.agents[1][j])
    elif j==2:
        agent3 = agent(0,gameset.agents[0][j],gameset.agents[1][j])
    elif j==3:
        agent4 = agent(0,gameset.agents[0][j],gameset.agents[1][j])
            
    
#    if ("make condition for ending of game")    باید پایان بزاری
#        print("game over looser")
#        break



# last_space_update = gameset.matrix_world()
# agent3.vis(last_space_update) # قسمتی از نقشه که این ایجنت میبینه