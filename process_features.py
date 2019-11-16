# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:39:09 2019

@author: Pablo
"""

import pandas as pd
import numpy as np

def get_SVD(animal):
    pass

def concatenate_body(animal):
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
            