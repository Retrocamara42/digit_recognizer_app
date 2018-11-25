#digit recognizer app
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from tensorflow.python import keras
from keras.models import Sequential, model_from_json

# Loading the model
print("Abriendo modelo")
json_file = open('./model/model_digit.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

model.load_weights("./model/model_digit.h5")

print("Compilando...")
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='adam',
              metrics=['accuracy'])

# Loading data input
img_rows, img_cols = 28, 28
num_classes = 10

image = plt.imread('./input/dos.png')

# Showing some predictions
print("Predicciones")
plt.imshow(image)
plt.show()
image = image.reshape(1, img_rows, img_cols, 4)
input = image[:,:,:,3].reshape(1,img_rows,img_cols,1)
plt.imshow(image[0,:,:,3])
plt.show()
pred = model.predict(input)
num=np.where(pred[0]==max(pred[0]))[0][0]
print("El numero es: %d" %num)
