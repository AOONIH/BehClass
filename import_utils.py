#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:15:44 2019

@author: Pablo
"""

import pandas as pd
import glob
import os

def import_animal(animal_uni_ID,parent_dir='Behaviour_Module_Data'):
    # This function will load in the data from a specified folder (first
    # argument) and put them into a dictionary with the file name as the key
    animal_folder = glob.glob(parent_dir + '/*' + animal_uni_ID + '*')
    data_store = dict()
    if len(animal_folder) > 1:
        raise Exception('Multiple options returned.  Be more specific')
    else:
        animal_folder = animal_folder[0]
    for r,d,f in os.walk(animal_folder):
        for file in f:
            if '.h5' in file:
                file_name = file.replace('.h5','')
                cur_file = os.path.join(r,file)
                cur_data = pd.read_hdf(cur_file)
                data_store.update({file_name:cur_data})
    return data_store

def filter_dictionary(dictionary,key_word):
    new_dict = dict()
    for key in dictionary:
        if key_word in key:
            new_dict.update({key:dictionary[key]})
    return new_dict
    

def reject_start_segment(panda_dict):
    # This function accepts a dictionary of pandas as input and will trim off all the
    # start values that are common across the pandas.
    test_panda = panda_dict[list(panda_dict.keys())[0]]
    num_rows  = len(test_panda)
    delete_columns = list()
    for row in range(num_rows):
        cur_row_val = test_panda.iloc[row]
        for key in panda_dict:
            cur_comp_panda = panda_dict[key]
            cur_comp_val = cur_comp_panda.iloc[row]
            if cur_row_val.equals(cur_comp_val):
                delete_columns.append(row)
            else:
                return delete_columns

def trim_start(panda_dict):
    reject_times = reject_start_segment(panda_dict)
    final_time   = reject_times[-1]
    new_panda_dict = dict()
    for key in panda_dict:
        cur_panda = panda_dict[key]
        new_panda = cur_panda.iloc[final_time:]
        new_panda = new_panda.reset_index()
        new_panda = new_panda.drop(columns="index")
        new_panda_dict.update({key:new_panda})
        
        

def downsample_panda(panda,window):
    # This function accepts a single panda as input and 
    new_panda = dict()
    for col in panda.columns:
        cur_panda_data = panda[col]
        counter = 0
        index = 0
        max_val = len(cur_panda_data)-window + 1
        while counter < max_val:
            cur_window = list(range(counter,counter+window))
            
        
    