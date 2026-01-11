from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    prediction = model.predict(np.array([[hours]]))[0]
    return render_template("result.html", prediction_text=f"Predicted Score: {round(prediction, 2)}")

if __name__ == "__main__":
    app.run(debug=True)
