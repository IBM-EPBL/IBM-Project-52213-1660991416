# -*- coding: utf-8 -*-
"""The Convolution  layer

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-V9QEjOV39FmhbXJ5hyz7bkkuEC43n52

# ** BM Project Name: Real-Time Communication System Powered by AI for Specially Abled**
# **# TEAM ID:PNT2022TMID33509**
  
  **Model Building**

**Import The Required Model Building Libraries **
"""

#import imagedatagenerator
from keras.preprocessing.image import ImageDataGenerator

#training datagen
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

#testing datagen
test_datagen=ImageDataGenerator(rescale=1./255)

"""**IMPORTING tensorflow**"""

import tensorflow as tf
import os

"""**Initialize The Model**"""

#create model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Flatten 
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import numpy as np
import matplotlib.pyplot as plt #to view graph in colab itself
import IPython.display as display
from PIL import Image
import pathlib

"""**Unzipping the dataset**"""

!unzip '/content/conversation engine for deaf and dumb (1).zip'