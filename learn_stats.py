import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Interactive Stats Tutor", layout="wide")
st.title("📊 Interactive Statistics Tutor")

# User input
concept = st.text_input("Paste a concept (e.g., mean, median, probability, normal distribution):")

# ------------------ PROBABILITY ------------------
def probability_demo():
    st.subheader("🎲 Probability Playground")
    red_count = st.slider("Number of Red Balls", 1, 10, 3)
    blue_count = st.slider("Number of Blue Balls", 1, 10, 2)

    if "red_picked" not in st.session_state:
        st.session_state.red_picked = 0
        st.session_state.blue_picked = 0
        st.session_state.total = 0

    if st.button("Pick a Ball 🎯"):
        jar = ["Red"] * red_count + ["Blue"] * blue_count
        choice = random.choice(jar)
        st.session_state.total += 1
        if choice == "Red":
            st.session_state.red_picked += 1
        else:
            st.session_state.blue_picked += 1
        st.success(f"You picked a {choice} ball!")

    total_balls = red_count + blue_count
    st.write(f"**Theoretical Probability:** Red = {red_count}/{total_balls}, Blue = {blue_count}/{total_balls}")

    if st.session_state.total > 0:
        red_prob = st.session_state.red_picked / st.session_state.total
        blue_prob = st.session_state.blue_picked / st.session_state.total
        st.write(f"**Experimental Probability:** Red = {red_prob:.2f}, Blue = {blue_prob:.2f}")

        fig, ax = plt.subplots()
        ax.bar(["Red", "Blue"], [st.session_state.red_picked, st.session_state.blue_picked], color=["red", "blue"])
        ax.set_ylabel("Times Picked")
        st.pyplot(fig)

# ------------------ MEAN & MEDIAN ------------------
def mean_median_demo():
    st.subheader("📏 Mean & Median Playground")
    numbers = st.text_input("Enter numbers separated by commas:", "2, 4, 6, 8")
    try:
        nums = [float(x.strip()) for x in numbers.split(",")]
        mean = np.mean(nums)
        median = np.median(nums)

        st.write(f"**Mean:** {mean:.2f}")
        st.write(f"**Median:** {median:.2f}")

        fig, ax = plt.subplots()
        ax.bar(range(len(nums)), nums, color="skyblue")
        ax.axhline(mean, color="red", linestyle="--", label=f"Mean = {mean:.2f}")
        ax.axhline(median, color="green", linestyle=":", label=f"Median = {median:.2f}")
        ax.legend()
        st.pyplot(fig)
    except:
        st.warning("Please enter valid numbers.")

# ------------------ NORMAL DISTRIBUTION ------------------
def normal_dist_demo():
    st.subheader("📈 Normal Distribution Playground")
    mean = st.slider("Mean (μ)", -5.0, 5.0, 0.0)
    stddev = st.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0)

    x = np.linspace(-10, 10, 400)
    y = (1 / (stddev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / stddev) ** 2)

    fig, ax = plt.subplots()
    ax.plot(x, y, color="blue")
    ax.axvline(mean, color="red", linestyle="--", label="Mean")
    ax.set_title("Normal Distribution Curve")
    ax.legend()
    st.pyplot(fig)

# ------------------ REGRESSION ------------------
def regression_demo():
    st.subheader("📉 Regression Playground")
    n_points = st.slider("Number of Data Points", 10, 200, 50)
    noise = st.slider("Noise Level", 0.0, 2.0, 0.5)

    x = np.linspace(0, 10, n_points)
    y = 2 * x + 3 + np.random.normal(0, noise, n_points)

    coeffs = np.polyfit(x, y, 1)
    y_pred = np.polyval(coeffs, x)

    st.write(f"**Regression Line Equation:** y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")

    fig, ax = plt.subplots()
    ax.scatter(x, y, color="blue", alpha=0.6, label="Data")
    ax.plot(x, y_pred, color="red", label="Regression Line")
    ax.legend()
    st.pyplot(fig)

# ------------------ ROUTER ------------------
if concept:
    c = concept.lower()
    if "prob" in c:
        probability_demo()
    elif "mean" in c or "median" in c:
        mean_median_demo()
    elif "normal" in c or "distribution" in c:
        normal_dist_demo()
    elif "regression" in c:
        regression_demo()
    else:
        st.info("Concept not found. Try: probability, mean, median, normal distribution, regression")
