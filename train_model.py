import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load and preprocess the data
data = pd.read_csv('healthcare_data.csv')  # Make sure you have this dataset
data = pd.get_dummies(data, drop_first=True)  # Encode categorical variables

# Define features and target
X = data.drop('outcome', axis=1)
y = data['outcome']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file
