#=====================================================================
# Function : divide data into train, validation and test
# Author : Yanyu Zhang
# Date : 10/04/2019
# Copyright 2019 Yanyu Zhang zhangya@bu.edu
#=====================================================================

import numpy as np 
import pandas as pd 
import os,shutil

# print(os.listdir("/home/ece-student/Desktop/shared/5G"))

base_dir = '/home/ece-student/Desktop/shared/5G'

train_dir = os.path.join(base_dir,'train')
os.mkdir(train_dir)

validation_dir = os.path.join(base_dir,'validation')
os.mkdir(validation_dir)

test_dir = os.path.join(base_dir,'test')
os.mkdir(test_dir)


train_poles_dir = os.path.join(train_dir,'poles')
os.mkdir(train_poles_dir)

train_nonpoles_dir = os.path.join(train_dir,'nonpoles')
os.mkdir(train_nonpoles_dir)


validation_poles_dir = os.path.join(validation_dir,'poles')
os.mkdir(validation_poles_dir)

validation_nonpoles_dir = os.path.join(validation_dir,'nonpoles')
os.mkdir(validation_nonpoles_dir)


test_poles_dir = os.path.join(test_dir,'poles')
os.mkdir(test_poles_dir)

test_nonpoles_dir = os.path.join(test_dir,'nonpoles')
os.mkdir(test_nonpoles_dir)


original_dataset_dir = 'poles'
original_dataset_dir_2 = 'nonpoles'

fnames = ['pole.{}.jpg'.format(i) for i in range(1,500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir,fname)
    dst = os.path.join(train_poles_dir,fname)
    shutil.copyfile(src,dst)

fnames = ['pole.{}.jpg'.format(i) for i in range(500,750)]
for fname in fnames:
    src = os.path.join(original_dataset_dir,fname)
    dst = os.path.join(validation_poles_dir,fname)
    shutil.copyfile(src,dst)

fnames = ['pole.{}.jpg'.format(i) for i in range(750,1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir,fname)
    dst = os.path.join(test_poles_dir,fname)
    shutil.copyfile(src,dst)
fnames = ['nonpole.{}.jpg'.format(i) for i in range(1,500)]

for fname in fnames:
    src = os.path.join(original_dataset_dir_2,fname)
    dst = os.path.join(train_nonpoles_dir,fname)
    shutil.copyfile(src,dst)

fnames = ['nonpole.{}.jpg'.format(i) for i in range(500,750)]
for fname in fnames:
    src = os.path.join(original_dataset_dir_2,fname)
    dst = os.path.join(validation_nonpoles_dir,fname)
    shutil.copyfile(src,dst)

fnames = ['nonpole.{}.jpg'.format(i) for i in range(750,1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir_2,fname)
    dst = os.path.join(test_nonpoles_dir,fname)
    shutil.copyfile(src,dst)

