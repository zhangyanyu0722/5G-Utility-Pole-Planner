#=====================================================================
# Function : Define CNN
# Author : Yanyu Zhang
# Date : 10/04/2019
# Copyright 2019 Yanyu Zhang zhangya@bu.edu
#=====================================================================
from keras import layers
from keras import models
from keras import optimizers

def model_Sequential():
  model = models.Sequential()
  model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))
  model.add(layers.MaxPool2D(2,2))
  model.add(layers.Conv2D(64,(3,3),activation='relu'))
  model.add(layers.MaxPool2D(2,2))
  model.add(layers.Conv2D(128,(3,3),activation='relu'))
  model.add(layers.MaxPool2D(2,2))
  model.add(layers.Conv2D(128,(3,3),activation='relu'))
  model.add(layers.MaxPool2D(2,2))
  model.add(layers.Flatten())
  model.add(layers.Dense(512,activation='relu'))
  model.add(layers.Dense(1,activation='sigmoid'))

  model.compile(loss='binary_crossentropy',
                optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])
  return model


