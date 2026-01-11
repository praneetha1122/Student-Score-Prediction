# Student-Score-Prediction
This project demonstrates a Flask web application that predicts student exam scores based on study hours using Linear Regression ML model. It includes model training, Flask deployment, and web interface for predictions.

Project Structure
ML_Flask_Project/

├── student_scores.csv # Student dataset (hours → scores)

├── model_training.py # Train and save ML model

├── model.pkl # Trained Linear Regression model

├── app.py # Flask web application

├── templates/ # HTML templates
│   ├── index.html # Input form
│   └── result.html # Prediction results

├── venv/ # Python virtual environment (ignored in Git)

├── .gitignore # Ignores venv, __pycache__

└── README.md # Project documentation

Setup Instructions
Clone the repository
git clone <repository_url>
cd ML_Flask_Project

Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

Install dependencies
pip install numpy pandas scikit-learn flask

Train the ML model
python model_training.py
You should see: ✅ Model trained and saved as model.pkl

Run Flask web app
python app.py
Open http://127.0.0.1:5000 in browser

Demo Usage
Enter study hours (e.g., 5.5)
Click Predict
See predicted score (e.g., Predicted Score: 51.38)

Example Predictions
Input: 2.5 hours → Output: ~21
Input: 5.5 hours → Output: ~51  
Input: 8.5 hours → Output: ~75

Notes
Dataset simulates student study hours vs exam scores
Model uses scikit-learn LinearRegression
Flask serves predictions via web interface
Virtual environment keeps dependencies isolated
Perfect for ML portfolio and campus placements

Dependencies
Python 3.10+
numpy
pandas
scikit-learn
flask

Author
Praneetha
