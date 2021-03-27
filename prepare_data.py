#!/usr/bin/python3

import os
import copy
import shutil
from tqdm import tqdm
from utils.parsing import parse_class_from_filename

## Paths

dataset_root = os.path.join(os.getcwd(), 'idao_dataset')

train_source = os.path.join(dataset_root, 'train')
public_test_source = os.path.join(dataset_root, 'public_test')
private_test_source = os.path.join(dataset_root, 'private_test')

tmp_dir = os.path.join(os.getcwd(), 'tmp')

train_dir = os.path.join(tmp_dir, 'train')
val_dir = os.path.join(tmp_dir, 'val')

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

## Copy files

# Classes
for folder_name in classes_folders:
    source_dir = os.path.join(train_source, folder_name)
    for i, filename in enumerate(tqdm(os.listdir(source_dir))):
        if i % 6 != 0:
            dest_dir = os.path.join(train_dir)
        else:
            dest_dir = os.path.join(val_dir)
        shutil.copy(
            os.path.join(source_dir, filename),
            os.path.join(dest_dir, parse_class_from_filename(filename))
        )

# Tests
shutil.copytree(public_test_source,
                    os.path.join(tmp_dir, 'test', 'unknown'),
                    dirs_exist_ok=False)

shutil.copytree(private_test_source,
                    os.path.join(tmp_dir, 'test', 'unknown'),
                    dirs_exist_ok=True)
