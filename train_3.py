#=====================================================================
# Function : train model_2
# Author : Yanyu Zhang
# Date : 10/04/2019
# Copyright 2019 Yanyu Zhang zhangya@bu.edu
#=====================================================================
from keras.preprocessing.image import ImageDataGenerator
from model_Sequential_2 import model_Sequential
from plot_loss_acc import plot_curve 

train_datagen = ImageDataGenerator(rescale=1./255,
                                  rotation_range=40,
                                  width_shift_range=0.2,
                                  height_shift_range=0.2,
                                  shear_range=0.2,
                                  zoom_range=0.2,
                                  horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory('train',
                                                   target_size=(150,150),
                                                   batch_size=32,
                                                   class_mode='binary')
validation_generator = test_datagen.flow_from_directory('validation',
                                                       target_size=(150,150),
                                                       batch_size=32,
                                                       class_mode='binary')
model = model_Sequential()
history = model.fit_generator(train_generator,
                             steps_per_epoch=25,
                             epochs=100,
                             validation_data = validation_generator,
                             validation_steps=13)
model.save('poles_and_nonpoles_2.h5')

plot_curve(history)
