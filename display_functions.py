# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:10:36 2019

@author: Pablo

"""
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import numpy as np

def plot_animal(animal,title):
    max_x = 0
    max_y = 0
    min_x = 1000
    min_y = 1000
    for key in animal:
        if 'right' in key:
            rightear1  = animal[key]
            cur_max_x = rightear1['x'].max()
            cur_max_y = rightear1['y'].max()
            cur_min_x = rightear1['x'].min()
            cur_min_y = rightear1['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'left' in key:
            leftear1 = animal[key]
            cur_max_x = leftear1['x'].max()
            cur_max_y = leftear1['y'].max()
            cur_min_x = leftear1['x'].min()
            cur_min_y = leftear1['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'tail' in key:
            tail1 = animal[key]
            cur_max_x = tail1['x'].max()
            cur_max_y = tail1['y'].max()
            cur_min_x = tail1['x'].min()
            cur_min_y = tail1['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'nose' in key:
            nose1 = animal[key]
            cur_max_x = nose1['x'].max()
            cur_max_y = nose1['y'].max()
            cur_min_x = nose1['x'].min()
            cur_min_y = nose1['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
                
                
    num_frames = len(nose1)
    max_x = int(max_x + 5)
    max_y = int(max_y + 5)
    min_x = int(min_x - 5)
    min_y = int(min_y - 5)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=50, metadata=dict(artist='PeterV'),bitrate=1500)
    
    ear_axis_x1   = [rightear1['x'].iloc[0],leftear1['x'].iloc[0]]
    ear_axis_y1   = [rightear1['y'].iloc[0],leftear1['y'].iloc[0]]
    
    ear_mid_point_x1 = ear_axis_x1[0] + 1/2 * (ear_axis_x1[1] - ear_axis_x1[0])
    ear_mid_point_y1 = ear_axis_y1[0] + 1/2 * (ear_axis_y1[1] - ear_axis_y1[0])
    
    tail1_axis_x1 = [tail1['x'].iloc[0],ear_mid_point_x1]
    tail1_axis_y1 = [tail1['y'].iloc[0],ear_mid_point_y1]
    
    nose1_axis_x1 = [ear_mid_point_x1,nose1['x'].iloc[0]]
    nose1_axis_y1 = [ear_mid_point_y1,nose1['y'].iloc[0]]
    
    fig, ax = plt.subplots(1)
    
    line1 = ax.plot(tail1_axis_x1,tail1_axis_y1)[0]
    line2 = ax.plot(ear_axis_x1,ear_axis_y1)[0]
    line3 = ax.plot(nose1_axis_x1,nose1_axis_y1)[0]
    
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)

    
    def animate(i, line1,line2,line3):
        
        ear_axis_x1   = [rightear1['x'].iloc[i],leftear1['x'].iloc[i]]
        ear_axis_y1   = [rightear1['y'].iloc[i],leftear1['y'].iloc[i]]
    
        ear_mid_point_x1 = ear_axis_x1[0] + 1/2 * (ear_axis_x1[1] - ear_axis_x1[0])
        ear_mid_point_y1 = ear_axis_y1[0] + 1/2 * (ear_axis_y1[1] - ear_axis_y1[0])
    
        tail1_axis_x1 = [tail1['x'].iloc[i],ear_mid_point_x1]
        tail1_axis_y1 = [tail1['y'].iloc[i],ear_mid_point_y1]
    
        nose1_axis_x1 = [ear_mid_point_x1,nose1['x'].iloc[i]]
        nose1_axis_y1 = [ear_mid_point_y1,nose1['y'].iloc[i]]
    
        line1.set_xdata(tail1_axis_x1)
        line1.set_ydata(tail1_axis_y1)
        
        line2.set_xdata(ear_axis_x1)
        line2.set_ydata(ear_axis_y1)
        
        line3.set_xdata(nose1_axis_x1)
        line3.set_ydata(nose1_axis_y1)
        
        return (line1,line2,line3)
                
    ani = animation.FuncAnimation(fig, animate, frames=num_frames, fargs=[line1,line2,line3])
    
    file_name = title + '.mp4'
    ani.save(file_name,writer=writer)
    
    
def plot_two_animals(animal1,animal2,title):
    max_x = 0
    max_y = 0
    min_x = 1000
    min_y = 1000
    for key in animal:
        if 'right' in key:
            rightear1  = animal[key]
            cur_max_x = rightear1['x'].max()
            cur_max_y = rightear1['y'].max()
            cur_min_x = rightear1['x'].min()
            cur_min_y = rightear1['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'left' in key:
            leftear1 = animal[key]
            cur_max_x = leftear1['x'].max()
            cur_max_y = leftear1['y'].max()
            cur_min_x = leftear1['x'].min()
            cur_min_y = leftear1['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'tail' in key:
            tail1 = animal[key]
            cur_max_x = tail1['x'].max()
            cur_max_y = tail1['y'].max()
            cur_min_x = tail1['x'].min()
            cur_min_y = tail1['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'nose' in key:
            nose1 = animal[key]
            cur_max_x = nose1['x'].max()
            cur_max_y = nose1['y'].max()
            cur_min_x = nose1['x'].min()
            cur_min_y = nose1['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
                
    for key in animal2:
        if 'right' in key:
            rightear2  = animal2[key]
            cur_max_x = rightear2['x'].max()
            cur_max_y = rightear2['y'].max()
            cur_min_x = rightear2['x'].min()
            cur_min_y = rightear2['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'left' in key:
            leftear2 = animal2[key]
            cur_max_x = leftear2['x'].max()
            cur_max_y = leftear2['y'].max()
            cur_min_x = leftear2['x'].min()
            cur_min_y = leftear2['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'tail' in key:
            tail2 = animal2[key]
            cur_max_x = tail2['x'].max()
            cur_max_y = tail2['y'].max()
            cur_min_x = tail2['x'].min()
            cur_min_y = tail2['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
        elif 'nose' in key:
            nose2 = animal2[key]
            cur_max_x = nose2['x'].max()
            cur_max_y = nose2['y'].max()
            cur_min_x = nose2['x'].min()
            cur_min_y = nose2['y'].min()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
            if cur_min_x < min_x:
                min_x = cur_min_x
            if cur_min_y < min_y:
                min_y = cur_min_y
                
                
    num_frames = len(nose1)
    max_x = int(max_x + 5)
    max_y = int(max_y + 5)
    min_x = int(min_x - 5)
    min_y = int(min_y - 5)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=50, metadata=dict(artist='PeterV'),bitrate=1500)
    
    ear_axis_x1   = [rightear1['x'].iloc[0],leftear1['x'].iloc[0]]
    ear_axis_y1   = [rightear1['y'].iloc[0],leftear1['y'].iloc[0]]
    
    ear_mid_point_x1 = ear_axis_x1[0] + 1/2 * (ear_axis_x1[1] - ear_axis_x1[0])
    ear_mid_point_y1 = ear_axis_y1[0] + 1/2 * (ear_axis_y1[1] - ear_axis_y1[0])
    
    tail1_axis_x1 = [tail1['x'].iloc[0],ear_mid_point_x1]
    tail1_axis_y1 = [tail1['y'].iloc[0],ear_mid_point_y1]
    
    nose1_axis_x1 = [ear_mid_point_x1,nose1['x'].iloc[0]]
    nose1_axis_y1 = [ear_mid_point_y1,nose1['y'].iloc[0]]
    
    
    ear_axis_x2   = [rightear2['x'].iloc[0],leftear2['x'].iloc[0]]
    ear_axis_y2   = [rightear2['y'].iloc[0],leftear2['y'].iloc[0]]
    
    ear_mid_point_x2 = ear_axis_x2[0] + 1/2 * (ear_axis_x2[1] - ear_axis_x2[0])
    ear_mid_point_y2 = ear_axis_y2[0] + 1/2 * (ear_axis_y2[1] - ear_axis_y2[0])
    
    tail1_axis_x2 = [tail2['x'].iloc[0],ear_mid_point_x2]
    tail1_axis_y2 = [tail2['y'].iloc[0],ear_mid_point_y2]
    
    nose1_axis_x2 = [ear_mid_point_x2,nose2['x'].iloc[0]]
    nose1_axis_y2 = [ear_mid_point_y2,nose2['y'].iloc[0]]
    
    fig, ax = plt.subplots(1)
    
    line1 = ax.plot(tail1_axis_x1,tail1_axis_y1)[0]
    line2 = ax.plot(ear_axis_x1,ear_axis_y1)[0]
    line3 = ax.plot(nose1_axis_x1,nose1_axis_y1)[0]
    
    line4 = ax.plot(tail1_axis_x2,tail1_axis_y2)[0]
    line5 = ax.plot(ear_axis_x2,ear_axis_y2)[0]
    line6 = ax.plot(nose1_axis_x2,nose1_axis_y2)[0]
    
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)

    
    def animate(i, line1,line2,line3,line4,line5,line6):
        
        ear_axis_x1   = [rightear1['x'].iloc[i],leftear1['x'].iloc[i]]
        ear_axis_y1   = [rightear1['y'].iloc[i],leftear1['y'].iloc[i]]
    
        ear_mid_point_x1 = ear_axis_x1[0] + 1/2 * (ear_axis_x1[1] - ear_axis_x1[0])
        ear_mid_point_y1 = ear_axis_y1[0] + 1/2 * (ear_axis_y1[1] - ear_axis_y1[0])
    
        tail1_axis_x1 = [tail1['x'].iloc[i],ear_mid_point_x1]
        tail1_axis_y1 = [tail1['y'].iloc[i],ear_mid_point_y1]
    
        nose1_axis_x1 = [ear_mid_point_x1,nose1['x'].iloc[i]]
        nose1_axis_y1 = [ear_mid_point_y1,nose1['y'].iloc[i]]
        
        
        ear_axis_x2   = [rightear2['x'].iloc[i],leftear2['x'].iloc[i]]
        ear_axis_y2   = [rightear2['y'].iloc[i],leftear2['y'].iloc[i]]
    
        ear_mid_point_x2 = ear_axis_x2[0] + 1/2 * (ear_axis_x2[1] - ear_axis_x2[0])
        ear_mid_point_y2 = ear_axis_y2[0] + 1/2 * (ear_axis_y2[1] - ear_axis_y2[0])
    
        tail1_axis_x2 = [tail2['x'].iloc[i],ear_mid_point_x2]
        tail1_axis_y2 = [tail2['y'].iloc[i],ear_mid_point_y2]
    
        nose1_axis_x2 = [ear_mid_point_x2,nose2['x'].iloc[i]]
        nose1_axis_y2 = [ear_mid_point_y2,nose2['y'].iloc[i]]
    
        line1.set_xdata(tail1_axis_x1)
        line1.set_ydata(tail1_axis_y1)
        
        line2.set_xdata(ear_axis_x1)
        line2.set_ydata(ear_axis_y1)
        
        line3.set_xdata(nose1_axis_x1)
        line3.set_ydata(nose1_axis_y1)
        
        line4.set_xdata(tail1_axis_x2)
        line4.set_ydata(tail1_axis_y2)
        
        line5.set_xdata(ear_axis_x2)
        line5.set_ydata(ear_axis_y2)
        
        line6.set_xdata(nose1_axis_x2)
        line6.set_ydata(nose1_axis_y2)
        
        return (line1,line2,line3,line4,line5,line6)
                
    ani = animation.FuncAnimation(fig, animate, frames=num_frames, fargs=[line1,line2,line3,line4,line5,line6])
    
    file_name = title + '.mp4'
    ani.save(file_name,writer=writer)