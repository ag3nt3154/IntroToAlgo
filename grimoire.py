# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:25:04 2017

@author: alexr
"""
import json
import numpy as np
import time
import os


def dump_json(data, filename):
    """
    Save JSON object to file
    """
    with open(filename, 'w') as f:
        data = json.dump(data, f)


def load_json(filename):
    """
    Load JSON object from file
    """
    with open(filename, 'r') as f:
        data = json.load(f)
        return data


def clear_disp():
    """
    Clears the printed display. Works well in command prompt, less so for pycharm and git bash
    :return:
    """
    os.system('cls')
    
def count_line(file_name):
    """
    Find no. of lines in a large text/.fvp file
    :param file_name:   Name/path of file e.g. 'D118 Re40 8.3M C2 300x300.fvp'
    :return:            No. of lines in the file
    """
    with open(file_name, 'r') as file:
        num_lines = sum(1 for line in file)
    return num_lines
    