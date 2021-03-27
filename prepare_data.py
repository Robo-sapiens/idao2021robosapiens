#!/usr/bin/python3

import os
import copy
import shutil
from tqdm import tqdm
import re

## Paths

data_root = os.path.join(os.getcwd(), 'idao_dataset', 'train')
train_dir = os.path.join(os.getcwd(), 'tmp', 'train')
val_dir = os.path.join(os.getcwd(), 'tmp', 'val')

## Classes

classes_folders = ['ER', 'NR']

target_classes = [
    'ER_1',
    'ER_3',
    'ER_6',
    'ER_10',
    'ER_20',
    'ER_30',
    'NR_1',
    'NR_3',
    'NR_6',
    'NR_10',
    'NR_20',
    'NR_30',
]

## Make dirs

for dir_name in [train_dir, val_dir]:
    for class_name in target_classes:
        os.makedirs(os.path.join(dir_name, class_name), exist_ok=True)

def parse_class_from_filename(filename):
    match = re.search(r'(E|N)+R_\d+', filename)
    return match[0]

def parse_angle_from_filename(filename):
    match = re.search(r'-*[\d.]+', filename)
    return match[0]

## Copy files

for folder_name in classes_folders:
    source_dir = os.path.join(data_root, folder_name)
    for i, filename in enumerate(tqdm(os.listdir(source_dir))):
        if i % 6 != 0:
            dest_dir = os.path.join(train_dir)
        else:
            dest_dir = os.path.join(val_dir)
        shutil.copy(
            os.path.join(source_dir, filename),
            os.path.join(dest_dir, parse_class_from_filename(filename))
        )
