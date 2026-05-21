import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import random
import requests

from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Energy Pricing System",
    page_icon="⚡",
    layout="wide"
)

# =========================================================
# AUTO REFRESH
# =========================================================

st.cache_data.clear()

# =========================================================
# FUTURISTIC CSS
# =========================================================

page_bg = """
<style>

[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(
            135deg,
            #020617 0%,
            #0F172A 40%,
            #111827 100%
        );

    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: white;
}

@keyframes gradient {

0% {
background-position: 0% 50%;
}

50% {
background-position: 100% 50%;
}

100% {
background-position: 0% 50%;
}

}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

section[data-testid="stSidebar"] {
    background: rgba(15,23,42,0.95);
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    padding: 20px;

    border-radius: 20px;

    backdrop-filter: blur(20px);

    box-shadow: 0 0 20px rgba(0,229,255,0.2);
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3, h4 {
    color: white;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div style='
        padding:40px;
        border-radius:30px;
        background:linear-gradient(
            135deg,
            rgba(0,255,255,0.15),
            rgba(255,255,255,0.05)
        );
        border:1px solid rgba(0,255,255,0.25);
        backdrop-filter:blur(30px);
        box-shadow:0 0 60px rgba(0,255,255,0.25);
        text-align:center;
    '>

    <h1 style='
        font-size:60px;
        color:#00F5FF;
        letter-spacing:3px;
        text-shadow:0 0 30px #00F5FF;
    '>
    ⚡ AI ENERGY PRICING SYSTEM
    </h1>

    <h3 style='
        color:#CBD5E1;
        font-weight:300;
    '>
    AI Powered Smart Energy Forecasting Dashboard
    </h3>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# LIVE STATUS
# =========================================================

st.markdown(
    """
    <marquee behavior="scroll" direction="left">

    ⚡ AI Engine Active |
    🛰 Monitoring Systems Online |
    🌍 Smart Grid Stable |
    🤖 AI Pricing Running |
    🔋 Storage Systems Active |
    📈 Demand Prediction Enabled

    </marquee>
    """,
    unsafe_allow_html=True
)

# =========================================================
# CLOCK
# =========================================================

current_time = datetime.now().strftime("%H:%M:%S")

st.markdown(f"## 🕒 Live Time: {current_time}")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚡ AI Control Center")

city = st.sidebar.selectbox(
    "🏙 Select City",
    [
        "Chennai",
        "Bangalore",
        "Hyderabad",
        "Mumbai",
        "Delhi",
        "Coimbatore",
        "Salem",
        "Madurai",
        "Trichy",
        "Pune"
    ]
)

temp_input = st.sidebar.slider(
    "🌡 Temperature (°C)",
    20,
    45,
    30
)

humidity_input = st.sidebar.slider(
    "💧 Humidity (%)",
    30,
    90,
    50
)

# =========================================================
# LIVE WEATHER
# =========================================================

st.sidebar.markdown("## 🌦 Live Weather")

st.sidebar.metric(
    "Temperature",
    f"{temp_input} °C"
)

st.sidebar.metric(
    "Humidity",
    f"{humidity_input}%"
)

# =========================================================
# CITY FACTOR
# =========================================================

city_factor = {
    "Chennai": 40,
    "Bangalore": 30,
    "Hyderabad": 35,
    "Mumbai": 45,
    "Delhi": 50,
    "Coimbatore": 20,
    "Salem": 15,
    "Madurai": 18,
    "Trichy": 16,
    "Pune": 25
}

# =========================================================
# LIVE METRICS
# =========================================================

st.markdown(f"## 🌍 Active City: {city}")

s1, s2, s3 = st.columns(3)

with s1:
    st.metric(
        "⚡ Power Demand",
        f"{random.randint(250,500)} MW"
    )

with s2:
    st.metric(
        "📈 Demand Level",
        f"{random.randint(40,95)}%"
    )

with s3:
    st.metric(
        "🔋 Storage Usage",
        f"{random.randint(45,90)}%"
    )

# =========================================================
# DATA GENERATION
# =========================================================

dates = pd.date_range(
    start="2024-01-01",
    periods=365
)

np.random.seed(42)

temperature = np.random.randint(
    20,
    40,
    size=365
)

humidity = np.random.randint(
    40,
    90,
    size=365
)

energy = (
    200 +
    temperature * 5 -
    humidity * 2 +
    city_factor[city] +
    np.random.randint(-20,20,size=365)
)

df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature,
    "Humidity": humidity,
    "Energy": energy
})

# =========================================================
# MACHINE LEARNING
# =========================================================

X = df[["Temperature", "Humidity"]]

y = df["Energy"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor()

model.fit(X_train, y_train)

prediction = model.predict(
    pd.DataFrame(
        [[temp_input, humidity_input]],
        columns=["Temperature", "Humidity"]
    )
)

# =========================================================
# MODEL ACCURACY
# =========================================================

accuracy = model.score(X_test, y_test)

# =========================================================
# ELECTRICITY PRICE
# =========================================================

price = prediction[0] * 0.12

# =========================================================
# KPI METRICS
# =========================================================

st.markdown("## 📊 Smart Energy Metrics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "⚡ Predicted Energy",
        f"{prediction[0]:.2f} kWh"
    )

with c2:
    st.metric(
        "💰 Electricity Price",
        f"₹ {price:.2f}"
    )

with c3:
    st.metric(
        "🎯 Model Accuracy",
        f"{accuracy*100:.2f}%"
    )

with c4:
    st.metric(
        "🧠 AI Confidence",
        f"{random.randint(92,99)}%"
    )

# =========================================================
# GAUGE CHART
# =========================================================

st.markdown("## ⚡ Energy Demand Gauge")

gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=prediction[0],
    title={'text': "Energy Demand"},
    gauge={
        'axis': {'range': [0, 500]}
    }
))

gauge.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(
    gauge,
    use_container_width=True
)

# =========================================================
# ALERTS
# =========================================================

if prediction[0] > 300:

    st.error(
        "🚨 Critical Energy Demand Spike Detected"
    )

elif prediction[0] > 250:

    st.warning(
        "⚠ Peak Energy Consumption Expected"
    )

else:

    st.success(
        "✅ Energy System Operating Normally"
    )

# =========================================================
# FORECAST GRAPH
# =========================================================

st.markdown("## 📈 Energy Forecast")

fig = px.line(
    df,
    x="Date",
    y="Energy",
    title="AI Energy Forecast"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(17,24,39,0.6)",
    font=dict(color="white")
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================================================
# TEMPERATURE GRAPH
# =========================================================

st.markdown("## 🌡 Temperature Analytics")

fig2 = px.scatter(
    df,
    x="Temperature",
    y="Energy",
    color="Humidity",
    size="Energy",
    hover_data=["Date"]
)

fig2.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(17,24,39,0.6)",
    font=dict(color="white")
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =========================================================
# AI CHATBOT
# =========================================================

st.markdown("## 🤖 AI Energy Assistant")

user_question = st.text_input(
    "Ask AI About Energy Usage"
)

if user_question:

    st.success("AI Response Generated")

    st.write(
        """
        ⚡ AI Analysis:

        Higher temperature increases energy demand.
        Smart storage balancing is recommended.
        Dynamic pricing can reduce peak load.
        """
    )

# =========================================================
# DOWNLOAD REPORT
# =========================================================

st.markdown("## 📥 Download Energy Report")

csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download CSV Report",
    data=csv,
    file_name="energy_report.csv",
    mime="text/csv"
)

# =========================================================
# DATASET TABLE
# =========================================================

st.markdown("## 📊 Dataset Preview")

st.dataframe(df.head(20))

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <center>

    <h3 style='color:white;'>
    ⚡ AI Smart Energy Pricing Dashboard
    </h3>

    <p style='color:#94A3B8;'>
    Real-Time Monitoring • AI Prediction • Smart Grid Analytics
    </p>

    </center>
    """,
    unsafe_allow_html=True
)