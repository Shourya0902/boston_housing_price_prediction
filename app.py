import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import uvicorn

app = FastAPI()

regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scalar.pkl', 'rb'))

# Define the data structure (Schema)
class PredictionInput(BaseModel):
    data: dict

@app.get("/")
def home():
    return {"message": "Welcome to the Prediction API"}

@app.post("/predict_api")
def predict_api(input_data: PredictionInput):
    # Extract the dictionary from the request
    data = input_data.data
    
    # 3. Convert dict values to a list and then to a NumPy array
    # We reshape to (1, -1) because scikit-learn expects a 2D array for a single sample
    feature_order = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
    raw_values = np.array([data[k] for k in feature_order]).reshape(1, -1)
    
    # 4. Scale the data
    new_data = scalar.transform(raw_values)
    
    # 5. Make the prediction
    output = regmodel.predict(new_data)
    
    # 6. Return the result
    # We use output[0] because predict() returns an array
    # FastAPI automatically handles 'jsonify' for you when you return a dict
    return float(output[0])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
