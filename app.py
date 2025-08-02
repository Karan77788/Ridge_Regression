from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model/ridge_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            user_input = pd.DataFrame([{
                'Make': request.form['make'],
                'Year': int(request.form['year']),
                'Mileage': int(request.form['mileage']),
                'FuelType': request.form['fuel'],
                'Transmission': request.form['trans'],
                'OwnerCount': int(request.form['owners'])
            }])

            prediction = model.predict(user_input)[0]
            return render_template('result.html', prediction=round(prediction, 2))
        except:
            return render_template('index.html', error="Invalid input.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
