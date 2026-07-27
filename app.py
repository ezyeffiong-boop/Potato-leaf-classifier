
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import gdown

# Model file name
MODEL_PATH = "potato_leaf_classifier.keras"

# Download model from Google Drive if it doesn't exist
if not os.path.exists(MODEL_PATH):
    gdown.download(
            url="https://drive.google.com/uc?id=12kI2BxRjwXb0sNryp58X5Z8MQeuULDdu",
                    output=MODEL_PATH,
                            quiet=False)
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels (must match the training order)
CLASS_NAMES = ["Other", "potato_healthy", "potato_late_blight"]

# Streamlit page configuration
st.set_page_config(page_title="Potato Leaf Disease Classifier")

# App title
st.title("🥔 Potato Leaf Disease Classifier")
st.write(
    "Upload an image of a potato leaf to determine whether it is Healthy, "
        "affected by Late Blight, or not a potato leaf.")
uploaded_file = st.file_uploader(
      "Choose an image",
          type=["jpg", "jpeg", "png"]
          )
if uploaded_file is not None:
  image = Image.open(uploaded_file).convert("RGB")

  st.image(image, caption="Uploaded Image", use_container_width=True)
  image = image.resize((224, 224))
  img_array = np.array(image) / 255.0
  img_array = np.expand_dims(img_array, axis=0)

              # Make prediction
  prediction = model.predict(img_array)
  predicted_class = np.argmax(prediction)
  confidence = np.max(prediction) * 100

  st.write(f"### Confidence: {confidence:.2f}%")
  if CLASS_NAMES[predicted_class] == "potato_healthy":
    st.success("✅ Healthy Potato Leaf")

  elif CLASS_NAMES[predicted_class] == "potato_late_blight":
    st.error("🍂 Potato Late Blight Detected")

  else:
    st.warning("⚠️ Neither Healthy Potato nor Potato Late Blight (Not a Potato Leaf)")
