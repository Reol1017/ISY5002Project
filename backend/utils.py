import pandas as pd
import pickle

# 加载 scaler, bagofwords, 和模型
with open('../Models/KTAS_scaler.pkl', 'rb') as file:
    ktas_scaler = pickle.load(file)

with open('../Models/nlp_complain.pkl', 'rb') as file:
    nlp_complain = pickle.load(file)

with open('../Models/KTAS_model.pkl', 'rb') as file:
    ktas_model = pickle.load(file)

# 预定义模型所需的完整特征列表（包含所有数值特征和文本特征）
ktas_features = [
    'Age', 'Patients number per hour', 'NRS_pain', 'RR', 'Saturation', 
    'Arrival mode_Private ambulance', 'Arrival mode_Private car', 
    'Injury_non-injured', 'Arrival mode_119 use', 'Mental_Pain Response'
] + list(nlp_complain.get_feature_names_out())  # 添加 nlp_complain 特征

def make_prediction(age, No_Patients_in_ER, RR, Saturation, NRS_pain, mode_of_transport, Chief_complain, injury, Mental_state):
    data = {
        "Age": age,
        "RR": RR,
        "Saturation": Saturation,
        'Patients number per hour': No_Patients_in_ER,
        'NRS_pain': NRS_pain,
        'Arrival mode_Private ambulance': mode_of_transport,
        'Injury_non-injured': injury,
        'Chief_complain': Chief_complain,
        'Mental_Pain Response': Mental_state
    }

    # 创建初始 DataFrame
    df_new = pd.DataFrame(data, index=[0])

    # 补充缺失列
    for col in ['Arrival mode_Private car', 'Arrival mode_119 use']:
        df_new[col] = 0

    # 数值特征和分类特征分离
    df_new_numeric = df_new[['Age', 'Patients number per hour', 'NRS_pain', 'RR', 'Saturation']]
    df_new_categoric = df_new[['Arrival mode_Private ambulance', 'Arrival mode_Private car', 'Injury_non-injured', 'Arrival mode_119 use', 'Mental_Pain Response']]
    df_new1 = pd.concat([df_new_numeric, df_new_categoric], axis=1)

    # 转换分类特征为数值
    df_new1["Injury_non-injured"] = df_new1["Injury_non-injured"].replace({'no': 0, 'yes': 1})
    df_new1["Mental_Pain Response"] = df_new1["Mental_Pain Response"].replace({'pain_response': 1, 'Normal': 0})
    df_new1["Arrival mode_Private ambulance"] = df_new1["Arrival mode_Private ambulance"].replace({'Private ambulance': 1, 'car': 0, '119_use': 0})
    df_new1["Arrival mode_Private car"] = df_new1["Arrival mode_Private car"].replace({'car': 1, 'Private ambulance': 0, '119_use': 0})
    df_new1["Arrival mode_119 use"] = df_new1["Arrival mode_119 use"].replace({'119_use': 1, 'car': 0, 'Private ambulance': 0})

    # 标准化数据
    df_scaled = ktas_scaler.transform(df_new1)
    df_new1 = pd.DataFrame(data=df_scaled, columns=df_new1.columns)

    # 文本特征向量化
    CF4 = nlp_complain.transform(df_new['Chief_complain'])
    df_new_comp = pd.DataFrame(columns=nlp_complain.get_feature_names_out(), data=CF4.toarray(), index=df_new.index)
    df_new = pd.concat([df_new1, df_new_comp], axis=1)

    # 补全缺失的列，确保与训练时特征顺序匹配
    df_new = df_new.reindex(columns=ktas_features, fill_value=0)

    # 使用模型进行预测
    prediction = ktas_model.predict(df_new)

    # 返回预测结果
    return "EMERGENCY" if prediction[0] == 1 else "NON-EMERGENCY"


with open('../Models/WT_scaler.pkl', 'rb') as file:
    wt_scaler = pickle.load(file)
    
with open('../Models/nlp_diagnosis.pkl', 'rb') as file:
    nlp_diagnosis = pickle.load(file)

with open('../Models/WT_model.pkl', 'rb') as file:
    wt_model = pickle.load(file)

# 动态添加 nlp_diagnosis 特征
scaler_features = [
    "Eligibility Class", "Emergency", "Arrival Hour", "Currently Admitted Patients", 
    "temp", "humidity", "windspeed", "uvindex", "visibility", "Gender", "Is Weekend", "Time of Day"
] + list(nlp_diagnosis.get_feature_names_out())  # 添加 nlp_diagnosis 特征

def make_waiting_time_prediction(diagnosis, eligibility, Emergency, hour, no_patients, temp, humidity, windspeed, uvindex, visibility, gender, Is_Weekend, Time_Day):
    # 创建输入数据
    data = {
        "Main Diagnosis": [diagnosis],
        'Eligibility Class': [eligibility],
        'Emergency': [Emergency],
        'Arrival Hour': [hour],
        "Currently Admitted Patients": [no_patients],
        "temp": [temp],
        "humidity": [humidity],
        "windspeed": [windspeed],
        "uvindex": [uvindex],
        "visibility": [visibility],
        "Gender": [gender],
        "Is Weekend": [Is_Weekend],
        "Time of Day": [Time_Day]
    }

    # 转换为 DataFrame
    df_new = pd.DataFrame(data)

    # 载入 NLP 模型并向量化 'Main Diagnosis'
    with open('../Models/nlp_diagnosis.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
    df_new_encoded = vectorizer.transform(df_new['Main Diagnosis'])
    df_new_features = pd.DataFrame(df_new_encoded.toarray(), columns=vectorizer.get_feature_names_out())

    # 转换分类变量
    df_new["Eligibility Class"] = df_new["Eligibility Class"].replace({'ROYAL COMMISSION': 0, 'EXEMPT': 1, 'INSURANCE': 2, 'CASH': 3})
    df_new["Gender"] = df_new["Gender"].replace({'Female': 0, 'Male': 1})
    df_new["Is Weekend"] = df_new["Is Weekend"].replace({'no': 0, 'yes': 1})
    df_new["Time of Day"] = df_new["Time of Day"].replace({'Morning': 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3})

    # 合并所有特征
    df_new = df_new.drop(columns=['Main Diagnosis'])
    df_final = pd.concat([df_new_features, df_new], axis=1)

    # 载入标准化模型并应用
    with open('../Models/WT_scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    df_scaled = scaler.transform(df_final)

    # 确保列顺序
    df_final_scaled = pd.DataFrame(df_scaled, columns=df_final.columns).reindex(columns=scaler.feature_names_in_, fill_value=0)

    # 加载等待时间预测模型并预测
    with open('../Models/WT_model.pkl', 'rb') as file:
        wt_model = pickle.load(file)
    prediction = wt_model.predict(df_final_scaled)

    return prediction[0]


with open('../Models/iso_forest_scaler.pkl', 'rb') as file:
    iso_scaler = pickle.load(file)

with open('../Models/iso_forest_model.pkl', 'rb') as file:
    iso_model = pickle.load(file)


def anomaly_detection_prediction(diagnosis, month, time, day):
    # 创建输入数据，包含诊断文本和时间特征
    data = {
        "Month": [month],
        "Hour": [time],
        "Weekday": [day]
    }

    # 转换诊断文本特征为向量
    diagnosis_vector = nlp_diagnosis.transform([diagnosis])
    diagnosis_features = pd.DataFrame(diagnosis_vector.toarray(), columns=nlp_diagnosis.get_feature_names_out())

    # 将时间特征转为 DataFrame
    time_features = pd.DataFrame(data)

    # 合并诊断和时间特征，形成最终的特征 DataFrame
    anomaly_features = pd.concat([diagnosis_features, time_features], axis=1)

    # 使用预训练的标准化器进行特征缩放
    anomaly_features_scaled = iso_scaler.transform(anomaly_features)

    # 使用 Isolation Forest 模型进行异常检测
    prediction = iso_model.predict(anomaly_features_scaled)

    # 返回预测结果
    if prediction[0] == -1:
        return 'THIS CASE HAS A HIGHER PROBABILITY OF BEING AN ANOMALY'
    else:
        return 'THIS CASE IS NOT AN ANOMALY'