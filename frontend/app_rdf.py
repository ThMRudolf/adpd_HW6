"""
Proof of concept application for inflation, exchange rate and interest rate.

Version 0.0.0
"""

from io import StringIO
import pickle
import streamlit as st
import pandas as pd
from great_tables import GT

# --- setup
SERIE = [
    "Exchange",
    "Inflation",
    "Interest",
]

# --- Read data
df_predictions_by_rate = pd.read_parquet(
    "data/model/models_summary.parquet"
)

################################# App #################################
st.title("Relation Exchange/Inflation/Interest App")

tab1, tab2, tab3 = st.tabs(
    [
        "📈 Exchange - Interest",
        "📈 Inflation - Interest",
        "📈 Exchange - Inflation",
    ]
)

# tab 1
with tab1:
    st.header("Exchange - Interest")
    st.subheader("Exchange - Interest App")
    # --- Drop box
    selected_rate = st.selectbox(
        label="rate",
        options=SERIE,
        index=0,
        placeholder="Select a serie",
    )

    # --- rate estimation
    estimated_exchange_rate = float(
        df_predictions_by_rate.query("exchange_rate == @selected_rate")[
            "Exchange"
        ].values[0]
    )

    # --- Display
    #st.metric("Estimated Exchange Rate", f"$ {estimated_exchange_rate}")

# tab 2
