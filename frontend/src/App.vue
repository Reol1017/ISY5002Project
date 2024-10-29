<template>
  <div id="app">
    <Sidebar />
    <Topbar />
    <div class="main-content" id="main-content">
        <MainPage />
    </div>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'
import Topbar from './components/Topbar.vue'
import MainPage from './pages/MainPage.vue'

export default {
  components: {
    Sidebar,
    Topbar,
    MainPage
  }
}
</script>

<style>
#app {
  display: flex;
}

.main-content {
  position: absolute;
  top: 80px; /* 下移 60px 以避开 Topbar */
  left: 12%; /* 右移 12% 以避开 Sidebar */
  width: 88%; /* 占据右侧 88% 的宽度 */
  height: calc(100% - 80px); /* 占据剩余的高度 */
  padding: 0px; /* 可选的内边距 */
  box-sizing: border-box;
  overflow: auto; /* 如果内容溢出，可以滚动 */
}
</style>
