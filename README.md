# Boston Housing Price Prediction

An end-to-end machine learning application that predicts Boston housing prices using Linear Regression, served via a FastAPI backend and an interactive Streamlit frontend — fully containerised with Docker.

🚀 **Live Demo:** `[coming soon]`

---

## What This Project Does

Takes 13 housing-related features (crime rate, number of rooms, distance to employment centres, etc.) and predicts the median property value. The model is exposed through a REST API and a user-friendly web interface where anyone can plug in values and get a prediction instantly.

---

## Model Performance

| Metric | Score |
|---|---|
| R² | 0.711 |
| Adjusted R² | 0.684 |
| RMSE | 4.64 |
| MSE | 21.51 |
| MAE | 3.16 |

The model explains ~71% of the variance in housing prices. The MAE of 3.16 means predictions are off by about $3,160 on average (prices are in $1,000s).

---

## Tech Stack

| Layer | Tools |
|---|---|
| Modelling | scikit-learn, pandas, numpy, statsmodels |
| API | FastAPI, uvicorn |
| Frontend | Streamlit |
| Containerisation | Docker |
| Visualisation | matplotlib, seaborn |

---

## Project Structure

```
boston_housing_price_prediction/
├── dataset/               # Raw housing data
├── notebook/              # EDA and model development
├── src/                   # Core application code
│   ├── app.py             # FastAPI app & prediction endpoint
│   └── frontend.py        # Streamlit UI
├── Dockerfile             # Container setup (FastAPI + Streamlit)
├── start.sh               # Startup script
├── requirements.txt
└── pyproject.toml
```

---

## Running Locally

**With Docker (recommended)**

```bash
git clone https://github.com/Shourya0902/boston_housing_price_prediction.git
cd boston_housing_price_prediction
docker build -t boston-housing .
docker run -p 8000:8000 -p 8501:8501 boston-housing
```

Then open:
- Streamlit UI: `http://localhost:8501`
- FastAPI docs: `http://localhost:8000/docs`

**Without Docker**

```bash
pip install -r requirements.txt
bash start.sh
```

---

## API Usage

`POST /predict`

```json
{
  "CRIM": 0.03,
  "ZN": 18.0,
  "INDUS": 2.31,
  "CHAS": 0,
  "NOX": 0.538,
  "RM": 6.575,
  "AGE": 65.2,
  "DIS": 4.09,
  "RAD": 1,
  "TAX": 296.0,
  "PTRATIO": 15.3,
  "B": 396.9,
  "LSTAT": 4.98
}
```

Returns predicted median house value in $1,000s.

---

## Author

**Shourya Marwaha**
MSc Data Science & Analytics, University of Leeds | MBA (Finance) | BTech (Mechanical Engineering)

[LinkedIn](https://www.linkedin.com/in/shouryamarwaha/) · [shouryamarwaha@gmail.com](mailto:shouryamarwaha@gmail.com)
