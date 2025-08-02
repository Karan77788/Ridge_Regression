# Ridge_Regression
📄 README.md
markdown
Copy
Edit
# Car Price Predictor using Flask & Ridge Regression

This is a simple web application built with **Flask** and **Ridge Regression** to predict the price of a used car based on its features like make, year, mileage, fuel type, transmission, and ownership history.

---

## Features

- Predict car price using a trained Ridge Regression model
- User-friendly web interface
- Model trained on a sample dataset (`car_prices.csv`)
- Encodes categorical data and scales numeric features automatically

---

##  Tech Stack

- Python 
- Flask 
- scikit-learn 
- HTML + CSS for UI 

---

##  Project Structure
```
car_price_predictor/
├── app.py # Flask application
├── train_model.py # Model training script
├── car_prices.csv # Sample dataset
├── model/
│ └── ridge_model.pkl # Trained Ridge Regression model
├── templates/
│ ├── index.html # Input form page
│ └── result.html # Result display page
├── static/
│ └── style.css # Stylesheet
└── requirements.txt # Dependencies
```

---

##  Getting Started

1. Clone the repo

```
git clone https://github.com/yourusername/car-price-predictor.git
cd car-price-predictor
```

2. Install dependencies
```
pip install -r requirements.txt
```
4. Train the model
```
python train_model.py
```
5. Run the web app
```
python app.py
```
6. Open in browser
Visit: http://127.0.0.1:5000

 # Sample Inputs
Make	Year	Mileage	FuelType	Transmission	OwnerCount
Honda	2018	30000	Petrol	Manual	1

 # Model Details
Algorithm: Ridge Regression

Categorical Encoding: OneHotEncoder

Feature Scaling: StandardScaler

Pipeline: Preprocessing + Model combined using Pipeline
# ScreenShots
![alt text](<Screenshot 2025-08-02 220322.png>)
![alt text](<Screenshot 2025-08-02 220402.png>)
![alt text](<Screenshot 2025-08-02 220534.png>)