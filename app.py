import streamlit as st
import pandas as pd
import datetime
import os
from predictor import predict_sleep
from suggestions import get_suggestions

# Page Title
st.title("🌙 Sleep Quality Predictor")

st.write("Enter your lifestyle details below to analyze your sleep quality.")

# User Inputs
sleep = st.slider("🛌 Sleep Duration (hours)", 0, 12, 6)

activity = st.slider("🏃 Physical Activity Level", 0, 100, 30)

stress = st.slider("😓 Stress Level", 0, 10, 5)

steps = st.number_input("👣 Daily Steps", 1000, 20000, 5000)

heart = st.slider("❤️ Heart Rate", 50, 120, 80)

screen_time = st.slider("📱 Screen Time Before Bed (minutes)", 0, 180, 60)

exercise = st.slider("🏋️ Exercise Minutes", 0, 120, 20)


# Predict Button
if st.button("🔍 Predict Sleep Quality"):

    # ML Prediction
    data = [sleep, activity, stress, steps, heart]

    result = predict_sleep(data)

    # Sleep Score Calculation
    score = max(0, min(100, (sleep * 10) - stress + activity / 2))

    # Result Display
    if result == "Good":
        st.success(f"Predicted Sleep Quality: {result} 😊")

    elif result == "Average":
        st.warning(f"Predicted Sleep Quality: {result} 😐")

    else:
        st.error(f"Predicted Sleep Quality: {result} 😴")


    # Score Display
    st.subheader(f"Sleep Score: {score}")

    st.progress(int(score))


    # Habit Quality Rating
    st.subheader("📊 Habit Quality Rating")

    if score >= 80:
        st.success("Excellent lifestyle habits")

    elif score >= 50:
        st.warning("Moderate lifestyle habits")

    else:
        st.error("Lifestyle needs improvement")


    # Suggestions Section
    st.subheader("💡 Personalized Suggestions")

    tips = get_suggestions(stress, screen_time, exercise)

    for tip in tips:
        st.info(tip)


    # Explanation Engine
    st.subheader("🔍 Main Factors Affecting Your Sleep")

    reasons = []

    if stress > 7:
        reasons.append("High stress level detected")

    if screen_time > 60:
        reasons.append("Too much screen exposure before sleep")

    if exercise < 20:
        reasons.append("Low physical activity")

    if sleep < 6:
        reasons.append("Insufficient sleep duration")

    if len(reasons) == 0:
        reasons.append("Your lifestyle habits look healthy")

    for r in reasons:
        st.write("•", r)


    # Improvement Simulator
    if result != "Good":

        st.subheader("🚀 Improvement Simulation")

        improved_score = min(100, score + 15)

        st.info(f"If habits improve, your Sleep Score may increase to: {improved_score}")


    # Save History Data
    new_entry = pd.DataFrame({
        "Date": [datetime.datetime.now()],
        "Score": [score]
    })

    file_exists = os.path.isfile("history.csv")

    new_entry.to_csv(
        "history.csv",
        mode="a",
        header=not file_exists,
        index=False
    )


# Weekly Trend Graph Section
st.subheader("📈 Weekly Sleep Trend")

try:

    history = pd.read_csv("history.csv")

    if "Score" in history.columns:

        st.line_chart(history["Score"])

    else:

        st.write("No history available yet")

except:

    st.write("No history available yet")