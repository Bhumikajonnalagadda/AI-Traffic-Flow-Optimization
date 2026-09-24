from flask import Flask, render_template, jsonify
from vehicle_detection import detect_vehicles
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# --------------------------------------------------
# Load traffic dataset
# --------------------------------------------------

data_file = "data/traffic_data.csv"

if not os.path.exists(data_file):
    print("traffic_data.csv not found.")
    exit()

data = pd.read_csv(data_file)

X = data[["vehicle_count", "average_speed"]]
y = data["congestion_level"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)


# --------------------------------------------------
# Shared YOLO vehicle count
# --------------------------------------------------

current_vehicle_count = None


# --------------------------------------------------
# Get current vehicle count
# --------------------------------------------------

def get_vehicle_count():

    latest = data.iloc[-1]

    if current_vehicle_count is not None:
        return current_vehicle_count

    return int(latest["vehicle_count"])


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# Analyze Traffic
# --------------------------------------------------

@app.route("/analyze")
def analyze():

    vehicle_count = get_vehicle_count()

    latest = data.iloc[-1]
    average_speed = float(latest["average_speed"])

    prediction_data = pd.DataFrame(
        [[vehicle_count, average_speed]],
        columns=["vehicle_count", "average_speed"]
    )

    prediction = model.predict(prediction_data)[0]

    # Traffic density
    if vehicle_count <= 15:
        traffic_density = "Low"
    elif vehicle_count <= 25:
        traffic_density = "Medium"
    elif vehicle_count <= 40:
        traffic_density = "High"
    else:
        traffic_density = "Very High"

    # Signal timing
    if traffic_density == "Low":
        green_time = 30
    elif traffic_density == "Medium":
        green_time = 45
    elif traffic_density == "High":
        green_time = 60
    else:
        green_time = 90

    return jsonify({
        "vehicle_count": vehicle_count,
        "average_speed": average_speed,
        "traffic_density": traffic_density,
        "congestion_level": prediction,
        "green_time": green_time,
        "model_accuracy": round(accuracy * 100, 2),
        "message": "Traffic analyzed successfully."
    })


# --------------------------------------------------
# Traffic Simulation
# --------------------------------------------------

@app.route("/simulate")
def simulate():

    vehicle_count = get_vehicle_count()

    latest = data.iloc[-1]
    average_speed = float(latest["average_speed"])

    prediction_data = pd.DataFrame(
        [[vehicle_count, average_speed]],
        columns=["vehicle_count", "average_speed"]
    )

    prediction = model.predict(prediction_data)[0]

    # Traffic density
    if vehicle_count <= 15:
        traffic_density = "Low"
    elif vehicle_count <= 25:
        traffic_density = "Medium"
    elif vehicle_count <= 40:
        traffic_density = "High"
    else:
        traffic_density = "Very High"

    # Signal timing
    if traffic_density == "Low":
        green_time = 30
    elif traffic_density == "Medium":
        green_time = 45
    elif traffic_density == "High":
        green_time = 60
    else:
        green_time = 90

    # Simple simulation
    vehicles_processed = min(
        vehicle_count,
        green_time
    )

    remaining_vehicles = (
        vehicle_count - vehicles_processed
    )

    processing_percentage = (
        vehicles_processed / vehicle_count
    ) * 100

    return jsonify({
        "initial_vehicles": vehicle_count,
        "green_time": green_time,
        "vehicles_processed": vehicles_processed,
        "remaining_vehicles": remaining_vehicles,
        "processing_percentage": round(
            processing_percentage,
            2
        ),
        "model_accuracy": round(
            accuracy * 100,
            2
        ),
        "congestion_level": prediction
    })


# --------------------------------------------------
# YOLO Vehicle Detection
# --------------------------------------------------

@app.route("/detect-vehicles")
def detect_vehicles_route():

    global current_vehicle_count

    video_path = "data/videos/traffic.mp4"

    if not os.path.exists(video_path):

        return jsonify({
            "vehicle_count": 0,
            "message": "Traffic video not found."
        })

    # Run YOLO
    detected_count = detect_vehicles(video_path)

    # Save YOLO result
    current_vehicle_count = detected_count

    return jsonify({
        "vehicle_count": current_vehicle_count,
        "message": "YOLO vehicle detection completed."
    })


# --------------------------------------------------
# Run Flask
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)