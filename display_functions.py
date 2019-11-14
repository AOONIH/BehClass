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

def plot_animal(animal):
    max_x = 0
    max_y = 0
    for key in animal:
        if 'right' in key:
            rightear  = animal[key]
            cur_max_x = rightear['x'].max()
            cur_max_y = rightear['y'].max()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
        elif 'left' in key:
            leftear = animal[key]
            cur_max_x = leftear['x'].max()
            cur_max_y = leftear['y'].max()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
        elif 'tail' in key:
            tail = animal[key]
            cur_max_x = tail['x'].max()
            cur_max_y = tail['y'].max()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
        elif 'nose' in key:
            nose = animal[key]
            cur_max_x = nose['x'].max()
            cur_max_y = nose['y'].max()
            if cur_max_x > max_x:
                max_x = cur_max_x
            if cur_max_y > max_y:
                max_y = cur_max_y
    num_frames = len(nose)
    max_x = int(max_x + 5)
    max_y = int(max_y + 5)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=20, metadata=dict(artist='PeterV'),bitrate=1500)
    fig = plt.figure(figsize=(10,6))
    plt.xlim(0,max_x)
    plt.ylim(0,max_y)
    plt.title('Motion of a single opponent',fontsize = 20)
    
    def animate(i):
        tail_x = tail['x'].iloc[i]
        tail_y = tail['y'].iloc[i]
        plt.scatter(tail_x,tail_y,s=10,c='r',marker="v")
        
        leftear_x = leftear['x'].iloc[i]
        leftear_y = leftear['y'].iloc[i]
        plt.scatter(leftear_x,leftear_y,s=10,c='r',marker="<")
        
        rightear_x = rightear['x'].iloc[i]
        rightear_y = rightear['y'].iloc[i]
        plt.scatter(rightear_x,rightear_y,s=10,c='r',marker=">")
        
        nose_x = nose['x'].iloc[i]
        nose_y = nose['y'].iloc[i]
        plt.scatter(nose_x,nose_y,s=10,c='r',marker="^")
        
    ani = animation.FuncAnimation(fig, animate, frames=num_frames, repeat=True)
    
    plt.show()
    
    ani.save('Single_Animal_Animation.mp4',writer=writer)
    
    
    
    