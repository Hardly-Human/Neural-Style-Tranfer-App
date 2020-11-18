import streamlit as st
from PIL import Image
import requests
import base64
import os


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">[ Download Image ]</a>'
    return href



################################################################################
# main()
################################################################################

def main():
  
  st.title("Neural Style Transfer App")
  st.text("Built with Style_Transfer-API and Streamlit")
  st.markdown("### [![Open Source Love svg1](https://aleen42.github.io/badges/src/github.svg)](https://github.com/Hardly-Human/Image-Colorization-App)\
  `            `[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://lbesson.mit-license.org/) \
  `            `[Get Style Images](https://unsplash.com/s/photos/paint-texture)")


  col1, col2 = st.beta_columns(2)

  col1.title("Original Image")
  image_file = col1.file_uploader("Upload Original Image", type = ['jpg','png','jpeg'])
  if image_file is None:
    col1.warning("Upload Original Image here")
  
  if image_file is not None:
    image1 = Image.open(image_file)
    rgb_im = image1.convert('RGB') 
    rgb_im.save("saved_image.jpg")
    image_path = "saved_image.jpg"
    col1.image(image1, use_column_width=True)
  

  col2.title("Style Image")
  style_file = col2.file_uploader("Upload Style Image", type = ['jpg','png','jpeg'])
  if style_file is None:
    col2.warning("Upload Style Image here")

  if style_file is not None:
    image2 = Image.open(style_file)
    rgb_im = image2.convert('RGB') 
    rgb_im.save("style_image.jpg")
    style_path = "style_image.jpg"
    col2.image(image2, use_column_width=True)

  if st.button("Transfer Style"):
    if image_file is not None:
      st.warning("Please Wait⌛...")
      r = requests.post(
      "https://api.deepai.org/api/fast-style-transfer",
      files={
          'content': open('saved_image.jpg', 'rb'),
          'style': open('style_image.jpg', 'rb'),
      },
      headers={'api-key': 'aa48ee59-f392-4783-b1ac-ab410534ca61'}
    )

      color_image_url = r.json()["output_url"]

      img_data = requests.get(color_image_url).content
      with open('color_image.jpg', 'wb') as handler:
        handler.write(img_data)
      st.success("Style Transfer Succesfull..🤟")
      color_image = Image.open('color_image.jpg')

      st.subheader("Processed Image")
      st.image(color_image)

      st.markdown(get_binary_file_downloader_html('color_image.jpg', 'Picture'), unsafe_allow_html=True)

    else:
      st.error("Please Upload Images!!!")


if __name__== "__main__":
  main()