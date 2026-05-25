import math

import matplotlib.pyplot as plt
import streamlit as st
from google import genai


st.set_page_config(page_title="AI Budget & Goal Planner", page_icon="$", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f7fbff 0%, #eef7f2 48%, #fff8ed 100%);
        color: #1f2933;
    }

    h1 {
        color: #12323f;
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    h2, h3 {
        color: #12323f;
        font-weight: 750;
    }

    section[data-testid="stSidebar"] {
        background: #12323f;
        border-right: 1px solid rgba(255, 255, 255, 0.18);
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p {
        color: #f8fafc;
    }

    section[data-testid="stSidebar"] [data-testid="stNumberInput"],
    section[data-testid="stSidebar"] [data-testid="stTextInput"] {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 8px;
        padding: 0.25rem 0.45rem;
    }

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.86);
        border: 1px solid rgba(18, 50, 63, 0.08);
        border-radius: 8px;
        box-shadow: 0 8px 24px rgba(18, 50, 63, 0.08);
        padding: 1rem;
    }

    div[data-testid="stMetric"] label {
        color: #52616b;
    }

    div[data-testid="stMetricValue"] {
        color: #12323f;
    }

    div[data-testid="stVerticalBlock"] > div:has(> div[data-testid="stMarkdownContainer"] h3) {
        background: rgba(255, 255, 255, 0.72);
        border: 1px solid rgba(18, 50, 63, 0.08);
        border-radius: 8px;
        box-shadow: 0 10px 28px rgba(18, 50, 63, 0.08);
        padding: 1.1rem 1.25rem;
    }

    .stButton > button {
        bacimport math

import matplotlib.pyplot as plt
import streamlit as st
from google import genai


st.set_page_config(page_title="AI Budget & Goal Planner", page_icon="$", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f7fbff 0%, #eef7f2 48%, #fff8ed 100%);
        color: #1f2933;
    }

    h1 {
        color: #12323f;
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    h2, h3 {
        color: #12323f;
        font-weight: 750;
    }

    section[data-testid="stSidebar"] {
        background: #12323f;
        border-right: 1px solid rgba(255, 255, 255, 0.18);
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p {
        color: #f8fafc;
    }

    section[data-testid="stSidebar"] [data-testid="stNumberInput"],
    section[data-testid="stSidebar"] [data-testid="stTextInput"] {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 8px;
        padding: 0.25rem 0.45rem;
    }

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.86);
        border: 1px solid rgba(18, 50, 63, 0.08);
        border-radius: 8px;
        box-shadow: 0 8px 24px rgba(18, 50, 63, 0.08);
        padding: 1rem;
    }

    div[data-testid="stMetric"] label {
        color: #52616b;
    }

    div[data-testid="stMetricValue"] {
        color: #12323f;
    }

    div[data-testid="stVerticalBlock"] > div:has(> div[data-testid="stMarkdownContainer"] h3) {
        background: rgba(255, 255, 255, 0.72);
        border: 1px solid rgba(18, 50, 63, 0.08);
        border-radius: 8px;
        box-shadow: 0 10px 28px rgba(18, 50, 63, 0.08);
        padding: 1.1rem 1.25rem;
    }

    .stButton > button {
        background: #0f766e;
        color: white;
        border: 0;
        border-radius: 8px;
        font-weight: 700;
        padding: 0.65rem 1rem;
        width: 100%;
        box-shadow: 0 8px 20px rgba(15, 118, 110, 0.22);
    }

    .stButton > button:hover {
        background: #0b5f59;
        color: white;
        border: 0;
    }

    .stAlert {
        border-radius: 8px;
    }

    canvas {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)kground: #0f766e;
        color: white;
        border: 0;
        border-radius: 8px;
        font-weight: 700;
        padding: 0.65rem 1rem;
        width: 100%;
        box-shadow: 0 8px 20px rgba(15, 118, 110, 0.22);
    }

    .stButton > button:hover {
        background: #0b5f59;
        color: white;
        border: 0;
    }

    .stAlert {
        border-radius: 8px;
    }

    canvas {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


                                   
                                        
