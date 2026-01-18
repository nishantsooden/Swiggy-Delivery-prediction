Swiggy Delivery Time Prediction
Overview

This project focuses on predicting food delivery time for Swiggy orders using machine learning techniques.
The objective is to estimate the expected delivery duration based on factors such as distance, order details, and delivery conditions.

Accurate delivery time prediction helps improve customer experience and operational efficiency in food delivery platforms.

Problem Statement

Food delivery platforms require reliable delivery time estimates to manage customer expectations and optimize logistics.
This project aims to build a predictive model that estimates delivery time using historical order and delivery data.

Key Features

Data preprocessing and feature engineering

Exploratory data analysis (EDA)

Machine learning model training and evaluation

Performance measurement using regression metrics

Technologies Used

Programming Language: Python

Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn

Development Environment: Jupyter Notebook

Project Structure
swiggy-delivery-time-prediction/
│── README.md
│── requirements.txt
│── swiggy_delivery_time.ipynb
│── data/
│   └── swiggy_data.csv
└── models/

Approach

Data loading and cleaning

Handling missing values and outliers

Feature selection and transformation

Model training using regression algorithms

Model evaluation and comparison

Model Evaluation

The model performance is evaluated using:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

(Results may vary depending on the dataset and model used)

Results

The trained model demonstrates reasonable accuracy in predicting delivery time and provides insights into key factors influencing delivery duration, such as distance and order complexity.

Future Improvements

Incorporate real-time traffic and weather data

Experiment with advanced models such as XGBoost or Random Forest

Deploy the model using a web application or API

Author

Nishant
GitHub: https://github.com/nishantsooden