import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Interface of Image Classification')



import os                   # used for folder
from skimage.io import imread      # use for reading as image         
from skimage.transform import resize      # Resizing an image
import pickle

st.text('Plz Uplaod image') 

model=pickle.load(open('img_model.p','rb'))

uploaded_file =st.file_uploader('Choose an image....' , type="jpg")

if uploaded_file is not None:
  img=Image.open(uploaded_file)
  st.image(img,caption='Uploaded Image')
  
  # predict
  
  if st.button('Predict'):
    CATEGORIES=['rugby ball leather','ice cream cone','sunflower']
    st.write("Result ...")
    flatten_data=[]
    img =np.array(img)
    img_resized=resize(img,(150,150,3))

    flatten_data.append(img_resized.flatten())
    flatten_data =np.array(flatten_data)
    
    y_out=model.predict(flatten_data)
    y_out =CATEGORIES(y_out[0])
    st.title(f'Predicted output : {y_out}')
    
    
      # percentage

    q=model.predict_proba(flatten_data)
    for index,item in enumerate(CATEGORIES):
      st.write(f' {item} : {q[0][index]*100}%') 
