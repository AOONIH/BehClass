# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:39:09 2019
@author: Pablo
"""

import pandas as pd
import numpy as np

def get_SVD(animal_SVD_mat):
    m_val = animal_SVD_mat.shape[0]
    n_val = animal_SVD_mat.shape[1]
    if m_val < n_val:
        animal_SVD_mat = animal_SVD_mat.transpose()
        m_val = animal_SVD_mat.shape[0]
        n_val = animal_SVD_mat.shape[1]
    
    u, s, vh = np.linalg.svd(animal_SVD_mat, full_matrices=True)
    s_diag = np.diag(s)
    # Now add the remaining zeros to the s_diag matrix
    
    concat_mat_size = m_val - n_val
    empty_mat = np.zeros([concat_mat_size,n_val])
    s_full = np.concatenate((s_diag,empty_mat),axis = 0)
    
    new_data = u @ s @ vh
    
    

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
    
    return output_mat.transpose()
            
def remake_panda(SVD_format,panda_format):
    pass

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

def reference_to_ani(animal1,animal2):
    for key in animal1:
        if 'right' in key:
            rightear1  = animal1[key]
        elif 'left' in key:
            leftear1 = animal1[key]
        elif 'tail' in key:
            tail1 = animal1[key]
        elif 'nose' in key:
            nose1 = animal1[key]      
    for key in animal2:
        if 'right' in key:
            rightear2  = animal2[key]
        elif 'left' in key:
            leftear2 = animal2[key]
        elif 'tail' in key:
            tail2 = animal2[key]
        elif 'nose' in key:
            nose2 = animal2[key]
    
    num_frames = len(nose)
    
    for frame in range(num_frames):
        
        cur_reference = tail1.iloc[frame]
        
        cur_nose1      = nose1.iloc[frame]
        cur_right_ear1 = rightear1.iloc[frame]
        cur_left_ear1  = leftear1.iloc[frame]
        
        cur_tail2      = tail2.iloc[frame]
        cur_nose2      = nose2.iloc[frame]
        cur_right_ear2 = rightear2.iloc[frame]
        cur_left_ear2  = leftear2.iloc[frame]
        
        
        cur_nose1      = cur_nose1 - cur_reference
        cur_right_ear1 = cur_right_ear1 - cur_reference
        cur_left_ear1  = cur_left_ear1 - cur_reference
        
        cur_tail2      = cur_tail2 - cur_reference
        cur_nose2      = cur_nose2 - cur_reference
        cur_right_ear2 = cur_right_ear2 - cur_reference
        cur_left_ear2  = cur_left_ear2 - cur_reference
        
        
        cur_reference  = cur_reference - cur_reference
        
        tail1.iloc[frame] = cur_reference
        rightear1.iloc[frame] = cur_right_ear1
        leftear1.iloc[frame]  = cur_left_ear1
        nose1.iloc[frame]     = cur_nose1
        
        tail2.iloc[frame] = cur_tail2
        rightear2.iloc[frame] = cur_right_ear2
        leftear2.iloc[frame]  = cur_left_ear2
        nose2.iloc[frame]     = cur_nose2
        
    for key in animal1:
        if 'right' in key:
            animal1[key] = rightear1
        elif 'left' in key:
            animal1[key] = leftear1
        elif 'tail' in key:
            animal1[key] = tail1
        elif 'nose' in key:
            animal1[key] = nose1
    for key in animal2:
        if 'right' in key:
            animal2[key] = rightear2
        elif 'left' in key:
            animal2[key] = leftear2
        elif 'tail' in key:
            animal2[key] = tail2
        elif 'nose' in key:
            animal2[key] = nose2
    
    return animal1, animal2
        

def dif_matrix(animal1,animal2):
    