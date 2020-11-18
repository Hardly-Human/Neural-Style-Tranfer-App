import streamlit as st
from PIL import Image


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




if __name__== "__main__":
  main()