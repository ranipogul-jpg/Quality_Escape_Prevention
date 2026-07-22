import streamlit as st

st.set_page_config(
    page_title="Quality Escape Prevention",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Quality Escape Prevention")
st.write("Machine Learning Prediction System")

st.sidebar.title("Navigation")
st.sidebar.write("Manufacturing AI Project")
st.sidebar.write("MindForgeAI Internship 2026")

st.header("Project Overview")
st.write("""
This application predicts whether a manufactured
product should undergo manual inspection
before dispatch using Machine Learning.
""")

st.subheader("Objective")
st.write("""
Reduce defective products reaching customers.

Improve quality control.

Reduce inspection cost.

Increase customer satisfaction.
""")

st.subheader("Model Information")
st.write("Algorithm : Random Forest")
st.write("Prediction : Inspection Required / No Inspection Required")


import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Quality Escape Prevention",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Quality Escape Prevention")
st.write("Machine Learning Prediction System")

st.sidebar.title("Navigation")
st.sidebar.write("Manufacturing AI Project")
st.sidebar.write("MindForgeAI Internship 2026")

st.header("Project Overview")
st.write("""
This application predicts whether a manufactured
product should undergo manual inspection
before dispatch using Machine Learning.
""")

st.subheader("Objective")
st.write("""
Reduce defective products reaching customers.
Improve quality control.
Reduce inspection cost.
Increase customer satisfaction.
""")

st.subheader("Model Information")
st.write("Algorithm : Random Forest")
st.write("Prediction : Inspection Required / No Inspection Required")

# --- Load Model, Scaler, and Encoder ---
try:
    model = joblib.load("../models/best_model.pkl")
    scaler = joblib.load("../models/scaler.pkl")
    label_encoder = joblib.load("../models/label_encoder.pkl")
except Exception as e:
    st.warning(f"Could not load model artifacts. Ensure they are saved in the '../models/' folder. Error: {e}")

# --- Machine Sensor Input Section ---
st.header("Machine Sensor Input")

# AI4I 2020 Dataset Features
type_val = st.selectbox("Product Type", ["Low (L)", "Medium (M)", "High (H)"])
air_temp = st.number_input("Air temperature [K]", min_value=200.0, max_value=400.0, value=298.0)
process_temp = st.number_input("Process temperature [K]", min_value=200.0, max_value=400.0, value=308.0)
speed = st.number_input("Rotational speed [rpm]", min_value=0, max_value=5000, value=1500)
torque = st.number_input("Torque [Nm]", min_value=0.0, max_value=200.0, value=40.0)
tool_wear = st.number_input("Tool wear [min]", min_value=0, max_value=500, value=50)

# Encode Type if label encoder is available
if 'label_encoder' in locals() and label_encoder is not None:
    try:
        # Match string formatting if necessary, or use direct transform
        encoded_type = label_encoder.transform([type_val])[0]
    except:
        encoded_type = 0 # Fallback
else:
    # Manual fallback if encoder isn't loaded
    encoded_type = 0 if type_val.startswith("Low") else (1 if type_val.startswith("Medium") else 2)

predict_btn = st.button("Predict")

if predict_btn:
    # Create DataFrame matching training columns order
    input_df = pd.DataFrame([[
        encoded_type,
        air_temp,
        process_temp,
        speed,
        torque,
        tool_wear
    ]], columns=[
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]"
    ])

    try:
        # Scale input data
        scaled_input = scaler.transform(input_df)
        
        # Predict
        prediction = model.predict(scaled_input)
        probability = model.predict_proba(scaled_input)

        # Display Result
        if prediction[0] == 1:
            st.error("⚠️ Inspection Required (Defect / Quality Escape Risk)")
        else:
            st.success("✅ No Inspection Required (Normal Operation)")

        confidence = probability.max() * 100
        st.write(f"Prediction Confidence : {confidence:.2f}%")
        
    except Exception as e:
        st.error(f"Error during prediction execution: {e}")

        import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --- Page Configuration ---
st.set_page_config(
    page_title="Quality Escape Prevention",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Quality Escape Prevention")
st.write("Machine Learning Prediction System")

# --- Sidebar ---
st.sidebar.title("Navigation")
st.sidebar.write("Manufacturing AI Project")
st.sidebar.write("MindForgeAI Internship 2026")

st.header("Project Overview")
st.write("""
This application predicts whether a manufactured
product should undergo manual inspection
before dispatch using Machine Learning.
""")

st.subheader("Objective")
st.write("""
Reduce defective products reaching customers.
Improve quality control.
Reduce inspection cost.
Increase customer satisfaction.
""")

st.subheader("Model Information")
st.write("Algorithm : Random Forest")
st.write("Prediction : Inspection Required / No Inspection Required")

# --- Load Saved Artifacts ---
@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load("../models/best_model.pkl")
        scaler = joblib.load("../models/scaler.pkl")
        label_encoder = joblib.load("../models/label_encoder.pkl")
    except Exception:
        # Fallback if path is executed from root directory
        model = joblib.load("models/best_model.pkl")
        scaler = joblib.load("models/scaler.pkl")
        label_encoder = joblib.load("models/label_encoder.pkl")
    return model, scaler, label_encoder

try:
    model, scaler, label_encoder = load_artifacts()
except Exception as e:
    st.error(f"Error loading model artifacts: {e}")

# --- Machine Sensor Input Section ---
st.header("Machine Sensor Input")

machine_type = st.selectbox("Product Type", ["L", "M", "H"])
air_temperature = st.number_input("Air temperature [K]", value=298.0)
process_temperature = st.number_input("Process temperature [K]", value=308.0)
rotational_speed = st.number_input("Rotational speed [rpm]", value=1500)
torque = st.number_input("Torque [Nm]", value=40.0)
tool_wear = st.number_input("Tool wear [min]", value=0)

# --- Predict Button & Logic ---
predict_button = st.button("🔍 Predict Inspection Status")

if predict_button:
    # Create DataFrame with exact training column names and order
    input_data = pd.DataFrame({
        "Air temperature [K]": [air_temperature],
        "Process temperature [K]": [process_temperature],
        "Rotational speed [rpm]": [rotational_speed],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear],
        "Type": [machine_type]
    })

    try:
        # Encode categorical values
        if 'label_encoder' in locals() and label_encoder is not None:
            input_data["Type"] = label_encoder.transform(input_data["Type"])

        # Scale the input
        scaled_data = scaler.transform(input_data)

        # Make Prediction
        prediction = model.predict(scaled_data)
        probability = model.predict_proba(scaled_data)

        # Display Results
        st.subheader("Prediction Result")

        if prediction[0] == 1:
            st.error("⚠️ Inspection Required")
        else:
            st.success("✅ No Inspection Required")

        # Display Confidence
        confidence = probability.max() * 100
        st.write(f"Confidence Score: {confidence:.2f}%")

        # Display Recommendation
        if prediction[0] == 1:
            st.warning("""
            Recommendation:
            • Send the unit for manual inspection.
            • Check machine settings.
            • Verify sensor readings before dispatch.
            """)
        else:
            st.info("""
            Recommendation:
            • Unit passed quality prediction.
            • Continue with normal dispatch process.
            """)

        # Show Entered Values
        st.subheader("Entered Machine Values")
        st.dataframe(input_data)

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

        import streamlit as st
import pandas as pd
import joblib
import time
from pathlib import Path

# --- Page Configuration ---
st.set_page_config(
    page_title="Quality Escape Prevention",
    page_icon="🏭",
    layout="wide"
)

# --- Sidebar Details ---
st.sidebar.title("Navigation")
st.sidebar.write("Manufacturing AI Project")
st.sidebar.write("MindForgeAI Internship 2026")

st.sidebar.markdown("---")
st.sidebar.header("Project Details")
st.sidebar.write("Project : Quality Escape Prevention")
st.sidebar.write("Model : Random Forest")
st.sidebar.write("Type : Binary Classification")

# --- Main App Title ---
st.title("🏭 Quality Escape Prevention")
st.write("Machine Learning Prediction System")

st.header("Project Overview")
st.write("""
This application predicts whether a manufactured
product should undergo manual inspection
before dispatch using Machine Learning.
""")

st.subheader("Objective")
st.write("""
Reduce defective products reaching customers.
Improve quality control.
Reduce inspection cost.
Increase customer satisfaction.
""")

st.subheader("Model Information")
st.write("Algorithm : Random Forest")
st.write("Prediction : Inspection Required / No Inspection Required")

# --- Step 9.4.1: Handle Model Loading Errors Safely ---
MODEL_PATH = Path("../models/best_model.pkl")
SCALER_PATH = Path("../models/scaler.pkl")
ENCODER_PATH = Path("../models/label_encoder.pkl")

# Fallback paths if running from root directory instead of app/ folder
if not MODEL_PATH.exists():
    MODEL_PATH = Path("models/best_model.pkl")
    SCALER_PATH = Path("models/scaler.pkl")
    ENCODER_PATH = Path("models/label_encoder.pkl")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    label_encoder = joblib.load(ENCODER_PATH) if ENCODER_PATH.exists() else None
except FileNotFoundError:
    st.error("Model, Scaler, or Encoder file not found. Please check your file paths.")
    st.stop()

# --- Machine Sensor Input Section ---
st.header("Machine Sensor Input")

machine_type = st.selectbox("Product Type", ["L", "M", "H"])
air_temperature = st.number_input("Air temperature [K]", min_value=200.0, max_value=400.0, value=298.0)
process_temperature = st.number_input("Process temperature [K]", min_value=200.0, max_value=400.0, value=308.0)
rotational_speed = st.number_input("Rotational speed [rpm]", min_value=0, max_value=5000, value=1500)
torque = st.number_input("Torque [Nm]", min_value=0.0, max_value=200.0, value=40.0)
tool_wear = st.number_input("Tool wear [min]", min_value=0, max_value=500, value=0)

# --- Predict Button & Validation Logic ---
predict_button = st.button("🔍 Predict Inspection Status")

if predict_button:
    # Step 9.4.2: Check Input Values
    if tool_wear < 0:
        st.error("Tool wear cannot be negative.")
        st.stop()

    if rotational_speed <= 0:
        st.error("Rotational speed must be greater than 0.")
        st.stop()

    st.success("Input values are valid.")

    # Step 9.4.4: Show a Progress Bar
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    # Create Input DataFrame
    input_data = pd.DataFrame({
        "Air temperature [K]": [air_temperature],
        "Process temperature [K]": [process_temperature],
        "Rotational speed [rpm]": [rotational_speed],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear],
        "Type": [machine_type]
    })

    try:
        # Encode categorical values if label encoder exists
        if label_encoder is not None:
            input_data["Type"] = label_encoder.transform(input_data["Type"])

        # Scale the input data
        scaled_data = scaler.transform(input_data)

        # Make Prediction
        prediction = model.predict(scaled_data)
        probability = model.predict_proba(scaled_data)

        # Calculate Confidence
        confidence = probability.max() * 100

        # Step 9.4.5: Display Results in a Professional Columns Layout
        st.subheader("Prediction Result")
        
        col1, col2 = st.columns(2)
        with col1:
            pred_text = "Inspection Required" if prediction[0] == 1 else "No Inspection Required"
            st.metric("Prediction", pred_text)
        with col2:
            st.metric("Confidence", f"{confidence:.2f}%")

        # Color-coded Status & Recommendation Box
        if prediction[0] == 1:
            st.error("⚠️ **Inspection Required**")
            st.warning("""
            Recommendation:
            • Send the unit for manual inspection.
            • Check machine settings.
            • Verify sensor readings before dispatch.
            """)
        else:
            st.success("✅ **No Inspection Required**")
            st.info("""
            Recommendation:
            • Unit passed quality prediction.
            • Continue with normal dispatch process.
            """)

        # Step 9.4.7: Show Prediction Probability Breakdown
        st.subheader("Prediction Probability Breakdown")
        st.write(f"No Inspection Probability: **{probability[0][0]*100:.2f}%**")
        st.write(f"Inspection Required Probability: **{probability[0][1]*100:.2f}%**")

        # Step 9.4.6: Expandable Input Summary
        with st.expander("View Input Data"):
            st.dataframe(input_data)

        # Step 9.4.8: Add a Warning Box for ML Models
        st.warning("""
        This prediction is generated by a Machine Learning model.
        Always confirm with a quality engineer before making critical production decisions.
        """)

    except Exception as e:
        st.error(f"An error occurred during prediction processing: {e}")

# --- Step 9.4.10: Add Footer ---
st.markdown("---")
st.write("Developed for MindForgeAI Internship 2026")