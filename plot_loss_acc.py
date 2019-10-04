#=====================================================================
# Function : Plot loss and accuracy
# Author : Yanyu Zhang
# Date : 10/04/2019
# Copyright 2019 Yanyu Zhang zhangya@bu.edu
#=====================================================================

import matplotlib.pyplot as plt

def plot_curve(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    epochs = range(1,len(acc)+1)
    
    plt.plot(epochs,acc,'bo',label='Training acc')
    plt.plot(epochs,val_acc,'b',label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.savefig("acc.png", dpi = 300)
    
    plt.figure()
    plt.plot(epochs,loss,'bo',label='Training loss')
    plt.plot(epochs,val_loss,'b',label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    
    plt.savefig("loss.png", dpi = 300)