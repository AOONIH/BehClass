# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:39:09 2019

@author: Pablo
"""

import pandas as pd
import numpy as np

def get_SVD(animal):
    pass

def format_data(animal,num_coords = 3):
    animal_parts = list()
    for key in animal:
        animal_parts.append(animal[key])
    num_samples = len(animal_parts[0])
    num_parts   = len(animal_parts)
    num_columns = num_samples
    
    coords = list()
    
    for dot in range(num_parts):
        cur_part = animal_parts[dot]
        cur_animal_array = np.empty([num_coords,num_columns])
        for time in range(num_samples):
            cur_animal_array[:,time] = list(cur_part.iloc[time])
        coords.append(cur_animal_array)
    output_mat = coords[0]
    for dot in range(1,num_parts):
        output_mat = np.concatenate((output_mat,coords[dot]),axis = 0)
    
    return output_mat
            
    

def reset_reference(animal):
    for key in animal:
        if 'right' in key:
            rightear  = animal[key]
        elif 'left' in key:
            leftear = animal[key]
        elif 'tail' in key:
            tail = animal[key]
        elif 'nose' in key:
            nose = animal[key]
    num_frames = len(nose)
    for frame in range(num_frames):
        cur_reference = tail.iloc[frame]
        cur_nose      = nose.iloc[frame]
        cur_right_ear = rightear.iloc[frame]
        cur_left_ear  = leftear.iloc[frame]
        cur_nose = cur_nose - cur_reference
        cur_right_ear = cur_right_ear - cur_reference
        cur_left_ear  = cur_left_ear - cur_reference
        cur_reference = cur_reference - cur_reference
        tail.iloc[frame] = cur_reference
        rightear.iloc[frame] = cur_right_ear
        leftear.iloc[frame]  = cur_left_ear
        nose.iloc[frame]     = cur_nose
    
    for key in animal:
        if 'right' in key:
            animal[key] = rightear
        elif 'left' in key:
            animal[key] = leftear
        elif 'tail' in key:
            animal[key] = tail
        elif 'nose' in key:
            animal[key] = nose
    
    return animal
            