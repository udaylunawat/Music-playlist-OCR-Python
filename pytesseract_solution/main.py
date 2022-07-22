
import os
import re
import cv2
from tqdm import tqdm
import pytesseract
import pandas
from itertools import groupby
from utilities import process_text

names, output_text = [], []
for image_name in tqdm(sorted(os.listdir('solo ss'))):
    img = cv2.imread(os.path.join('solo ss', image_name))
    x,y = 135, 208
    w,h = -70,-120
    img = img[y:h, x:w]
    raw_text = pytesseract.image_to_string(img, lang='eng')
    processed_text = process_text(raw_text)
    print(f'\nProcessing {image_name}...')

    names.append(os.path.splitext(image_name)[0])
    output_text.append(processed_text)

for file_name, text in zip(names, output_text):
    with open(os.path.join('texts', file_name+'.txt'), 'w') as f:
        f.write(text)
    f.close()