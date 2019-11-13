#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:47:52 2019

@author: Pablo

"""

"""
1) Velocity of animal
2) Velocity of snout
3) Body vector w.r.t box
4) Head vector w.r.t. body
5) Tail to head, 1 through midpoint, 1 direct
6) Derivatives of these
7) Rotation speed of body vector
"""

import pandas as pd
import numpy as np
import math
def get_centre_mass(panda_list):
    # This function will parse a list of pandas with the same dimensions and 
    # generate an average of the values for each index, returning a panda
    num_samples = len(panda_list[0])
    num_pandas  = len(panda_list)
    for comp_panda in panda_list:
        if num_samples != len(comp_panda):
            raise Exception('Not all data frames are the same size')
    centre_mass = list()
    for time in range(num_samples):
        ave_x = 0
        ave_y = 0
        ave_z = 0
        for data in panda_list:
            ave_x = ave_x + data['x'][time]
            ave_y = ave_y + data['y'][time]
            ave_z = ave_z + data['z'][time]
        ave_x = ave_x / num_pandas
        ave_y = ave_y / num_pandas
        ave_z = ave_z / num_pandas
        centre_mass.append([ave_x,ave_y,ave_z])
    centre_mass_pd = pd.DataFrame(centre_mass,columns=list('xyz'))
    
    return centre_mass_pd
def vector_length(vector_array):
    # This function is a utility.  Given an Nx1 array of values, this function
    # will return the length of the vector
    length = np.sqrt(np.sum(np.square(vector_array)))
    return length

def unit_vector(vector):
    # This function is a utility.  Given a Nx1 array of values, this function
    # will return the unit vector
    return vector / np.linalg.norm(vector)  
    
def get_velocity(dataframe):
    # This function will take a panda and calculate the derivative across each
    # column, returning this as a panda, as well as a displacement value, also
    # returned as a panda with a two columns, 1 for displacement in xy, the
    # other as displacement in xyz
    component_diff = dict()
    displacement = list()
    for (columnName, columnData) in dataframe.iteritems():
        cur_data = columnData.values
        cur_data_diff = np.gradient(cur_data)
        component_diff.update({columnName:cur_data_diff})
    velocity = pd.DataFrame(component_diff)
    xy = list()
    xyz = list()
    for time in range(1,len(dataframe)):
        pre_time = time - 1
        pre_value = dataframe.iloc[pre_time]
        current_value = dataframe.iloc[time]
        component_displacement = current_value - pre_value
        component_displacement = component_displacement.values
        xy.append(vector_length(component_displacement[0:2]))
        xyz.append(vector_length(component_displacement[0:3]))
    xy.append(0)
    xyz.append(0)
    displacement = pd.DataFrame({'xy':xy,'xyz':xyz},columns=['xy','xyz'])
    return velocity,displacement

def body_vector(left_ear,right_ear,tail,head):
    num_samples = len(left_ear)
    
    body_angle_list  = list()
    head_angle_list  = list()
    body_length_list = list()
    tail_nose_list   = list()
    body_rotation= list()
    
    if (num_samples != len(right_ear)) or (num_samples != len(tail)):
        raise Exception('Data frames do not have the same number of indeces')
    basis_vector = unit_vector((1,1,1))
    old_body_vec = basis_vector
    for frame in range(num_samples):
        # Get positions
        left_ear_pos = left_ear.iloc[frame]
        right_ear_pos= right_ear.iloc[frame]
        tail_pos     = tail.iloc[frame]
        head_pos     = head.iloc[frame]
        # Get location of ear midpoint
        ear_midpoint = (left_ear_pos - right_ear_pos).values
        ear_midpoint = ear_midpoint * 0.5
        ear_midpoint = right_ear_pos.values + ear_midpoint
        
        body_vector = tail_pos.values - ear_midpoint
        tail_ear_dist = vector_length(body_vector)
        body_vector = unit_vector(body_vector)
        body_angle  = np.arccos(np.clip(np.dot(body_vector,basis_vector), -1.0, 1.0))
        head_vector = head_pos.values - ear_midpoint
        head_ear_dist = vector_length(head_vector)
        body_length_list.append(tail_ear_dist + head_ear_dist)
        tail_nose_list.append(vector_length(head_pos - tail_pos))
        head_vector = unit_vector(head_vector)
        head_angle  = np.arccos(np.clip(np.dot(body_vector,head_vector),-1.0,1.0))
        body_angle_list.append(body_angle)
        head_angle_list.append(head_angle)
        # Note the initial body_rotation will reflect the starting angle of the
        # vector w.r.t the box
        body_rot = np.arccos(np.clip(np.dot(body_vector,old_body_vec),-1.0,1.0))
        body_rotation.append(body_rot)
        old_body_vec = body_vector
    output_dict = {'Body_Angle':body_angle_list,
                   'Head_Angle':head_angle_list,
                   'Animal_Length':body_length_list,
                   'Tail_to_Nose':tail_nose_list,
                   'Rotation':body_rotation,
                   'Rotational_Speed':np.gradient(body_rotation)}
    output_panda = pd.DataFrame(output_dict,columns=list(output_dict.keys))
    return output_panda
    
    
        
        
        
        
        
    
        
        
    
    
    
        