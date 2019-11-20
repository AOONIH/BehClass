# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:39:09 2019
@author: Pablo
"""

import pandas as pd
import numpy as np
import math
from scipy import signal
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap


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

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def rotate_vector(vector_x,vector_y,rotation):
    if vector_x < 0:
        rotation = rotation * -1
        
    new_x = vector_x * math.cos(rotation) - vector_y * math.sin(rotation)
    new_y = vector_y * math.cos(rotation) - vector_x * math.sin(rotation)
    return (new_x,new_y)

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
    
    num_frames = len(nose1)
    
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
        
        cur_ear_mid = cur_left_ear1[0:2] + (1/2 * (cur_right_ear1[0:2]-cur_left_ear1[0:2]))
        
        
        rotation = angle_between(cur_ear_mid,[0,1])
        tail1.iloc[frame] = cur_reference
        
        cur_right_ear1[0],cur_right_ear1[1] = rotate_vector(cur_right_ear1[0],cur_right_ear1[1],rotation)
        cur_left_ear1[0],cur_left_ear1[1] = rotate_vector(cur_left_ear1[0],cur_left_ear1[1],rotation)
        cur_nose1[0],cur_nose1[1] = rotate_vector(cur_nose1[0],cur_nose1[1],rotation)
        
        cur_tail2[0],cur_tail2[1] = rotate_vector(cur_tail2[0],cur_tail2[1],rotation)
        cur_right_ear2[0],cur_right_ear2[1] = rotate_vector(cur_right_ear2[0],cur_right_ear2[1],rotation)
        cur_left_ear2[0],cur_left_ear2[1] = rotate_vector(cur_left_ear2[0],cur_left_ear2[1],rotation)
        cur_nose2[0],cur_nose2[1] = rotate_vector(cur_nose2[0],cur_nose2[1],rotation)
        
        cur_ear_mid = cur_left_ear1[0:2] + (1/2 * (cur_right_ear1[0:2]-cur_left_ear1[0:2]))
        
        if cur_ear_mid[1] < 0:
            cur_right_ear1[1] = cur_right_ear1[1] * -1
            cur_left_ear1[1] = cur_left_ear1[1] * -1
            cur_nose1[1] = cur_nose1[1] * -1
            
            cur_tail2[1] = cur_tail2[1] * -1
            cur_right_ear2[1] = cur_right_ear2[1] * -1
            cur_left_ear2[1] = cur_left_ear2[1] * -1
            cur_nose2[1] = cur_nose2[1] * -1
        
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

def get_distance(series1,series2):
    distance = np.sqrt(sum((series1-series2) ** 2))
    if distance < 1/100:
        distance = 0.0
    return distance

def dif_matrix(animal1,animal2,start_time = 0):
    parts_ani1 = len(animal1)
    parts_ani2 = len(animal2)
    cur_time = start_time
    example_dict = animal1[list(animal1.keys())[0]]
    max_len = len(example_dict)
    empty_frame = np.empty([parts_ani1+parts_ani1, parts_ani2+parts_ani2])
    data_store = np.empty([(parts_ani1+parts_ani1) ** 2,1])
    
    for counter in range(cur_time,max_len):
        row = 0 
        for key1 in animal1:
            col = 0
            cur_main_part = animal1[key1]
            cur_point = cur_main_part.iloc[counter]
            for key2 in animal1:
                cur_comp_part = animal1[key2]
                cur_comp_point= cur_comp_part.iloc[counter]
                distance = get_distance(cur_point,cur_comp_point)
                empty_frame[row,col] = distance
                col = col + 1
            for key2 in animal2:
                cur_comp_part = animal2[key2]
                cur_comp_point= cur_comp_part.iloc[counter]
                distance = get_distance(cur_point,cur_comp_point)
                empty_frame[row,col] = distance
                col = col + 1
            row = row + 1
        for key1 in animal2:
            col = 0
            cur_main_part = animal2[key1]
            cur_point = cur_main_part.iloc[counter]
            for key2 in animal1:
                cur_comp_part = animal1[key2]
                cur_comp_point= cur_comp_part.iloc[counter]
                distance = get_distance(cur_point,cur_comp_point)
                empty_frame[row,col] = distance
                col = col + 1
            for key2 in animal2:
                cur_comp_part = animal2[key2]
                cur_comp_point= cur_comp_part.iloc[counter]
                distance = get_distance(cur_point,cur_comp_point)
                empty_frame[row,col] = distance
                col = col + 1
            row = row + 1
        flat_time = empty_frame.flatten('F')
        flat_time = np.reshape(flat_time,[(parts_ani1+parts_ani1) ** 2,1])
        data_store= np.concatenate((data_store,flat_time),axis = 1)
    data_store = data_store[:,1:]
    return data_store

def perform_pca(difference_mat,threshold = 0.05):
    pca = PCA()
    pca.fit(difference_mat)
    singular_values = pca.singular_values_
    tot_sing = sum(singular_values)
    selected_components = singular_values > (tot_sing * threshold)
    all_components =  pca.components_
    selected_components = all_components[selected_components,:]
    
    return selected_components

def take_spectrum(pcs,frame_rate = 50,width = 0.25):
    max_width = int(frame_rate/2)
    widths = np.arange(width,max_width,width)
    
    spectral_components = list()
    for component in  range(pcs.shape[0]):
        cur_comp = pcs[component,:]
        spectral_components.append(signal.cwt(cur_comp,signal.ricker,widths))
    return spectral_components

def gen_tsne(spectra_list,pooling = 1):
    tsne_vector = spectra_list[0]
    for spectra in range(1,len(spectra_list)):
        tsne_vector = np.concatenate((tsne_vector,spectra_list[spectra]))
    pooling = int(pooling)
    if pooling > 1:
        counter = 0
        while 
    embedded_2 = TSNE(n_components=2).fit_transform(tsne_vector.transpose())
    embedded_3 = TSNE(n_components=3).fit_transform(tsne_vector.transpose())
    return (embedded_2, embedded_3)
    
def gen_umap(spectra_list,pooling=1):
    umap_vector = spectra_list[0]
    for spectra in range(1,len(spectra_list)):
        umap_vector = np.concatenate((umap_vector,spectra_list[spectra]))
    reducer = umap.UMAP()
    embedding_umap = reducer.fit_transform(umap_vector)
    return embedding_umap
        