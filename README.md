## BostonHousing
#Boston housing prices
Here is your complete `README.md` file as a single block. You can copy and save it in your `BostonHousing/` folder:



markdown
## Boston Housing Price Prediction App

This project is a complete machine learning pipeline to predict housing prices using the **Boston Housing Dataset**. It includes data preprocessing, model training, and deployment through a Streamlit web application hosted on Streamlit Cloud.


 Project Overview

- **Objective**: Predict the median value of owner-occupied homes (in $1000s).
- **Algorithm**: Random Forest Regressor (best performer)
- **Deployment**: Streamlit Cloud
- **Language**: Python  
- **Frameworks**: Streamlit, scikit-learn, pandas, etc.

## Dataset Info

* Source: [Scikit-learn Boston Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html)
* 13 Features including crime rate, number of rooms, distance to employment centers, etc.
* Target: `MEDV` (Median value of owner-occupied homes)

---

## Model Details

* Multiple algorithms were tested (Random Forest, Linear Regression)
* **Random Forest** gave the best results
* Trained using scikit-learn
* Model saved as `model.pkl` using `pickle`




##  Features

* User input for all 13 features
* Real-time house price prediction
* Simple, clean UI with sidebar input
* Fast model response using pre-trained Random Forest
* Fully cloud-hosted and free to access


##  How to Train the Model



2. Follow the steps for:

   * Loading data
   * EDA
   * Preprocessing
   * Training
   * Saving the model

##  Tech Stack

* Streamlit
* scikit-learn
* pandas
* matplotlib / seaborn
* Python 3.x

##  Author

Dilmi Imesha




