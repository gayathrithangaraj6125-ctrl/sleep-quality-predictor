import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# load dataset
data = pd.read_csv("dataset.csv")

# selecting features
X = data[[
    "Sleep Duration",
    "Physical Activity Level",
    "Stress Level",
    "Daily Steps",
    "Heart Rate"
]]

y = data["Quality of Sleep"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")