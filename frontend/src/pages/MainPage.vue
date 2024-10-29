<template>
    <div class="main-page">
      <div class="patient-text">
        <p>Patient</p>
      </div>
      <div class="main-box">
        <!-- 左侧 30% -->
        <div class="section left-section">
            <div class="profile">
                <div class="small-profile"></div>
                <div class="mid-profile"></div>
                <div class="main-profile">
                    <!-- 两个半透明圆形装饰 -->
                    <div class="circle circle1"></div>
                    <div class="circle circle2"></div>
                    <div class="personal-pic">
                        <img src="../assets/yoyo.jpg" alt="Profile Picture">    
                    </div>
                    <div class="personal-info">
                        <p style="font-size: 90%;">Personal Infomation</p>
                        <p style="font-size: 200%;">{{ name }}</p>
                        <br>
                        <p style="font-size: 70%;">ID:</p>
                        <p style="font-size: 120%;">{{ id }}</p>
                        <p style="font-size: 180%;">{{ gender }}</p>
                    </div>
                </div>
            </div>
            <div class="symptom-description">
                <div class="symptom-description-title">
                    <p style="font-size: 120%; ">Symptom Description</p>
                    <el-button round style="background-color: #f4f5f9; right: 0%;">Download Report</el-button>
                </div>
                <div class="symptom-description-text">
                    <p>{{ diagnosis }}</p>
                </div>
                <div class="symptom-description-button">
                    <el-button-group>
                        <el-button type="primary" style="background-color: #fff; color: #161616;">Monthly</el-button>
                        <el-button type="primary" style="background-color: #fff; color: #161616;">Weekly</el-button>
                        <el-button type="primary" style="background-color: #1eabe7;">Today</el-button>
                    </el-button-group>
                </div>
            </div>
            <div class="medical-history">
                <div class="medical-history-title">
                    <p style="font-size: 120%; ">Medical History</p>
                    <p style="right: 0%;">EFFECT: NO</p>
                </div>
                <div class="medical-history-text">
                    <p v-html="medical_History"></p>
                </div>
                
            </div>
        </div>
        <!-- 中间 30% -->
        <div class="section center-section">
            <div class="infomation">
                <div class="info-container">
                    <hr>
                    <br>
                    <br>
                    <div class="info-item">
                        <span style="font-weight:bold;">AGE:</span>
                        <span style="font-weight: 500; margin-left: auto;">{{ age }}</span>
                    </div>
                    <hr>
                    <div class="info-item">
                        <span style="font-weight:bold;">Respiratory Rate:</span>
                        <span style="font-weight: 500; margin-left: auto;">{{ rr }} breaths per minute</span>
                    </div>
                    <div class="info-item">
                        <span style="font-weight:bold;">Saturation:</span>
                        <span style="font-weight: 500; margin-left: auto;">{{saturation}}% on room air</span>
                    </div>
                    <div class="info-item">
                        <span style="font-weight:bold;">Chief Complaint:</span>
                        <span style="font-weight: 500; margin-left: auto; text-align: right; width: 50%;">{{ chief_complaint }}</span>
                    </div>
                    <div class="info-item">
                        <span style="font-weight:bold;">Mental Pain:</span>
                        <span style="font-weight: 500; margin-left: auto; text-align: right; width: 50%;">{{ mental_pain }}</span>
                    </div>
                    <hr>
                    <div class="info-item">
                        <span style="font-weight:bold; color: #00d7b7;">NO Patients in ER: {{ no_patients_in_ER }}</span>
                        <span style="font-weight:bold; margin-left: auto; color: #00d7b7;">{{ arrival_time }}</span>
                    </div>
                </div>
                <div class="test-result"> Test Resutl AI</div>
            </div>
            <div class="ai-result">
                <div class="ai-result-container">
                    <div class="ai-result-pic">
                        <img src="../assets/ai result.jpg" alt="Profile Picture"> 
                        <p v-if="ktas == 'NON-EMERGENCY'" style="position: absolute; top: 10%; right: 4%; font-size: 110%;color: #000000;">NON<br>EMERGENCY</p>
                        <p v-else style="position: absolute; top: 10%; right: 4%; font-size: 110%;color: red;">EMERGENCY</p>
                        <p style="position: absolute;top: 50%; right: 8%; font-size: 80%; color: #cccccc;">Waiting Time</p>
                        <p style="position: absolute;top: 70%; right: 13%; font-size: 120%; color: #ffffff;">{{formattedWaitingTime}}</p>
                    </div>
                    <div style="bottom: 1px; position: absolute;">
                        <p>**<span style="color: red; font-weight: bold;">H.pylori-associated chronic gastritis</span>** and recommends **<span style="color: #00c9c7; font-weight: bold;">triple therapy with antibiotics and PPIs</span>** for 10-14 days, alongside symptom monitoring and dietary adjustments.</p>
                    </div>
                </div>
            </div>
        </div>
        <!-- 右侧 40% -->
        <div class="section right-section">
            <div class="Weather">
                <div class="weather-widget">
                    <el-icon :size="70"><Sunny /></el-icon>
                    <p>{{ convertedTemperature }}°</p>
                </div>
                <div class="weather-date">
                    <p>{{ formattedTime }}</p>
                </div>
            </div>
            <div class="patient-data-statistics">
                <div class="data-statistics-title">
                    <p style="font-size: 120%; ">Patient Data Statistics</p>
                    <el-button round style="background-color: #f4f5f9; right: 0%;">Download Report</el-button>
                </div>
                <div class="data-statistics-container">
                    <BarChart :data="chartData" :options="chartOptions" />
                </div>

            </div>
            <div class="anomaly">
                <div class="anomaly-container">
                    <LineChart :data="lineChartData" :options="lineChartOptions" />
                    <div class="anomaly-text"><p>Anomaly</p></div>
                </div>
            </div>
            <div class="final-function">
                <div class="left-box">
                    <el-button color="#1eabe7" class="submit-button" @click="dialogFormVisible = true"> 
                        <span style="color: #ffffff;  font-size: 250%;  font-weight: bold;">Submit </span> 
                    </el-button>
                </div>
                <div class="right-box">
                    <div style="margin-left: 10%;">
                        <p>Anomaly Analysis</p>
                        <p style="font-size: small;">{{ anomalyAnalysis }}</p>
                    </div>

                </div>
            </div>
        </div>
        <div class="section padding-section">
        </div>

        <el-dialog v-model="dialogFormVisible" title="Shipping address" width="80%">
            <el-form :model="formData" :rules="rules" ref="form" label-width="auto">
                <el-form-item label="Name" prop="name">
                    <el-input v-model="formData.name" />
                </el-form-item>

                <div class="form-row">
                    <el-form-item label="Gender" prop="gender">
                        <el-radio-group v-model="formData.gender">
                            <el-radio value="Male">Male</el-radio>
                            <el-radio value="Female">Female</el-radio>
                        </el-radio-group>
                    </el-form-item>

                    <el-form-item label="Age" prop="age">
                        <el-input v-model="formData.age" type="number" />
                    </el-form-item>

                    <el-form-item label="NO Patients in ER" prop="noOfPatients">
                        <el-input v-model="formData.noOfPatients" type="number" />
                    </el-form-item>
                </div>

                <div class="form-row">
                    <el-form-item label="Respiratory Rate (RR)" prop="rr">
                        <el-input v-model="formData.rr" type="number" />
                    </el-form-item>

                    <el-form-item label="Saturation" prop="saturation">
                        <el-input v-model="formData.saturation" type="number" />
                    </el-form-item>

                    <el-form-item label="NRS Pain" prop="nrsPain">
                        <el-input v-model="formData.nrsPain" type="number" />
                    </el-form-item>
                </div>

                <el-form-item label="Model of Transport" prop="modelOfTransport">
                    <el-radio-group v-model="formData.modelOfTransport">
                        <el-radio value="119_use">119 Use</el-radio>
                        <el-radio value="car">Car</el-radio>
                        <el-radio value="Private ambulance">Private Ambulance</el-radio>
                    </el-radio-group>
                </el-form-item>

                <div class="form-row">
                    <el-form-item label="Mental Pain" prop="mental_pain">
                        <el-radio-group v-model="formData.mental_pain">
                            <el-radio value="Normal">Normal</el-radio>
                            <el-radio value="pain_response">Pain Response</el-radio>
                        </el-radio-group>
                    </el-form-item>

                    <el-form-item label="Injured">
                        <el-switch v-model="formData.injury" active-value="yes" inactive-value="no"/>
                    </el-form-item>
                </div>

                <el-form-item label="Eligibility Class" prop="eligibility">
                    <el-radio-group v-model="formData.eligibility">
                        <el-radio value="ROYAL COMMISSION">Royal Commission</el-radio>
                        <el-radio value="EXEMPT">Exempt</el-radio>
                        <el-radio value="INSURANCE">Insurance</el-radio>
                        <el-radio value="CASH">Cash</el-radio>
                    </el-radio-group>
                </el-form-item>

                <el-form-item label="Diagnosis" prop="diagnosis">
                    <el-input v-model="formData.diagnosis" type="textarea" />
                </el-form-item>

                <el-form-item label="Chief Complaint" prop="chief_complaint">
                    <el-input v-model="formData.chief_complaint" type="textarea" />
                </el-form-item>

                <div class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">Cancel</el-button>
                    <el-button type="primary" @click="onSubmit">Confirm</el-button>
                </div>
            </el-form>
            <template #footer>
            <div class="dialog-footer">
                <el-button @click="dialogFormVisible = false">Cancel</el-button>
                <el-button type="primary" @click="submitForm">
                Confirm
                </el-button>
            </div>
            </template>
        </el-dialog>
      </div>

      
    </div>
  </template>
  
  <script>
  import { SwitchButton, Sunny } from '@element-plus/icons-vue';
  import { Bar, Line } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, LineElement, PointElement, CategoryScale, LinearScale } from 'chart.js';
  import axios from 'axios';
  import './MainPage.css';
import { reactive, ref } from 'vue'
  import { ElMessageBox } from 'element-plus';

  ChartJS.register(Title, Tooltip, Legend, BarElement, LineElement, PointElement, CategoryScale, LinearScale);
  

  export default {
    name: 'MainPage',
    components: {
        Sunny,
        BarChart: Bar, // Register the Bar component as BarChart
        LineChart: Line

    },
    data() {
        return {
        dialogFormVisible: false,  // 添加这个来控制对话框的显示
        formLabelWidth: '140px',
            
          formData: {
            name: '',
            gender: '',
            age: '',
            noOfPatients: '',
            rr: '',
            saturation: '',
            nrsPain: '',
            modelOfTransport: '',
            injury: '',
            mental_pain: '',
            diagnosis: '',
            chief_complaint: '',
            eligibility: '',

          },
          rules: {
                name: [{ required: true, message: 'Please enter the name', trigger: 'blur' }],
                gender: [{ required: true, message: 'Please select gender', trigger: 'change' }],
                age: [{ required: true, message: 'Please enter age', trigger: 'blur' }],
                noOfPatients: [{ required: true, message: 'Please enter number of patients in ER', trigger: 'blur' }],
                rr: [{ required: true, message: 'Please enter respiratory rate (RR)', trigger: 'blur' }],
                saturation: [{ required: true, message: 'Please enter saturation level', trigger: 'blur' }],
                nrsPain: [{ required: true, message: 'Please enter NRS pain score', trigger: 'blur' }],
                modelOfTransport: [{ required: true, message: 'Please select model of transport', trigger: 'change' }],
                mental_pain: [{ required: true, message: 'Please select mental pain status', trigger: 'change' }],
                eligibility: [{ required: true, message: 'Please select eligibility class', trigger: 'change' }],
                diagnosis: [{ required: true, message: 'Please enter diagnosis', trigger: 'blur' }],
                chief_complaint: [{ required: true, message: 'Please enter chief complaint', trigger: 'blur' }]
            },
          name: "Yongon Li",
          id: "**** **** **** 1234",
          gender: "Female",
          diagnosis: "Patient reports experiencing stomach pain with a burning sensation that worsens after meals, especially when consuming oily or spicy foods. Additional symptoms include nausea, occasional vomiting, and bloating. The patient notes a decreased appetite and unintentional weight loss over the past few weeks, along with sleep disturbances due to pain.",
          medical_History: "Patient has a history of gastritis diagnosed two years ago, with episodes of acid reflux and occasional indigestion. <br><br>No prior history of ulcers, gastrointestinal surgeries, or significant weight fluctuations. <br>Denies any known food allergies or intolerances. <br>No history of chronic illness such as diabetes, hypertension, or cardiovascular disease.",
          age: 45,
          rr: 18,
          saturation: 95,
          chief_complaint: "Persistent stomach pain with nause and loss of appetite",
          mental_pain: "reports feeling of anxiety and distress due to prolonged symptoms",
          arrival_time: "21:13:34",
          no_patients_in_ER: 10,
          ktas: "NON-EMERGENCY",
          waiting_time: 36.17,
          anomaly_detection: "NOT ANOMALY",
          temperature: null,
          city: "Singapore",
          currentDate: new Date(),

          chartData: {
                labels: ["DA", "Fever", "CDC", "BF", "Organic", "Brain", "Psyco"],
                datasets: [
                {
                    label: "Value 1",
                    backgroundColor: "#d2d2d2",
                    hoverBackgroundColor: "#1eabe7",  // 鼠标悬停或选中时的颜色 
                    data: [62, 100, 36, 85, 24, 31, 73]
                },
                {
                    label: "Value 2",
                    backgroundColor: "#ebebeb",
                    hoverBackgroundColor: "#1eabe7",  // 鼠标悬停或选中时的颜色
                    data: [73, 66, 20, 37, 7, 37, 61]
                }
                ]
            },
            chartOptions: {
                responsive: true,
                plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    enabled: true,
                    callbacks: {
                    label: (tooltipItem) => `${tooltipItem.raw} | ${(tooltipItem.raw / 350 * 100).toFixed(2)}%` // Assuming 350 is max value for % calculation
                    }
                }
                },
                scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
                }
            },

            anomaly: { 1: 1, 2: 4, 3: 3, 4: 2, 5: 5, 6: 2, 7: 14, 8: 18, 9: 13, 10: 2, 11: 3, 12: 4 },
            anomalySum: { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 },
            // 初始化 lineChartData 为有效的空结构，避免未初始化的读取错误
            lineChartData: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                datasets: [
                    {
                        label: "Anomaly Rate",
                        data: [], // 初始化为空数组，将在 mounted 中填充
                        borderColor: "#1eabe7",
                        backgroundColor: "rgba(30, 171, 231, 0.2)",
                        fill: true,
                        pointBackgroundColor: "#1eabe7",
                        pointRadius: 3,
                        tension: 0.4 // 曲线的平滑度
                    }
                ]
            },
            lineChartOptions: {
                responsive: true,
                aspectRatio : 4,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        enabled: true,
                        backgroundColor: "#1eabe7",
                        titleColor: "#ffffff",
                        bodyColor: "#ffffff",
                        callbacks: {
                            label: (tooltipItem) => `${tooltipItem.raw}%`
                        }
                    }
                },
                scales: {
                    x: {
                        display: false, // 隐藏 x 轴
                        grid: {
                            display: false // 隐藏 x 轴的网格线
                        }
                    },
                    y: {
                        display: false, // 隐藏 y 轴
                        grid: {
                            display: false // 隐藏 y 轴的网格线
                        }
                    }
                }
            },

          anomalyAnalysis: "The recent surge in flu cases is likely due tocold weather weakening immune defensesand increasing close indoor interactions,facilitating virus spread."
        };
    },
    mounted() {
        this.fetchWeatherData();
    },
    created(){
        this.initLineChartData();
    },
    methods: {

        // 提交表单数据
        async submitForm() {
            console.log("Submitting form data...", this.formData);
            // 格式化数据
            const payload = {
                age: this.formData.age,
                No_Patients_in_ER: this.formData.noOfPatients,
                RR: this.formData.rr,
                Saturation: this.formData.saturation,
                NRS_pain: this.formData.nrsPain,
                mode_of_transport: this.formData.modelOfTransport,
                Chief_complain: this.formData.chief_complaint,
                injury: this.formData.injury,
                Mental_state: this.formData.mental_pain,
                city: "Singapore", // 固定为 "Singapore"
                diagnosis: this.formData.diagnosis,
                eligibility: this.formData.eligibility,
                gender: this.formData.gender,
                time_day: this.getTimeDay(), // 根据时间自动设置
            };

            try {
                // 发送 POST 请求
                const response = await axios.post('http://127.0.0.1:5000/predict_ktas', payload);
                console.log("Response received:", response);
                const responseData = response.data;

                // 同步表单数据到组件的其他变量
                this.name = this.formData.name;
                this.age = this.formData.age;
                this.no_patients_in_ER = this.formData.noOfPatients;
                this.rr = this.formData.rr;
                this.saturation = this.formData.saturation;
                this.chief_complaint = this.formData.chief_complaint;
                this.diagnosis = this.formData.diagnosis;
                this.mental_pain = this.formData.mental_pain;
                this.eligibility = this.formData.eligibility;
                this.gender = this.formData.gender;
                
                // 同步返回的 ktas, waiting_time, anomaly_detection
                this.ktas = responseData.ktas;
                this.waiting_time = responseData.waiting_time;
                this.anomaly_detection = responseData.anomaly_detection;

                const currentTime = new Date();
                this.arrival_time = currentTime.toLocaleTimeString('en-GB', { hour12: false }); // HH:MM:SS format

                this.resetForm(); // 重置表单
                // 关闭对话框
                this.dialogFormVisible = false;
            } catch (error) {
                console.error("Error submitting form:", error);
            }

            // this.$refs.form.validate((valid) => {
            //     if (valid) {
            //         // 处理提交逻辑，比如通过 API 提交数据
            //         console.log("Form Submitted:", this.form);
            //         this.showDialog = false; // 关闭对话框
            //         this.resetForm(); // 重置表单
            //     } else {
            //         console.log('Form validation failed!');
            //     }
            // });
        },
        // 重置表单
        resetForm() {
            this.formData = {
                name: '',
                gender: '',
                age: '',
                noOfPatients: '',
                rr: '',
                saturation: '',
                nrsPain: '',
                modelOfTransport: '',
                injury: '',
                mental_pain: '',
                diagnosis: '',
                chief_complaint: '',
                eligibility: '',
            };
        },

        // 计算 time_day
            getTimeDay() {
            const hours = new Date().getHours();
            if (hours >= 6 && hours < 12) {
                return "Morning";
            } else if (hours >= 12 && hours < 18) {
                return "Afternoon";
            } else if (hours >= 18 && hours < 24) {
                return "Evening";
            } else {
                return "Night";
            }
        },

        async fetchWeatherData() {
        const WEATHER_API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline";
        const WEATHER_API_KEY = "EZLL9NFRQP9M3FGWRJAPSMLKG"; // 替换为你的实际 API 密钥

        try {
            const response = await axios.get(`${WEATHER_API_URL}/${this.city}`, {
            params: {
                key: WEATHER_API_KEY,
                include: "current",
            },
            });

            if (response.status === 200) {
            const weatherData = response.data.currentConditions;
            this.temperature = weatherData.temp; // 获取温度
            } else {
            console.error("Failed to fetch weather data:", response);
            }
        } catch (error) {
            console.error("Error fetching weather data:", error);
        }
        },

        initLineChartData() {
            // 计算 anomalyRate 数据
            const anomalyRate = Object.keys(this.anomaly).map(
                (key) => ((this.anomaly[key] / this.anomalySum[key]) * 100).toFixed(2)
            );

            // 更新 lineChartData 的 data 部分
            this.lineChartData.datasets[0].data = anomalyRate;
        }
    },
    computed: {
    formattedWaitingTime() {
      // 去掉小数部分
      const totalMinutes = Math.floor(this.waiting_time);
      // 计算小时和分钟
      const hours = Math.floor(totalMinutes / 60);
      const minutes = totalMinutes % 60;
      // 格式化为 HH:MM 格式
      return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}`;
    },
    convertedTemperature() {
      // 检查温度是否高于50，如果是，则将其从华氏度转换为摄氏度
      if (this.temperature > 50) {
        return ((this.temperature - 32) * 5 / 9).toFixed(1); // 保留一位小数
      }
      return this.temperature; // 否则直接返回原始温度
    },
    formattedTime() {
      const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
      const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

      const dayName = daysOfWeek[this.currentDate.getDay()]; // 获取星期几
      const date = this.currentDate.getDate(); // 获取日期
      const monthName = months[this.currentDate.getMonth()];

      // 添加日期后缀（st, nd, rd, th）
      const suffix = (date) => {
        if (date % 10 === 1 && date !== 11) return "st";
        if (date % 10 === 2 && date !== 12) return "nd";
        if (date % 10 === 3 && date !== 13) return "rd";
        return "th";
      };

      return `${dayName} ${date}${suffix(date)} ${monthName}.`;
      
    }
  }
  }
  </script>
  
<style></style>