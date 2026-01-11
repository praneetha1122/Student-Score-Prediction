import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# 1 Load the dataset
data = pd.read_csv("student_scores.csv")

# 2️ Split into input (X) and output (y)
X = data[['Hours']]  # input feature
y = data['Scores']   # output label

# 3️ Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️ Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5️ Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")