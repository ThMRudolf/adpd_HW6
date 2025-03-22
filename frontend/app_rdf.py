"""
Proof of concept application for inflation, exchange rate and interest rate.

Version 0.0.0
"""

import streamlit as st
import pandas as pd

import statsmodels.api as sm

# Load the models' summary from the .parquet file
models_summary = pd.read_parquet('data/model/models_summary.parquet')

# Extract the model parameters
params_tipo_de_cambio_tasa_de_interes = models_summary.loc[models_summary['model'] == 'tipo_de_cambio ~ tasa_de_interes', 'params'].values[0]
params_tasa_de_interes_inflacion = models_summary.loc[models_summary['model'] == 'tasa_de_interes ~ inflacion', 'params'].values[0]
params_tipo_de_cambio_inflacion = models_summary.loc[models_summary['model'] == 'tipo_de_cambio ~ inflacion', 'params'].values[0]

# Convert the parameters to a dictionary
params_tipo_de_cambio_tasa_de_interes = params_tipo_de_cambio_tasa_de_interes
params_tasa_de_interes_inflacion = params_tasa_de_interes_inflacion
params_tipo_de_cambio_inflacion = params_tipo_de_cambio_inflacion

# Predict values using the model parameters
def predict_tipo_de_cambio_tasa_de_interes(interes_rate):
    return params_tipo_de_cambio_tasa_de_interes['const'] + params_tipo_de_cambio_tasa_de_interes['interes_rate'] * interes_rate

def predict_tasa_de_interes_inflacion(inflation):
    return params_tasa_de_interes_inflacion['const'] + params_tasa_de_interes_inflacion['inflation'] * inflation

def predict_tipo_de_cambio_inflacion(inflation):
    return params_tipo_de_cambio_inflacion['const'] + params_tipo_de_cambio_inflacion['inflation'] * inflation

# Streamlit app
st.title('Economic Predictions')

option = st.selectbox(
    'Select the prediction model:',
    ('Exchange Rate from Interest Rate', 'Interest Rate from Inflation', 'Exchange Rate from Inflation')
)

if option == 'Exchange Rate from Interest Rate':
    interes_rate = st.number_input('Enter Interest Rate:')
    if st.button('Predict'):
        result = predict_tipo_de_cambio_tasa_de_interes(interes_rate)
        st.write(f'Predicted Exchange Rate: {result}')

elif option == 'Interest Rate from Inflation':
    inflation = st.number_input('Enter Inflation Rate:')
    if st.button('Predict'):
        result = predict_tasa_de_interes_inflacion(inflation)
        st.write(f'Predicted Interest Rate: {result}')

elif option == 'Exchange Rate from Inflation':
    inflation = st.number_input('Enter Inflation Rate:')
    if st.button('Predict'):
        result = predict_tipo_de_cambio_inflacion(inflation)
        st.write(f'Predicted Exchange Rate: {result}')