import streamlit as st 
import pytesseract 
from PIL import Image
 
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
st.title("OPTICAL CHARACTER RECOGNITION (OCR)")
st.text("Upload an image to extract text!")

uploaded_file = st.sidebar.file_uploader("Choose an image",type = ["jpg","png","jpeg"])
if uploaded_file is not None:
  img = Image.open(uploaded_file)
  st.image(img, caption = 'Uploaded Image',use_column_width = True) 
  st.write("")
  
  if st.button('PREDICT'):
    st.write("RESULT:")
    output = pytesseract.image_to_string(img)
    st.write(output)
