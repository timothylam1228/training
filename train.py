import os
from tkinter import Image
import cv2
#use tensorflow to do image classification
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from PIL import Image

# #helper libraries
import numpy as np
# import matplotlib.pyplot as plt

# #load data
import pandas as pd
import csv

# #Load data
# def load_image( infilename ) :
#     img = Image.open( infilename )
#     img.load()
#     data = np.asarray( img, dtype="int32" )
#     return data

data = pd.read_csv('Passed.csv')

#split data into train and test


#make prediction
# predictions = model.predict(test_x

#main function

def create_dataset_PIL(img_folder):
    
    img_data_array=[]
    class_name=[]
    for file in os.listdir(os.path.join(img_folder)):
        image_path= os.path.join(img_folder,  file)
        image= np.array(Image.open(image_path))
        image = image.astype('float32')
        image /= 255  
        img_data_array.append(image)
    return img_data_array , class_name

def main():
    train = data.sample(frac=0.8,random_state=0)
    test = data.drop(train.index)

    #split data into x and y
    #get current directory
    ROOT = os.path.dirname(os.path.abspath(__file__))
    PIL_img_data, class_name=create_dataset_PIL(ROOT+'\\Passed-1')
    print(PIL_img_data)
    image_path = train.iloc[:,0]
    train_x = cv2.imread(image_path)
    train_y = train.iloc[:,1]
    test_x = test.iloc[:,0]
    test_y = test.iloc[:,1]

    #load image

    #start training
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

    model.fit(train_x, train_y, epochs=5)

    #test model
    test_loss, test_acc = model.evaluate(test_x, test_y)

    print('Test accuracy:', test_acc)


main()
# def readCSV():
#     with open('Passed.csv', 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             print(row)

# readCSV()