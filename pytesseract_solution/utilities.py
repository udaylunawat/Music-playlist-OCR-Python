
import os
import re
import cv2
import pytesseract
import pandas
from itertools import groupby
from google.colab.patches import cv2_imshow

def remove_extra_rc(s):
    '''
    Removes extra return carriage
    '''
    re.sub(r'(\n\s*)+\n+', '\n\n', s)
    return s


def join_artist_songs(splitted):
    '''
    if two consecutive texts are seperated by \n, before and after, merge them

    e.g.
    """

    Choo lo

    Local Train

    """

    would return

    """
    Choo lo
    Local Train
    """
    '''
    for index, text in enumerate(splitted):
            try:
                if splitted[index+1] == '' and splitted[index-1] == '' \
                    and splitted[index+3] == '':
                    splitted.pop(index+1)
            except:
                continue
            
    return splitted


def remove_extra(splitted):
    if splitted[-1] == '\x0c':
        splitted = splitted[:-1]
    if splitted[-2] == '':
        splitted = splitted[:-2]
    if splitted[1] == '':
        splitted = splitted[2:]
    return splitted


def process_text(raw_text):
    '''
    - removing multiple whitespaces from text
    - splitting text by \n
    - replace | with I
    - removes x0c at end of text
    - merge artist and song that are seperated by \n in raw_text
    - remove if only artist at start, or only song at end, of raw_text 
    - removes extra return carriage from splitted text
    '''
    raw_text = ' '.join(raw_text.split(' '))
    splitted = raw_text.split('\n')
    splitted = list(map(lambda x:x.replace('|', 'I'), splitted))
    splitted = join_artist_songs(splitted)
    splitted = remove_extra_rc('\n'.join(splitted)).split('\n')
    splitted = remove_extra(splitted)
    splitted = list(filter(lambda x: x!=' ', splitted))
    splitted = [i[0] for i in groupby(splitted)]
    return '\n'.join(splitted)