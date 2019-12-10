#=====================================================================
# Function : genarate more train files
# Author : Yanyu Zhang
# Date : 10/04/2019
# Copyright 2019 Yanyu Zhang zhangya@bu.edu
#=====================================================================
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(rotation_range=40, 
                            width_shift_range=0.2,
                            height_shift_range=0.2, 
                            shear_range=0.2, 
                            zoom_range=0.2, 
                            horizontal_flip=True,
                            fill_mode='nearest' 
                            )

from keras.preprocessing import image
import os
import matplotlib.pyplot as plt

base_dir = '/home/ece-student/Desktop/shared/5G'
train_dir = os.path.join(base_dir,'train')
train_poles_dir = os.path.join(train_dir,'poles')
fnames = [os.path.join(train_poles_dir,fname) for fname in os.listdir(train_poles_dir)]
img_path = fnames[5] 
img = image.load_img(img_path,target_size=(150,150)) 
x = image.img_to_array(img) 
x = x.reshape((1,)+x.shape) 
i = 0
for batch in datagen.flow(x,batch_size=1):
    plt.figure(i)
    imgplot = plt.imshow(image.array_to_img(batch[0]))
    i+=1
    if(i%4==0):
        break
