from importlib.util import set_loader
from tkinter import Grid
import numpy as np
#import Pygame
import operator
import random as rd
from datetime import datetime
import matplotlib.pyplot as plt
from world import world


class agent:
    
    all_agent = []
    
    def __init__(self,score,xloc,yloc):
        self.score = score
        self.xloc= xloc # محور عمودی
        self.yloc=yloc  # محور افقی
        # برای مشخص کردن برنده در زمان حمله، اگر کسی که بهش حمله میشه جهت آخرین حرکتش به سمت حمله کننده نباشه، حمله پیروز میشه.
        # پس طبق آخرین حرکت به هر ایجنت یه جهت میدیم direction
        self.direction= 1 # up:1 , down:2 , right:3 , left:4
        agent.all_agent.append(self)

    def __str__(self):
           return "{self.name}"

    
    #def update_agentloc(self):
    #    for c,j in zip(agent.all_agent,range(0,4)):
    #            gameset.agents[0][j] = c.xloc
    #            gameset.agents[1][j] = c.yloc
                
#حرکت کردن ایجنت + مشخص کردن جهت ایجنت + امتیاز دادن بهش                      
# 1(up),2(down),3(right),4(left)
    def apply_action(self,act,online_space):
        m=int(self.xloc)
        n=int(self.yloc)

        if act == 1 : #up
            if online_space[m-1][n] == 999: #رفتن به خارج از نقشه
                print("wrong direction... Try again please") #یه چیزی بزار که دوباره وارد کنه جهتو
            elif online_space[m-1][n] == 2 :    #جایزه حمله
                self.direction = 1
                self.score= self.score + 2
                self.being_attacked(m-1,n,1)
                self.xloc= self.xloc - 1
            elif online_space[m-1][n] == 1 :    #جایزه غذا
                self.score=self.score + 1
                self.xloc= self.xloc - 1
            elif online_space[m-1][n] == 0:
                self.direction = 1
                self.xloc= self.xloc - 1

  
        elif act==2 : #down
            if online_space[m+1][n] == 999:#رفتن به خارج از نقشه
                print("wrong direction... Try again please") #یه چیزی بزار که دوباره وارد کنه جهتو
            elif online_space[m+1][n] == 2 :    #جایزه حمله
                self.direction = 2
                self.score= self.score + 2
                self.being_attacked(m+1,n,2)
                self.xloc= self.xloc + 1
            elif online_space[m+1][n] == 1 :    #جایزه غذا
                self.direction = 2
                self.score = self.score + 1
                self.xloc= self.xloc + 1
            elif online_space[m+1][n] == 0:
                self.direction = 2
                self.xloc= self.xloc + 1
            
        elif act==3 : #right
            if online_space[m][n+1] == 999:#رفتن به خارج از نقشه
                print("wrong direction... Try again please") #یه چیزی بزار که دوباره وارد کنه جهتو
            elif online_space[m][n+1] == 2:
                self.direction = 3
                self.score = self.score + 2
                self.being_attacked(m,n +1,3)
                self.yloc =self.yloc + 1
            elif online_space[m][n+1] == 1 :  
                self.direction = 3
                self.score = self.score + 1
                self.yloc =self.yloc + 1
            elif online_space[m][n+1] == 0:
                self.direction = 3
                self.yloc =self.yloc + 1

        elif act==4 : #left
            if online_space[m-1][n] == 999:#رفتن به خارج از نقشه
                print("wrong direction... Try again please") #یه چیزی بزار که دوباره وارد کنه جهتو
            elif online_space[m][n-1] == 2 :    #جایزه حمله
                self.direction = 4
                self.score = self.score + 2
                self.being_attacked(m ,n-1,4)
                self.yloc= self.yloc -1
            elif online_space[m][n-1] == 1 :    #جایزه غذا
                self.direction = 4
                self.score = self.score + 1
                self.yloc= self.yloc -1
            elif online_space[m][n-1] == 0 :
                self.direction = 4
                self.yloc= self.yloc -1
                
            
        #self.update_agentloc()
        
            
# پیدا کردن ایجنتی که بهش حمله شده + بررسی جهت خودش + امتیاز دادن        
    def being_attacked(self,xloc,yloc,attacker_direc):
        for c in agent.all_agent:
            if xloc == c.xloc and yloc == c.yloc:
                if c != self :
                    if c.direction!=attacker_direc :
                        c.score = c.score - 4
                    elif c.direction == attacker_direc:
                        # remove 2 points reward and reduce 4 point more because i like...
                        self.score = self.score - 6 
                        c.score = c.score + 2
                return "defeat"
        
                       
        
        # search between users of class for find location of agent who moved 
        
            
    #def reward_checker(self,online_space):
        
    #def check_situation(self,online_space,act)
     
        
    
    
            # یه ماتریس ۳*۳ که خود ایجنت وسطشه
            # تابع برای ساخت ماتریس فضای قابل مشاهده هر ایجنت
    def vis (self,online_space):
        visi = np.zeros((3,3))
        a = int(self.xloc) -1
        b = int(self.yloc) -1
        #(i,j) شمارنده برای ساخت ماتریس ۳ در ۳ از ماتریس فضای اصلی
        #(visx,visy) شمارنده در ماتریس ویز (فضای قابل مشاهده) برای هر ایجنت
        #999 قسمت های خارج از نقشه و غیر قابل ورود
        for i,visx in zip(range(a ,a+3),range(0,3)) :
            for j,visy in zip(range(b,b+3),range(0,3)):
                    if j < 0:
                        visi[visx][visy] = 999
                    elif i< 0:
                        visi[visx][visy] = 999
                    else:
                        visi[visx][visy] = online_space[i][j]
                        
        return visi
    