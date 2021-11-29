import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from tensorflow.keras.models import model_from_json
import numpy as np
import shutil

import os # inbuilt module
import random # inbuilt module
import webbrowser # inbuilt module




st.sidebar.title("What to do")
app_mode = st.sidebar.selectbox("Choose the app mode",
    ["Training", "Testing"])
if app_mode == "Training":
    st.write('yo')
elif app_mode == "Testing":
    #=================================== Title ===============================
    st.title("""
    Cat 🐱 Or Dog 🐶 Recognizer
    	""")
    
    
    #========================== File Uploader ===================================
    img_file_buffer = st.file_uploader("Upload an image here 👇🏻")
    
    try:
    	image = Image.open(img_file_buffer)
    	img_array = np.array(image)
    	if image is not None:
    	    st.image(
    	        image,
    	        use_column_width=True
    	    )
    except:
    	st.write("""
    		### ❗ Any Picture hasn't selected yet!!!
    		""")
    
    #================================= Predict Button ============================
    st.text("""""")
    submit = st.button("👉🏼 Predict")
    
    #==================================== Model ==================================
    def processing(testing_image_path):
        IMG_SIZE = 50
        img = load_img(testing_image_path, 
                target_size=(IMG_SIZE, IMG_SIZE), color_mode="grayscale")
        img_array = img_to_array(img)
        img_array = img_array/255.0
        img_array = img_array.reshape((1, 50, 50, 1))   
        prediction =loaded_model.predict(img_array)    
        return prediction
    
    def generate_result(prediction):
    	st.write("""
    	## 🎯 RESULT
    		""")
    	if prediction[0]<0.5:
    	    st.write("""
    	    	## Model predicts it as an image of a CAT 🐱!!!
    	    	""")
    	else:
    	    st.write("""
    	    	## Model predicts it as an image of a DOG 🐶!!!
    	    	""")
    
    #=========================== Predict Button Clicked ==========================
    if submit:
    	try:
    		# save image on that directory
    		save_img("temp_dir/test_image.png", img_array)
    
    		image_path = "temp_dir/test_image.png"
    		# Predicting
    		st.write("👁️ Predicting...")
    
    		model_path_h5 = "model/model.h5"
    		model_path_json = "model/model.json"
    		json_file = open(model_path_json, 'r')
    		loaded_model_json = json_file.read()
    		json_file.close()
    		loaded_model = model_from_json(loaded_model_json)
    		loaded_model.load_weights(model_path_h5)
    
    		loaded_model.compile(loss='binary_crossentropy', metrics=['accuracy'],optimizer='adam')
    
    		prediction = processing(image_path)
    
    		generate_result(prediction)
    
    	except:
    		st.write("""
    		### ❗ Oops... Something Is Going Wrong
    			""")
    
    #=============================== Copy Right ==============================
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
