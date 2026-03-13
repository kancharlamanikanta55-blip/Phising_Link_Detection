from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  # Added for serving HTML
import numpy as np
import joblib
import os
from utility import main

# 1. Load the model
model = joblib.load("model.pkl")

app = FastAPI()

# 2. Setup Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Mount Static Files
# This looks for the 'static' folder you created
app.mount("/static", StaticFiles(directory="static"), name="static")

class URLData(BaseModel):
    url: str

# 4. Route to serve the website
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

# 5. Classification Logic
@app.post("/classify-url/")
async def classify_url(url_data: URLData):
    # Extract features using your utility.py
    features = main(url_data.url)
    features = np.array(features).reshape((1, -1))
    
    # Simple whitelist for common safe sites
    whitelist = {
        "https://www.google.com/",
        "https://www.netflix.com/in/",
        "https://www.microsoft.com/en-in",
        "https://www.audisankara.ac.in/",
        "https://chatgpt.com/c"
    }
    
    if url_data.url in whitelist:
        return {"url": url_data.url, "classification": "SAFE"}

    # Predict using the model
    prediction = model.predict(features)

    # Categories based on your LabelEncoder in the notebook
    # 0: Benign, 1: Defacement, 2: Malware, 3: Phishing
    categories = {0: "SAFE", 1: "DEFACEMENT", 2: "MALWARE", 3: "PHISHING"}
    result = categories.get(int(prediction[0]), "Unknown category")

    return {"url": url_data.url, "classification": result}

if __name__ == "__main__":
    import uvicorn
    # Use environment port for Render (default to 10000)
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
