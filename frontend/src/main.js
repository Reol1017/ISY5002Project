import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
// import router from './router/index.js'  // 导入路由

const app = createApp(App)
app.use(ElementPlus)
// app.use(router)
app.mount('#app')
