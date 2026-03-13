import streamlit as st
import joblib
import numpy as np
import os
from utility import main as extract_features

st.set_page_config(page_title="Phishing Detector", layout="centered")

st.title("🛡️ Phishing Link Detector")

# 1. Check if the model file actually exists
if not os.path.exists('model.pkl'):
    st.error("❌ Error: 'model.pkl' not found in this folder! Please make sure the file is in C:\Final\Phising_Link_Detection")
else:
    try:
        # Load the model
        model = joblib.load('model.pkl')
        st.success("✅ Model loaded successfully!")

        # 2. UI for User Input
        url_input = st.text_input("Enter a URL to analyze:", placeholder="https://example.com")

        if st.button("Check URL"):
            if url_input:
                with st.spinner('Analyzing...'):
                    # Get features from utility.py
                    features = extract_features(url_input)
                    features_array = np.array(features).reshape(1, -1)
                    
                    # Predict
                    prediction = model.predict(features_array)
                    
                    st.divider()
                    if prediction[0] == 0:
                        st.balloons()
                        st.success("### RESULT: SAFE ✅")
                    else:
                        st.error("### RESULT: MALICIOUS ⚠️")
            else:
                st.warning("Please enter a URL first.")

    except Exception as e:
        st.error(f"❌ An error occurred while loading the model: {e}")