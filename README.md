# Network Intrusion Detection Using Machine Learning

## Project Overview
This project uses machine learning to classify network traffic records from the RT-IoT2022 dataset into the categories represented by the `Attack_type` target.

## Technologies
- Python
- Pandas
- Scikit-learn
- Random Forest and Decision Tree
- Streamlit

## Project Files
- `app.py` — Streamlit dashboard application
- `intrusion_detection_model.pkl` — trained machine-learning model
- `feature_columns.pkl` — feature-column order used by the model
- `requirements.txt` — Python dependencies

## Run Locally
Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

## Important
Generate the model and feature-column files from the same trained model and preprocessing workflow used by this project. Confirm the dataset's normal and attack label mapping before presenting binary intrusion-detection results.
