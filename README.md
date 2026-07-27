# 🥔 Potato Leaf Disease Classifier

## Overview
This project is a Convolutional Neural Network (CNN) application developed for the GET 324 Mini Project. It classifies uploaded images into one of three categories:

- Healthy Potato
- Potato Late Blight
- Other (Not a Potato Leaf)

The model was built using TensorFlow/Keras and deployed with Streamlit.

## Features
- Upload potato leaf images.
- Detect Healthy Potato leaves.
- Detect Potato Late Blight.
- Identify images that are not potato leaves.
- Display prediction confidence.

## Project Structure

```text
.
├── app.py
├── requirements.txt
└── README.md
```

## Technologies Used
- Python
- TensorFlow/Keras
- Streamlit
- NumPy
- Pillow
- gdown

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Model
The trained model is hosted on Google Drive and is downloaded automatically using **gdown** when the application starts.

## How to Use
1. Open the Streamlit application.
2. Upload a JPG, JPEG, or PNG image.
3. Wait for the prediction.
4. The application displays:
   - ✅ Healthy Potato Leaf
      - 🍂 Potato Late Blight
         - ⚠️ Neither Healthy Potato nor Potato Late Blight (Other)
         5. The confidence score is also displayed.

         ## Dataset
         The model was trained using potato leaf images belonging to three classes:
         - Other
         - Healthy Potato
         - Potato Late Blight

         ## Author
         **Ezekiel Effiong**

         Department of Agricultural and Biosystems Engineering

         University of Uyo

         GET 324 – Cloud Computing and AI Model Deployment for Engineering Applications
