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
#df_predictions_by_rate.
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
    st.header("Exchange")
    st.subheader("Exchange App")
    # --- Drop box
    selected_rate_tab1 = st.selectbox(
        label="exchange_rate",
        options=SERIE,
        index=0,
        placeholder="Select a serie",
    )
    interest_tab1 = st.number_input("interest rate tab1", format="%f", value=3., step=1.0)
    inflation_tab1 = st.number_input("inflation tab1", format="%f", step=1.0, value=1.0)

    # --- Format input into pandas dataframe
    user_entry_tab1 = pd.DataFrame(
        [
            {
                "interest_rate": interest_tab1,
                "inflation": inflation_tab1,
            }
        ]
    )
    ## --- rate estimation
    #estimated_exchange_rate = float(
    #    df_predictions_by_rate.query("exchange_rate == @selected_rate")[
    #        "Exchange"
    #    ].values[0]
    #)

    # --- Display
    #st.metric("Estimated Exchange Rate", f"$ {estimated_exchange_rate}")

# tab 2
with tab2:
    st.header("Interest")
    st.subheader(" Interest App")
    # --- Drop box
    selected_rate_tab2 = st.selectbox(
        label="interest_rate",
        options=SERIE,
        index=0,
        placeholder="Select a serie",
    )
    exchange_tab2 = st.number_input("exchange rate tab2", format="%f", value=3., step=1.0)
    inflation_tab2 = st.number_input("inflation tab2", format="%f", step=1.0, value=1.0)

    # --- Format input into pandas dataframe
    user_entry_tab2 = pd.DataFrame(
        [
            {
                "exchange_rate": exchange_tab2,
                "inflation": inflation_tab2,
            }
        ]
    )

# tab 3
with tab3:
    st.header("Inflation")
    st.subheader(" inflation App")
    # --- Drop box
    selected_rate_tab3 = st.selectbox(
        label="inflation_rate",
        options=SERIE,
        index=0,
        placeholder="Select a serie",
    )
    exchange_tab3= st.number_input("exchange rate tab3", format="%f", value=3., step=1.0)
    interest_tab3= st.number_input("interest rate tab3", format="%f", value=3., step=1.0)

    # --- Format input into pandas dataframe
    user_entry_tab3 = pd.DataFrame(
        [
            {
                "exchange_rate": exchange_tab3,
                "Interest": interest_tab3,
            }
        ]
    )