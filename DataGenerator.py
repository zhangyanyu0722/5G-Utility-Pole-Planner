#=====================================================================
# Function : Using keras ImageDataGenerator define the model
# Author : Yanyu Zhang
# Date : 10/04/2019
# Copyright 2019 Yanyu Zhang zhangya@bu.edu
#=====================================================================
from keras.preprocessing.image import ImageDataGenerator
from keras import models


def DataGenerator(model, in_epochs):
  train_datagen = ImageDataGenerator(rescale=1./255)
  test_datagen = ImageDataGenerator(rescale=1./255)

  train_generator = train_datagen.flow_from_directory('train',
                                                    target_size=(150,150),
                                                    batch_size=20,
                                                    class_mode='binary')
  
  validation_generator = test_datagen.flow_from_directory('validation',
                                                        target_size=(150,150),
                                                         batch_size=20,
                                                        class_mode='binary')

  history = model.fit_generator(train_generator,
                              steps_per_epoch=50,
                               epochs=in_epochs,
                               validation_data=validation_generator,
                               validation_steps=25)

  model.save('poles_and_nonpoles.h5')
  return history