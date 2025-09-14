import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# -------------------
# Page Config
# -------------------
st.set_page_config(page_title="Stats Playground", layout="wide")

# -------------------
# Sidebar Navigation
# -------------------
st.sidebar.title("📊 Stats Playground")
topic = st.sidebar.selectbox(
    "Choose a topic",
    ["Mean & Median", "Probability Basics", "Distributions", "Custom Lesson"]
)

dark_mode = st.sidebar.checkbox("🌙 Dark Mode", value=False)

# Apply dark mode style
if dark_mode:
    st.markdown(
        """
        <style>
        body {
            background-color: #1E1E1E;
            color: white;
        }
        .stPlotlyChart {
            background-color: #1E1E1E;
        }
        </style>
        """, unsafe_allow_html=True
    )

# -------------------
# Topic 1: Mean & Median
# -------------------
if topic == "Mean & Median":
    st.header("📍 Understanding Mean & Median")
    st.write("Example: Exam scores of 10 students")

    scores = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    mean_val = np.mean(scores)
    median_val = np.median(scores)

    st.write(f"Mean: {mean_val}, Median: {median_val}")

    fig, ax = plt.subplots(figsize=(6,3))
    ax.hist(scores, bins=5, color="skyblue", edgecolor="black")
    ax.axvline(mean_val, color='red', linestyle='--', label=f"Mean = {mean_val}")
    ax.axvline(median_val, color='green', linestyle='-', label=f"Median = {median_val}")
    ax.legend()
    st.pyplot(fig)

    # MCQ
    st.subheader("📝 Quick Quiz")
    q1 = st.radio("If a new student scores 100, which measure changes more?", 
                  ["Mean", "Median"])
    if q1 == "Mean":
        st.success("✅ Correct! Mean is sensitive to outliers.")
    elif q1 == "Median":
        st.error("❌ Median is less affected by outliers.")

# -------------------
# Topic 2: Probability
# -------------------
elif topic == "Probability Basics":
    st.header("🎲 Probability Basics")
    st.write("Example: Tossing a fair coin")

    outcomes = ["Head", "Tail"]
    st.write("Outcomes:", outcomes)

    st.latex(r"P(\text{Head}) = \frac{1}{2}, \; P(\text{Tail}) = \frac{1}{2}")

    flips = np.random.choice(outcomes, size=50)
    head_count = np.sum(flips == "Head")
    tail_count = 50 - head_count

    fig, ax = plt.subplots(figsize=(4,3))
    ax.bar(["Head", "Tail"], [head_count, tail_count], color=["orange", "blue"])
    st.pyplot(fig)

    # MCQ
    q2 = st.radio("If we toss 1 coin, what’s the probability of getting Tail?",
                  ["0.25", "0.5", "1"])
    if q2 == "0.5":
        st.success("✅ Correct! A fair coin has equal chance.")
    else:
        st.error("❌ Try again.")

# -------------------
# Topic 3: Distributions
# -------------------
elif topic == "Distributions":
    st.header("📈 Normal Distribution")
    st.write("Example: Heights of students in cm")

    data = np.random.normal(170, 10, 200)
    fig, ax = plt.subplots(figsize=(6,3))
    ax.hist(data, bins=20, color="purple", edgecolor="white", density=True)
    st.pyplot(fig)

    st.write("Most values cluster around the mean (170 cm).")

# -------------------
# Topic 4: Custom Content
# -------------------
elif topic == "Custom Lesson":
    st.header("✍️ Paste Your Own Content")
    user_content = st.text_area("Paste your explanation, notes, or example here:")
    if user_content:
        st.write("### Your Lesson")
        st.write(user_content)
        st.info("👉 Future: AI can turn this into interactive graphs & quizzes automatically!")
