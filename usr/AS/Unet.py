# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 09:39:49 2018

@author: Ayush Shirsat
"""
import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")


from tqdm import tqdm_notebook, tnrange
from itertools import chain
from skimage.io import imread, imshow, concatenate_images
from skimage.transform import resize
from skimage.morphology import label
from sklearn.model_selection import train_test_split

import tensorflow as tf
from PIL import Image
import cv2

from keras.models import Model, load_model
from keras.layers import Input, BatchNormalization, Activation, Dense, Dropout
from keras.layers.core import Lambda, RepeatVector, Reshape
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.pooling import MaxPooling2D, GlobalMaxPool2D
from keras.layers.merge import concatenate, add
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.optimizers import Adam, SGD
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

im_height = 128
im_width = 128
border = 5
img_channels = 1

path_img = 'C:/Users/Ayush Shirsat/Desktop/Proj/test_unet/image_re/'
path_mask = 'C:/Users/Ayush Shirsat/Desktop/Proj/test_unet/label_re/'

listing_img = sorted(os.listdir(path_img)) 
img_samples = len(listing_img)
print("Number of images: ",img_samples)

listing_mask = sorted(os.listdir(path_mask)) 
mask_samples = len(listing_mask)
print("Number of masks: ",mask_samples)

X = np.zeros((img_samples, im_height, im_width, 1), dtype=np.float32)
Y = np.zeros((mask_samples, im_height, im_width, 1), dtype=np.uint8)
print('Getting and resizing images ... ')

# Load images
for n,img in enumerate(listing_img):
    img = cv2.imread(path_img + img, 0)
    x_img = img_to_array(img, dtype=np.uint8)
    x_img = resize(x_img, (128, 128, 1))
    X[n, ..., 0] = x_img.squeeze() / 255

# Load masks
for n,mask in enumerate(listing_mask):
    mask = cv2.imread(path_mask + mask, 0)
    ret,mask = cv2.threshold(mask,100,255,cv2.THRESH_BINARY)
    mask = img_to_array(mask) / 255
    mask = resize(mask, (128, 128, 1))
    Y[n] = mask
    
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)
       
def conv2d_block(input_tensor, n_filters, kernel_size=3, batchnorm=True):
    # first layer
    x = Conv2D(filters=n_filters, kernel_size=(kernel_size, kernel_size), kernel_initializer="he_normal",
               padding="same")(input_tensor)
    if batchnorm:
        x = BatchNormalization()(x)
    x = Activation("relu")(x)
    # second layer
    x = Conv2D(filters=n_filters, kernel_size=(kernel_size, kernel_size), kernel_initializer="he_normal",
               padding="same")(x)
    if batchnorm:
        x = BatchNormalization()(x)
    x = Activation("relu")(x)
    return x

def get_unet(input_img, n_filters=16, dropout=0.5, batchnorm=True):
    # contracting path
    c1 = conv2d_block(input_img, n_filters=n_filters*1, kernel_size=3, batchnorm=batchnorm)
    p1 = MaxPooling2D((2, 2)) (c1)
    p1 = Dropout(dropout*0.5)(p1)

    c2 = conv2d_block(p1, n_filters=n_filters*2, kernel_size=3, batchnorm=batchnorm)
    p2 = MaxPooling2D((2, 2)) (c2)
    p2 = Dropout(dropout)(p2)

    c3 = conv2d_block(p2, n_filters=n_filters*4, kernel_size=3, batchnorm=batchnorm)
    p3 = MaxPooling2D((2, 2)) (c3)
    p3 = Dropout(dropout)(p3)

    c4 = conv2d_block(p3, n_filters=n_filters*8, kernel_size=3, batchnorm=batchnorm)
    p4 = MaxPooling2D(pool_size=(2, 2)) (c4)
    p4 = Dropout(dropout)(p4)
    
    c5 = conv2d_block(p4, n_filters=n_filters*16, kernel_size=3, batchnorm=batchnorm)
    
    # expansive path
    u6 = Conv2DTranspose(n_filters*8, (3, 3), strides=(2, 2), padding='same') (c5)
    u6 = concatenate([u6, c4])
    u6 = Dropout(dropout)(u6)
    c6 = conv2d_block(u6, n_filters=n_filters*8, kernel_size=3, batchnorm=batchnorm)

    u7 = Conv2DTranspose(n_filters*4, (3, 3), strides=(2, 2), padding='same') (c6)
    u7 = concatenate([u7, c3])
    u7 = Dropout(dropout)(u7)
    c7 = conv2d_block(u7, n_filters=n_filters*4, kernel_size=3, batchnorm=batchnorm)

    u8 = Conv2DTranspose(n_filters*2, (3, 3), strides=(2, 2), padding='same') (c7)
    u8 = concatenate([u8, c2])
    u8 = Dropout(dropout)(u8)
    c8 = conv2d_block(u8, n_filters=n_filters*2, kernel_size=3, batchnorm=batchnorm)

    u9 = Conv2DTranspose(n_filters*1, (3, 3), strides=(2, 2), padding='same') (c8)
    u9 = concatenate([u9, c1], axis=3)
    u9 = Dropout(dropout)(u9)
    c9 = conv2d_block(u9, n_filters=n_filters*1, kernel_size=3, batchnorm=batchnorm)
    
    outputs = Conv2D(1, (1, 1), activation='sigmoid') (c9)
    model = Model(inputs=[input_img], outputs=[outputs])
    return model

input_img = Input((im_height, im_width, 1), name='img')
model = get_unet(input_img, n_filters=16, dropout=0.05, batchnorm=True)

opt = SGD(lr = 0.05)
model.compile(optimizer=opt, loss="binary_crossentropy", metrics=["accuracy"])
#model.summary()

callbacks = [EarlyStopping(monitor='val_loss', patience=10)]

results = model.fit(X_train, Y_train, batch_size=32, epochs=250, callbacks=callbacks,validation_split = 0.2, shuffle = True)

train_loss = results.history['loss']
val_loss = results.history['val_loss'] 
train_acc = results.history['acc']
val_acc = results.history['val_acc']

plt.figure(figsize=(8, 8))
plt.title("Learning curve")
plt.plot(results.history["loss"], label="loss")
plt.plot(results.history["val_loss"], label="val_loss")
plt.plot( np.argmin(results.history["val_loss"]), np.min(results.history["val_loss"]), marker="x", color="r", label="best model")
plt.xlabel("Epochs")
plt.ylabel("loss")
plt.legend();

score = model.evaluate(X_test, Y_test, verbose=0) # accuracy check
print('Test accuracy:', score[1]) # Prints test accuracy

# Serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# Serialize weights to H5
model.save_weights("model.h5")
print("Saved model to disk")

# X_test and Y_test are saved so model can be tested 
np.save('X_test', X_test)
np.save('Y_test', Y_test)

y_pred = model.predict(X_test)
for key in range(10,20):
    check = y_pred[key] 
    check = check * 255
    check = np.round(check)    
    ret,check = cv2.threshold(check,80,255,cv2.THRESH_BINARY)
    #check = array_to_img(check)
    plt.figure()
    plt.imshow(check)
    #cv2.imshow('predicted_mask', check)
