# -*- coding: utf-8 -*-

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.models import load_model
# from tensorflow.keras.applications.resnet50 import preprocess_input

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
# MODEL_PATH ='./model.h5'

# Load your trained model
model = load_model('./Monkey-Classifictaion_model.h5')


def model_predict(img_path, model):
    print(img_path)
    img = tf.keras.utils.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = tf.keras.utils.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
   

# Be careful how your trained model deals with the input
# otherwise, it won't make correct prediction!
   # x = preprocess_input(x)
    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds == 0:
        preds = "mantled_howler"
    elif preds == 1:
        preds = "patas_monkey"
    elif preds == 2:
        preds = "bald_uakari"
    elif preds == 3:
        preds = "japanese_macaque"
    elif preds == 4:
        preds = "pygmy_marmoset"
    elif preds == 5:
        preds = "white_headed_capuchin"
    elif preds == 6:
        preds = "silvery_marmoset"
    elif preds == 7:
        preds = "common_squirrel_monkey"
    elif preds == 8:
        preds = "black_headed_night_monkey"
    elif preds == 9:
        preds = "nilgiri_langur"

    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(
            basepath, './uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
