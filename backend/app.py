# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import requests
import pandas as pd
from datetime import datetime
from utils import make_prediction, make_waiting_time_prediction, anomaly_detection_prediction

# 创建 Flask 应用
app = Flask(__name__)
# CORS(app, resources={r"/predict_ktas": {"origins": "http://localhost:5173"}})  # 允许指定来源的跨域请求
CORS(app, resources={r"/*": {"origins": "*"}})

# 天气 API 的 URL 和密钥
WEATHER_API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
WEATHER_API_KEY = "EZLL9NFRQP9M3FGWRJAPSMLKG"  # 替换为实际的 API 密钥

def get_weather_data(city):
    """Fetch current weather data for the specified city using Visual Crossing API."""
    current_date = datetime.now().strftime('%Y-%m-%d')
    response = requests.get(f"{WEATHER_API_URL}/{city}/{current_date}", params={
        "key": WEATHER_API_KEY,
        "include": "current"
    })
    
    if response.status_code == 200:
        weather_data = response.json().get('currentConditions', {})
        return {
            "temp": weather_data.get("temp", 0),
            "humidity": weather_data.get("humidity", 0),
            "windspeed": weather_data.get("windspeed", 0),
            "uvindex": weather_data.get("uvindex", 0),
            "visibility": weather_data.get("visibility", 0)
        }
    else:
        return None

@app.route('/predict_ktas', methods=['POST'])
def predict_ktas():
    # 从请求中获取 JSON 数据
    data = request.json

    print(data)
    
    # 提取请求中的各项参数
    age = data.get("age")
    No_Patients_in_ER = data.get("No_Patients_in_ER")
    RR = data.get("RR")
    Saturation = data.get("Saturation")
    NRS_pain = data.get("NRS_pain")
    mode_of_transport = data.get("mode_of_transport")
    Chief_complain = data.get("Chief_complain")
    injury = data.get("injury")
    Mental_state = data.get("Mental_state")
    
    # 调用 make_prediction 函数进行预测
    ktas_prediction = make_prediction(age, No_Patients_in_ER, RR, Saturation, NRS_pain, mode_of_transport, Chief_complain, injury, Mental_state)
    emergency = 1 if ktas_prediction == "EMERGENCY" else 0

    # Step 2: 获取天气数据
    city = data.get("city")  # 获取天气数据所需的城市名称
    weather_data = get_weather_data(city)
    if weather_data is None:
        return jsonify({"error": "Unable to fetch weather data"}), 500
    
    # Step 3: 使用 Waiting Time 模型进行预测
    diagnosis = data.get("diagnosis")
    eligibility = data.get("eligibility")
    hour = datetime.now().hour  # 使用当前小时
    no_patients = No_Patients_in_ER
    gender = data.get("gender")
    today = datetime.today().weekday()
    is_weekend = 1 if today >= 5 else 0  # 周六 (5) 和周日 (6) 为周末
    time_day = data.get("time_day")

    waiting_time_prediction = make_waiting_time_prediction(
        diagnosis, eligibility, emergency, hour, no_patients, 
        weather_data["temp"], weather_data["humidity"], 
        weather_data["windspeed"], weather_data["uvindex"], 
        weather_data["visibility"], gender, is_weekend, time_day
    )

    month = datetime.now().month
    day = datetime.now().day
    anomaly_prediction = anomaly_detection_prediction(diagnosis, month, hour, day)

    

    # 返回预测结果
    return jsonify({
        "ktas": ktas_prediction,
        "waiting_time": waiting_time_prediction,
        "anomaly_detection": anomaly_prediction
    })

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
