#!/usr/bin/python3

import os
import copy
import shutil
from tqdm import tqdm

## Paths

data_root = os.path.join(os.getcwd(), 'idao_dataset', 'train')
train_dir = os.path.join(os.getcwd(), 'tmp', 'train')
val_dir = os.path.join(os.getcwd(), 'tmp', 'val')

## Classes

classes = ['ER', 'NR']

## Make dirs

for dir_name in [train_dir, val_dir]:
    for class_name in classes:
        os.makedirs(os.path.join(dir_name, class_name), exist_ok=True)

## Copy files

for class_name in classes:
    source_dir = os.path.join(data_root, class_name)
    for i, file_name in enumerate(tqdm(os.listdir(source_dir))):
        if i % 6 != 0:
            dest_dir = os.path.join(train_dir)
        else:
            dest_dir = os.path.join(val_dir)
        shutil.copy(
            os.path.join(source_dir, file_name),
            os.path.join(dest_dir, class_name)
        )
