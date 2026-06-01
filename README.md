#  Smart Crime Analytics System

### Hybrid Machine Learning Framework for Geospatial Crime Prediction & Analysis

---

##  Overview

CrimeVision AI is a machine learning-based system designed to analyze, predict, and visualize crime patterns using geospatial and temporal data.

This project combines data analytics, machine learning, and interactive visualization to provide insights into crime trends and support decision-making.

---

##  Features

*  Crime data analysis and visualizatioN
*  Crime type prediction using ML models
*  Geospatial crime mapping
*  Interactive dashboard using Streamlit
*  Crime pattern insights (area & time-based)
*  Dynamic filtering (area, time, location)

---

##  Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Seaborn, Matplotlib
* Streamlit

---

##  Project Structure

```
CrimeVision-AI/
│
├── app.py                 # Main app entry point
├── home.py                # Home page UI
├── dashboard.py          # Dashboard & analysis
├── about.py              # About page
│
├── crime_model.pkl       # Trained ML model
├── le_type.pkl           # Label encoder (crime type)
├── le_area.pkl           # Label encoder (area)
│
├── sample_data.csv       # Dataset
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

##  Installation

1. Clone the repository:

```
https://github.com/Sayandip10/Smart-Crime-Analytics-System
```

2. Navigate to the project folder:

```
cd CrimeVision-AI
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the App

```
python -m streamlit run app.py
```

---

##  Machine Learning Model

* Model Used: **XGBoost Classifier**
* Task: Crime Type Prediction
* Input Features:

  * Area (Encoded)
  * Latitude
  * Longitude
  * Hour

---

##  Screenshots

<img width="1524" height="711" alt="image" src="https://github.com/user-attachments/assets/01d5a8d3-2db9-461a-b79c-8eedfeb2061e" />
<img width="1034" height="602" alt="image" src="https://github.com/user-attachments/assets/000ce34c-7438-47e4-bca1-0e868de7d872" />
<img width="1033" height="460" alt="image" src="https://github.com/user-attachments/assets/434267c6-4ad3-433c-b1d0-e10d761261b9" />




---

##  Future Improvements

* Improve model accuracy
* Add real-time data integration
* Deploy as web application
* Add user authentication

---




---

##  License

This project is for academic purposes.
