<template>
    <el-menu
      class="el-menu-vertical-demo"
      :default-active="activeMenu"
      background-color="#e9e9e9"
      text-color="#bfbfbf"
      active-text-color="#292929"
      router
    >
      <!-- 用户头像和主页标题 -->
      <div class="logo-section">
        <h2>EMERGENCY </h2>
      </div>
  
    <!-- 主菜单项 -->
    <el-menu-item index="1">
      <div class="menu-content">
        <span>Main Page</span>
      </div>
    </el-menu-item>

    <el-menu-item index="2">
      <div class="menu-content">
        <span>Archives</span>
      </div>
    </el-menu-item>

    <el-menu-item index="3">
      <div class="menu-content">
        <span>Modification</span>
      </div>
    </el-menu-item>

    <el-menu-item index="4">
      <div class="menu-content">
        <span>Data</span>
      </div>
    </el-menu-item>

    <el-menu-item index="5">
      <div class="menu-content">
        <span>Departments</span>
      </div>
    </el-menu-item>
    
    <el-menu-item index="6">
      <div class="menu-content">
        <span>Settings</span>
      </div>
    </el-menu-item>
  </el-menu>
</template>
  
  <script>
  import { ElMenu, ElMenuItem } from 'element-plus'
  
  export default {
    name: 'Sidebar',
    components: {
      ElMenu,
      ElMenuItem
    },
    data() {
      return {
        activeMenu: '1', // 设置初始激活的菜单项
      }
    }
  }
  </script>
  
  <style scoped>
  .el-menu-vertical-demo {
    position: fixed;
    top: 0;
    left: 0;
    width: 12%;
    height: 100vh;
    background-color: #f0f0f0;
    color: #292929;
    display: flex;
    flex-direction: column;
    justify-content: start;
  }
  
  .logo-section {
    display: flex;
    align-items: center;
    justify-content: center; /* 水平居中 */
    width: 100%;
    padding: 20px;
    color: #292929;
    text-align: center; /* 让文本在 div 中心对齐 */
  } 

  .logo-section h2 {
    margin-right: 25%;
    font-size: 28px; /* 可以根据需要调整字体大小 */
    font-weight: bold;
  }

/* 设置每个菜单项的高度和样式 */
.el-menu-item {
  display: flex;
  align-items: center;
  height: 8vh; /* 占总高度的8% */
}

.menu-content {
  margin-left: 25%; /* 左边空出 25% 的距离 */
  font-size: 16px;
}
  </style>
  