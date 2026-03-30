# MINI PROJECT REPORT

# SLEEP QUALITY PREDICTOR USING MACHINE LEARNING

---

## ABSTRACT

Sleep is a critical factor influencing human health, productivity, and mental well‑being. Poor sleep quality can result in stress, fatigue, reduced concentration, and long‑term health issues. This project presents a Machine Learning‑based Sleep Quality Predictor that analyzes user lifestyle parameters such as sleep duration, stress level, physical activity, heart rate, daily steps, screen exposure before bedtime, and exercise duration to predict sleep quality.

The developed system classifies sleep quality into three categories: Good, Average, and Poor. In addition to prediction, the system provides personalized suggestions for improving sleep habits and visualizes weekly sleep trends using an interactive dashboard. The application is implemented using Python and deployed as a web application using Streamlit for real‑time user interaction.

---

## 1. INTRODUCTION

Sleep plays a vital role in maintaining both physical and psychological health. Modern lifestyle habits such as excessive screen exposure, irregular routines, lack of exercise, and increased stress levels significantly affect sleep quality. Identifying these influencing factors and analyzing their impact can help individuals improve their overall well‑being.

This project introduces a Sleep Quality Predictor using Machine Learning techniques that evaluates lifestyle parameters and predicts the sleep condition of a user. The system also provides personalized suggestions to improve sleep quality and presents analytical insights through graphical visualization.

The application is designed as a user‑friendly interactive web platform where users can enter their daily lifestyle habits and receive instant feedback regarding their sleep condition.

---

## 2. OBJECTIVE OF THE PROJECT

The main objectives of the project are:

• To develop a Machine Learning model that predicts sleep quality.
• To analyze the impact of lifestyle habits on sleep patterns.
• To provide personalized recommendations for improving sleep health.
• To visualize sleep trends using graphical analysis.
• To deploy the model as an interactive web application using Streamlit.

---

## 3. PROBLEM STATEMENT

Sleep disorders and poor sleep quality are becoming increasingly common due to unhealthy lifestyle habits. Many individuals are unaware of how daily behaviors such as stress, reduced exercise, and excessive screen time affect their sleep quality.

The goal of this project is to build a predictive system that evaluates lifestyle parameters and determines sleep quality while also suggesting improvements for better sleep health.

---

## 4. SCOPE OF THE PROJECT

The Sleep Quality Predictor system focuses on analyzing lifestyle habits that influence sleep behavior and predicting sleep quality accordingly.

Scope of the project includes:

• Predicting sleep quality using Machine Learning
• Providing personalized health suggestions
• Displaying sleep score and habit quality rating
• Visualizing weekly sleep trends
• Deploying the application as a web‑based dashboard

Future scope includes:

• Integration with wearable fitness tracking devices
• Real‑time sleep monitoring system
• Mobile application deployment
• Deep learning‑based prediction models

---

## 5. SYSTEM REQUIREMENTS

### Hardware Requirements

• Processor: Intel i3 or higher
• RAM: Minimum 4GB
• Hard Disk: 500GB recommended

### Software Requirements

• Operating System: Windows 10 or above
• Programming Language: Python
• Development Tool: Visual Studio Code
• Libraries Used:

* Pandas
* NumPy
* Scikit‑learn
* Streamlit
* Matplotlib

---

## 6. TECHNOLOGIES USED

### Python

Python is used as the primary programming language for implementing Machine Learning algorithms and building the application logic.

### Machine Learning

Machine Learning techniques are used to analyze user lifestyle data and predict sleep quality.

### Random Forest Classifier

Random Forest Classifier is used as the prediction algorithm due to its high accuracy and ability to handle multiple input parameters effectively.

### Streamlit

Streamlit is used to build the interactive web interface for real‑time prediction and visualization.

### Pandas and NumPy

These libraries are used for dataset preprocessing, transformation, and numerical computation.

---

## 7. DATASET DESCRIPTION

The dataset used in this project contains lifestyle attributes that influence sleep quality. The major features used for prediction include:

• Sleep Duration
• Physical Activity Level
• Stress Level
• Daily Steps
• Heart Rate
• Screen Time Before Bed
• Exercise Minutes

These features are used to train the Machine Learning model for accurate prediction of sleep quality.

---

## 8. SYSTEM ARCHITECTURE

The architecture of the Sleep Quality Predictor system consists of the following steps:

User Input → Data Processing → Machine Learning Model → Prediction Output → Suggestion Engine → Visualization Dashboard

---

## 9. METHODOLOGY

The methodology followed in this project includes the following steps:

Step 1: Data Collection

Lifestyle dataset related to sleep behavior is collected.

Step 2: Data Preprocessing

The dataset is cleaned and prepared for training by removing inconsistencies and formatting input features.

Step 3: Model Training

Random Forest Classifier is trained using selected dataset features.

Step 4: Model Evaluation

Model performance is tested for prediction accuracy.

Step 5: Deployment

The trained model is deployed using Streamlit as a web application.

---

## 10. IMPLEMENTATION DETAILS

The implementation of the project includes:

• Loading dataset using Pandas
• Training Random Forest model using Scikit‑learn
• Saving trained model using Pickle
• Creating prediction module
• Designing interactive Streamlit interface
• Adding sleep score visualization
• Adding personalized suggestion engine
• Displaying weekly sleep trend chart
• Deploying the application online using Streamlit Cloud

---

## 11. RESULTS AND DISCUSSION

The Sleep Quality Predictor successfully analyzes user lifestyle parameters and predicts sleep quality in real time. The application provides multiple outputs including:

• Sleep quality classification
• Sleep score progress indicator
• Personalized suggestions
• Habit quality rating
• Weekly trend visualization

The deployed application enables users to interact with the system easily and understand the impact of their daily habits on sleep quality.

---

## 12. ADVANTAGES OF THE SYSTEM

Advantages of the system include:

• Interactive user interface
• Real‑time prediction capability
• Personalized improvement suggestions
• Graphical trend visualization
• Lightweight and fast execution
• Easy accessibility through web deployment

---

## 13. LIMITATIONS OF THE SYSTEM

Limitations of the system include:

• Prediction depends on dataset quality
• Limited number of input parameters
• Requires manual user input
• Cannot replace professional medical diagnosis

---

## 14. FUTURE ENHANCEMENTS

Future enhancements of the system include:

• Integration with wearable health monitoring devices
• Real‑time sensor‑based sleep tracking
• Mobile application development
• Deep learning model implementation
• Cloud database integration for long‑term tracking

---

## 15. CONCLUSION

The Sleep Quality Predictor demonstrates how Machine Learning techniques can be effectively used to analyze lifestyle habits and predict sleep quality. The system provides meaningful insights and personalized recommendations that help users improve their sleep behavior.

The interactive Streamlit‑based web application enhances usability and accessibility, making the solution practical for real‑world usage. This project highlights the importance of predictive analytics in health‑related applications and showcases the potential of Machine Learning in lifestyle improvement systems.

---

## 16. REFERENCES

• Python Documentation
• Scikit‑learn Documentation
• Streamlit Documentation
• Machine Learning Research Papers
• Kaggle Dataset Resources
