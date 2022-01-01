import streamlit as st
import io
import requests
import json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

st.title('顔認識アプリ')

subscription_key = 'a83a8206592f48969a51d1089e01d825'
assert subscription_key

face_api_url = 'https://papageno.cognitiveservices.azure.com/face/v1.0/detect'

uploaded_file = st.file_uploader("Choose an image...", type='jpg')

if uploaded_file is not None:
    img = Image.open(uploaded_file)

    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img = output.getvalue()  #バイナリ取得

    headers = {
        'Content-Type':'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    params = {
        'returnFaceId': 'true',
        'returnFaceAttributes': 'blur,exposure,noise,age,gender,facialhair,glasses,hair,makeup,accessories,occlusion,headpose,emotion,smile'
    }

    res = requests.post(face_api_url, params=params, headers=headers, data=binary_img)
    results = res.json()

    textcolor = (0, 255, 0)
    textsize = 100
    font = ImageFont.truetype("arial.ttf", size=textsize) 

    for result in results:
        rect = result['faceRectangle']
        gender = result['faceAttributes']['gender']
        age = result['faceAttributes']['age']
        text = str(gender) + ": " + str(int(age))
        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'],rect['top']),(rect['left']+rect['width'],rect['top']+rect['height'])], fill=None, outline='green', width=5)
        draw.text((rect['left'],rect['top']-200), text , font=font, fill=textcolor, align='center')
        
    st.image(img, caption='Uploaded Image.', use_column_width=True)
