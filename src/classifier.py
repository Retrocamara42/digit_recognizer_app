# Classifier for predicting a number in a 28x28 Image

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.python import keras
from keras.models import Sequential, model_from_json


class DigitRecognizer(object):

    def __init__(self):
        self.img_rows, self.img_cols = 28, 28
        self.model = None

    def load_model(self):
        # Loading the model and compiling it
        print("Loading the model...")
        json_file = open('./model/model_digit.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights("./model/model_digit.h5")

        print("Compiling...")
        self.model.compile(
                    loss=keras.losses.categorical_crossentropy,
                    optimizer='adam',
                    metrics=['accuracy'])

    def predicting(self):
        # Loading data input
        image = plt.imread('./input/input.jpg')
        # Predicting
        print("Predicting...")
        #plt.imshow(image)
        #plt.show()
        image = image.reshape(1, self.img_rows, self.img_cols, 3)
        layerBW = image[:,:,:,2][0]
        layerBW = 1-(layerBW/255)
        input=layerBW.reshape(1,self.img_rows,self.img_cols,1)
        #plt.imshow(layerBW)
        #plt.show()
        pred = self.model.predict(input)
        num=np.where(pred[0]==max(pred[0]))[0][0]
        print("The number is: %d" %num)
        print("************************")
