# AI-Powered Traffic Flow Optimization System

An AI-based traffic management system that detects vehicles from video, analyzes traffic conditions, predicts congestion, and recommends traffic signal timings.

## 🌐 Live Demo

[Open Live Demo](https://bhumikajonnalagadda.github.io/AI-Traffic-Flow-Optimization/)

## 💻 GitHub Repository

[View Source Code](https://github.com/Bhumikajonnalagadda/AI-Traffic-Flow-Optimization)

## 🚀 Features

* 🚗 YOLO-based vehicle detection
* 📊 Vehicle counting
* 🚦 Traffic density classification
* ⚠️ Traffic congestion prediction
* ⏱️ Green signal time recommendation
* 🔄 Traffic flow simulation
* 📈 Traffic analysis visualization
* 🌐 Flask web dashboard

## 🛠️ Technologies Used

* Python
* Flask
* YOLO
* Ultralytics
* OpenCV
* Pandas
* Scikit-learn
* HTML
* CSS
* JavaScript
* Chart.js

## 🤖 Machine Learning

A Decision Tree Classifier is used to predict traffic congestion based on:

* Vehicle count
* Average speed

The project uses a sample traffic dataset for demonstration and testing.

## 📁 Project Structure

```text
AI_Traffic_Flow_Optimization/
│
├── app.py
├── vehicle_detection.py
├── requirements.txt
├── README.md
├── index.html
│
├── data/
│   ├── traffic_data.csv
│   └── videos/
│       └── traffic.mp4
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

If required, install YOLO:

```bash
python -m pip install ultralytics
```

### 2. Run the application

```bash
python app.py
```

### 3. Open in browser

```text
http://127.0.0.1:5000
```

## 🧪 Testing

The following features were tested successfully:

* YOLO vehicle detection
* Traffic analysis
* Traffic simulation
* Traffic analysis chart
* Traffic density indicator

## ⚠️ Limitations

This project uses a small sample dataset and a demonstration traffic video. The simulation and model results are intended for educational and prototype purposes rather than real-world traffic control.

## 🔮 Future Enhancements

* Real-time traffic camera integration
* Vehicle tracking
* Real-world speed estimation
* Larger traffic datasets
* Adaptive traffic signal control
* Multiple intersection support
* Cloud deployment

## 👩‍💻 Author

**Bhumika Jonnalagadda**

GitHub: [Bhumikajonnalagadda](https://github.com/Bhumikajonnalagadda)
