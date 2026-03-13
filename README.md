# 🛡️ Phishing Link Detector

A Machine Learning-powered web application that identifies malicious URLs and phishing attempts in real-time.

## 🚀 [Live Demo](https://phisinglinkdetection-2dny67ynz8xdabf3kc6m2d.streamlit.app/)

## 📝 Project Overview
Phishing remains one of the most common cyber threats. This project uses a **Random Forest** (or your specific model) classifier trained on a dataset of over 650,000 URLs to predict whether a given link is safe or malicious based on its structural features.

### Key Features
* **Real-time Analysis:** Enter any URL and get an instant safety verdict.
* **Feature Extraction:** The app analyzes 21 different URL characteristics, including:
    * Presence of IP addresses
    * URL and Hostname length
    * Presence of suspicious words (e.g., "login", "verify", "bank")
    * Count of special characters (dots, hyphens, @ symbols)
    * Use of URL shortening services (e.g., bit.ly)

## 🛠️ Technology Stack
* **Language:** Python 3.12
* **ML Framework:** Scikit-Learn
* **Web Interface:** Streamlit
* **Data Handling:** Pandas, Numpy
* **Feature Extraction:** TLD (Top Level Domain parser), Regex

## 📂 Project Structure
* `app.py`: The main Streamlit web interface logic.
* `utility.py`: Contains the feature extraction engine and regex patterns.
* `model.pkl`: The trained Machine Learning model.
* `requirements.txt`: List of dependencies for cloud deployment.

## ⚙️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
