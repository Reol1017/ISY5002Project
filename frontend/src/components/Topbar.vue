<template>
    <div class="topbar">
      <!-- 左侧：搜索栏 -->
      <el-input
        class="search-bar"
        placeholder="Search here..."
        prefix-icon="el-icon-search"
        clearable
      />
      <div style="padding-right: 5%">
        <!-- 右侧：图标和用户信息 -->
        <div class="right-section">
          <!-- 图标区域 -->
          <div class="icons">
            <el-badge :value="12" class="icon-badge">
              <el-icon :size="35"><Bell /></el-icon>
            </el-badge>
            <div style="width: 30px;"></div>
            <el-badge :value="5" class="icon-badge">
              <el-icon :size="35"><Message /></el-icon>
            </el-badge>
          </div>
  
          <div style="width: 3%;"></div>
          <!-- 用户信息 -->
          <div class="user-info">
            <div style="width: 150px;">
              <span class="user-name">Hello, Wan</span>
            </div>
            <div style="width: 150px;">
              <span class="user-role">Super Admin</span>
            </div>
          </div>
  
          <!-- 圆形框显示本地图片 -->
          <div class="profile-pic">
            <img src="../assets/dog.jpg" alt="Profile Picture" />
          </div>
  
          <!-- 设置图标 -->
          <div class="icons">
            <el-badge is-dot class="icon-badge">
              <el-icon :size="35"><Setting /></el-icon>
            </el-badge>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ElInput, ElBadge, ElAvatar } from 'element-plus'
  import { Bell, Message, Setting } from '@element-plus/icons-vue'
  
  export default {
    components: {
      ElInput,
      ElBadge,
      ElAvatar,
      Bell,
      Message,
      Setting
    }
  }
  </script>
  
  <style scoped>
  .topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #f9f9f9;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 0;
    left: 12%;
    width: 88%;
    height: 80px;
    z-index: 10;
  }
  
  .search-bar {
    width: 500px;
    border-radius: 500px;
    background-color: #f5f5f5;
    padding: 5px 15px;
    border: none;
    box-shadow: none;
  }
  
  /* 右侧：图标和用户信息 */
  .right-section {
    display: flex;
    align-items: center;
    gap: 30px;
  }
  
  .icons {
    margin-top: 15px;
    display: flex;
    align-items: center;
    gap: 20px;
  }
  
  .icon-badge {
    font-size: 24px;
    color: #5a5a5a;
    cursor: pointer;
  }
  
  .user-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 2px;
  }
  
  .user-name {
    font-weight: bold;
    color: #333;
  }
  
  .user-role {
    color: #888;
    font-size: 12px;
  }

  .profile-pic {
    width: 50px;
    height: 40px;
    border-radius: 50%; /* 确保容器为圆形 */
    overflow: hidden; /* 隐藏溢出部分 */
    border: 2px solid #ddd; /* 可选边框 */
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .profile-pic img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  </style>
  