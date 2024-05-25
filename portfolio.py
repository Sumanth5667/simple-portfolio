import streamlit as st
from PIL import Image

# Set the page title and icon
st.set_page_config(page_title="My Portfolio", page_icon=":trophy:", layout="wide")



# Add a title and introduction
st.title("Welcome to My Portfolio")
st.divider()
# About Me section
st.header("About Me")
st.write("""
Enthusiastic data scientist eager to contribute to team success through hard work, attention to detail, and excellent organizational skills. Clear understanding of machine learning, deep learning, computer vision, data visualization and analysis, and training in natural language processing. Motivated to learn, grow, and excel in the data science field.
Microsoft azure fundamentals certified 1X and Microsoft Data Fundamentals certified 1X.
""")
st.image("mypic.jpeg", caption="Sumanth Nimmagadda", width=300, output_format='JPEG')

st.divider()

# Projects section
st.header("Projects")

# Project 1: DERM DETECT SKIN CANCER CLASSIFIER
st.subheader("Project 1: DERM DETECT SKIN CANCER CLASSIFIER")
st.write("""
**Website Link:** [DERM DETECT](https://dermdetect-skincancerclassifier.streamlit.app/)

Derm detect is a skin cancer classifier where it classifies skin lesions of 7 types: Actinic keratosis, Basal cell carcinoma, Benign keratosis, Dermatofibroma, Melanoma, Nevus, Vascular lesion.
- **Data Augmentation:** Generated 39,785+ images using the HAM10000 dataset.
- **Models Trained:** Xception, Mobilenet, Inception, VGG16 & 19, Resnet, EfficientNet B4 to B7, Nasnet.
- **Techniques Used:** Applied class weighting to improve results and overcome imbalance in the image dataset.
- **Results:** Captured sensitive and relatable patterns from the dataset using the Inception v3 model.
- **Deployment:** Deployed using Streamlit to enhance user feasibility.
""")
col1, col2 = st.columns(2)
with col1:
    st.image("img1.png", caption="Inception v3 Model Results", width=300)
with col2:
    st.image("img2.png", caption="Data Augmentation Examples", width=300)
st.divider()
# Project 2: BGREMOVER2024
st.subheader("Project 2: BGREMOVER2024")
st.write("""
**Website Link:** [BGREMOVER2024](https://bgremover2024.streamlit.app/)

BGREMOVER2024 is a lightweight web application developed using Python. It uses the `rembg` library to decrease latency compared to previous methodologies. The application is deployed using Streamlit.
""")
st.image("rembg2.png", caption="BGREMOVER2024", width=400)

st.divider()
# Project 3: Fire Weather Index Predictor
st.subheader("Project 3: Fire Weather Index Predictor")
st.write("""
**Duration:** 2023/08 - 2023/09

The challenge in increasing the accuracy used multiple trial and error methods on data such as feature selection, feature transformation on the data set. At the same time, made the model unbiased for prediction.
- Finally developed a web application using Flask framework which takes the input from the user and predicts the output as FWI Index.
""")
st.divider()

# Skills section
st.header("Skills")

# Use columns to display skills side by side
col1, col2 = st.columns(2)

# Skills - Left Column
with col1:
    st.write("""
    - Machine Learning (Advanced)
    - Deep Learning (Advanced)
    - Computer Vision (Intermediate)
    - NLP (Beginner)
    - Data Visualization (Advanced)
    - Data Analysis (Advanced)
    """)

# Skills - Right Column
with col2:
    st.write("""
    - Statistics (Intermediate)
    - SQL (Advanced)
    - MongoDB (Beginner)
    - Power BI (Intermediate)
    - Predictive Modelling (Advanced)
    """)
st.divider()

st.header("Certifications")

# Add certifications with links
st.write("""
- Certification: [Microsoft Azure Data Fundamentals DP-900](https://www.credly.com/earner/earned/badge/ef2141b0-66be-4ada-9093-32258682d4e6)
- Certification: [Microsoft Azure Fundamentals AZ-900](https://www.credly.com/earner/earned/badge/9c172bed-7bf3-4c4d-8faa-14d78dd0a7d5)
""")

st.divider()
# Achievements section
st.header("Achievements")
st.write("""
- Kaggle competitions contributor, generated a dataset that has more than 29,000+ views and 6,000+ downloads.
- Ranked among top-100 in Digit Recognizer Competition.
""")
st.divider()
# Contact section
st.header("Contact Me")
st.write("""
Feel free to reach out to me through any of the following methods:
- Email: sumanthnimmagadda5667@gmail.com
- LinkedIn: [https://www.linkedin.com/in/sumanth-nimmagadda-472455221/]
- GitHub: [https://github.com/Sumanth5667/]
- Kaggle :[https://www.kaggle.com/sumanthnimmagadda]
- Mobile :[+91 8464887585]
""")
st.divider()
