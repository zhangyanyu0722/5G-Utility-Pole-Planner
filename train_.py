#=====================================================================
# Function : train model
# Author : Yanyu Zhang
# Date : 10/04/2019
# Copyright 2019 Yanyu Zhang zhangya@bu.edu
#=====================================================================
from plot_loss_acc import plot_curve 
from model_Sequential import model_Sequential
from DataGenerator import DataGenerator

epochs = int(30)
model = model_Sequential()
history = DataGenerator(model, epochs)
plot_curve(history)