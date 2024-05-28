import streamlit as st
from PIL import Image
import webbrowser

# Set the page title and icon
st.set_page_config(page_title="My Portfolio", page_icon=":trophy:")
def open_url(url):
    webbrowser.open_new_tab(url)
st.sidebar.title("SUMANTH NIMMAGADDA")
st.sidebar.write("**Email:** sumanthnimmagadda5667@gmail.com")
st.sidebar.write("**Mobile:** +91 8464887585")
st.sidebar.divider()
# Add buttons for links in the sidebar
st.sidebar.write('Connect with me on LinkedIn')
if st.sidebar.button('LinkedIn'):
    open_url("https://www.linkedin.com/in/sumanth-nimmagadda-472455221/")
st.sidebar.divider()
st.sidebar.write('My Git hub account')
if st.sidebar.button('GitHub'):
    open_url("https://github.com/Sumanth5667/")
st.sidebar.divider()
st.sidebar.write('My kaggle account')
if st.sidebar.button('Kaggle'):
    open_url("https://www.kaggle.com/sumanthnimmagadda")



# Add a title and introduction
st.title("Welcome to My Portfolio")
st.divider()
# About Me section
st.header("About Me")
st.write("""
Enthusiastic data scientist eager to contribute to team success through hard work, attention to detail, and excellent organizational skills. Clear understanding of machine learning, deep learning, computer vision, data visualization and analysis, and training in natural language processing. Motivated to learn, grow, and excel in the data science field.
Microsoft azure fundamentals certified 1X and Microsoft Data Fundamentals certified 1X.
""")
st.image("images/mypic.jpeg", caption="Sumanth Nimmagadda", width=300, output_format='JPEG')

st.divider()

# Projects section
st.header("Projects")

st.subheader("Project 1: STREAMLYTICS-ML FOR PEOPLE")
st.write("""
**Website Link:** [STREAMLYTICS](https://streamlytics-mlforpeople.streamlit.app/)

- <u>**STREAMLYTIICS**</u>: Streamlined ML FOR EVERY ONE. An intuitive web app for seamless machine learning model training. It simplifies dataset uploading,
preprocessing, visualization, model selection,
hyperparameter tuning, and evaluation. Whether you're a
beginner or an expert, AutoML Trainer provides a smooth
journey from data exploration to model training.
- <u>**FEATURES**</u>:
- Data Visualization: Explore data insights with correlation
heatmaps, pairplots, distribution plots, and more.
- Model Selection: Choose from classification, regression,
and clustering models tailored to your problem.
- Hyperparameter Tuning: Fine-tune model
hyperparameters for optimal performance.
- Model Training and Evaluation: Train models with a click
and evaluate performance using various metrics.
- <u>**Supported Models**</u>:
- *Classification*: Logistic Regression, Random Forest
Classifier
- *Regression*: Linear Regression, Ridge Regression, Lasso
Regression, ElasticNet Regression, Random Forest
Regressor
- *Clustering* : KMeans Clustering
""", unsafe_allow_html=True)

# Create columns for images
col1, col2 = st.columns(2)

with col1:
    st.image("images/stream1.jpg", caption="Web Ui", width=400)
with col2:
    st.image("images/stream2.jpg", caption="Results after prediction", width=400)

# Divider between sections
st.divider()

# Underlined text
st.markdown("<u>This is underlined text</u>", unsafe_allow_html=True)

# Additional content if needed
st.write("Here is some additional text or content below the underlined text.")


# Project 1: DERM DETECT SKIN CANCER CLASSIFIER
st.subheader("Project 2: DERM DETECT SKIN CANCER CLASSIFIER")
st.write("""
**Website Link:** [DERM DETECT](https://dermdetect-skincancerclassifier.streamlit.app/)

Derm detect is a skin cancer classifier where it classifies skin lesions of 7 types: Actinic keratosis, Basal cell carcinoma, Benign keratosis, Dermatofibroma, Melanoma, Nevus, Vascular lesion.
- **Data Augmentation:** Generated 39,785+ images using the HAM10000 dataset.
- **Models Trained:** Xception, Mobilenet, Inception, VGG16 & 19, Resnet, EfficientNet B4 to B7, Nasnet.
- **Techniques Used:** Applied class weighting to improve results and overcome imbalance in the image dataset.
- **Results:** Captured sensitive and relatable patterns from the dataset using the Inception v3 model.
- **Deployment:** Deployed using Streamlit to enhance user feasibility.
""")
# Create columns for images
col1, col2 = st.columns(2)
with col1:
    st.image("images/img1-fRyLnblzu-transformed.png", caption="Web Ui for classifier", width=500)
with col2:
    st.image("images/pixelcut-export.png", caption="Results after prediction", width=500)
st.divider()
# Project 2: BGREMOVER2024
st.subheader("Project 3: BGREMOVER2024")
st.write("""
**Website Link:** [BGREMOVER2024](https://bgremover2024.streamlit.app/)

- BGREMOVER2024 is a lightweight web application developed using Python. It uses the `rembg` library
- Decreased latency compared to previous methodologies. The application is deployed using Streamlit.
""")
# Create columns for images
col1, col2 = st.columns(2)

with col1:
    st.image("images/bg-remover1.jpg", caption="Before removing background", width=500)
with col2:
    st.image("images/bgremover2.jpg", caption="Results after removing bg", width=500)

st.divider()
# Project 3: Fire Weather Index Predictor
st.subheader("Project 4: Fire Weather Index Predictor")
st.write("""
**Duration:** 2023/08 - 2023/09

- The challenge in increasing the accuracy used multiple trial and error methods on data such as feature selection, feature transformation on the data set. At the same time, made the model unbiased for prediction.
-  Finally developed a web application using Flask framework which takes the input from the user and predicts the output as FWI Index.
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
