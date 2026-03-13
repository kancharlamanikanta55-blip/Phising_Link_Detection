import streamlit as st
import joblib
import numpy as np
import pandas as pd  # <--- Added Pandas
import os
from utility import main as extract_features

st.set_page_config(page_title="Phishing Detector", layout="centered")

st.title("🛡️ Phishing Link Detector")

# --- MODEL LOADING WITH FIX ---
if not os.path.exists('model.pkl'):
    st.error("❌ Error: 'model.pkl' not found!")
else:
    try:
    model = joblib.load('model.pkl')
    
    # This is the "Safety Valve"
    # It checks if the model has the old 'use_label_encoder' attribute 
    # and handles it so it doesn't crash during .predict()
    if hasattr(model, "use_label_encoder"):
        model.use_label_encoder = False 
        
    st.success("✅ Model loaded successfully!")

        url_input = st.text_input("Enter a URL to analyze:", placeholder="https://example.com")

        if st.button("Check URL"):
            if url_input:
                with st.spinner('Analyzing...'):
                    # 1. Get raw features
                    features = extract_features(url_input)
                    
                    # 2. Define exact column names from your training session
                    cols = [
                        'use_of_ip', 'abnormal_url', 'count.', 'count-www', 'count@', 
                        'count_dir', 'count_embed_domian', 'short_url', 'count-https', 
                        'count-http', 'count%', 'count?', 'count-', 'count=', 
                        'url_length', 'hostname_length', 'sus_url', 'fd_length', 
                        'tld_length', 'count-digits', 'count-letters'
                    ]
                    
                    # 3. Create DataFrame (XGBoost 3.2.0 needs this for accuracy)
                    features_df = pd.DataFrame([features], columns=cols)
                    
                    # --- DEBUG SECTION ---
                    st.write("### 🔍 Model Debug Info")
                    st.write("Features extracted:", features_df)
                    # ----------------------
                    
                    # 4. Predict
                    prediction = model.predict(features_df)
                    
                    st.divider()
                    if prediction[0] == 0:
                        st.balloons()
                        st.success("### RESULT: SAFE ✅")
                    else:
                        st.error("### RESULT: MALICIOUS ⚠️")
            else:
                st.warning("Please enter a URL first.")

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")


