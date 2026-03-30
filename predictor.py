import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

def predict_sleep(data):

    columns = [
        "Sleep Duration",
        "Physical Activity Level",
        "Stress Level",
        "Daily Steps",
        "Heart Rate"
    ]

    data_df = pd.DataFrame([data], columns=columns)

    prediction = model.predict(data_df)[0]

    return prediction