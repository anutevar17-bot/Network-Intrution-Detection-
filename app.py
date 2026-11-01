
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

# Load model
model = joblib.load("intrusion_detection_model.pkl")
features = joblib.load("feature_columns.pkl")

st.title("🛡️ Network Intrusion Detection System")
st.write("Machine Learning Based Cybersecurity Dashboard")

st.divider()

col1, col2 = st.columns(2)

col1.metric("Algorithm", "Random Forest")
col2.metric("Detection", "Multi-class Classification")

st.divider()

st.header("📂 Upload Network Traffic CSV")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        st.success("CSV uploaded successfully!")

        st.subheader("Uploaded Dataset")
        st.dataframe(data.head(20))

        X_new = data.drop(
            columns=["Attack_type"],
            errors="ignore"
        )

        missing = [
            col for col in features
            if col not in X_new.columns
        ]

        if missing:
            st.error(
                "Missing columns: " + ", ".join(missing)
            )
        else:
            X_new = X_new[features]

            predictions = model.predict(X_new)

            result = data.copy()
            result["Predicted_Category"] = predictions

            st.success("Prediction completed!")

            st.subheader("Prediction Results")
            st.dataframe(result)

            st.subheader("Prediction Distribution")
            st.bar_chart(
                pd.Series(predictions).value_counts()
            )

            st.download_button(
                "Download Prediction Results",
                result.to_csv(index=False),
                "network_predictions.csv",
                "text/csv"
            )

    except Exception as e:
        st.error(f"Error: {e}")
