<template>
  <div id="app">
    
    <div id="chartnav">
      <router-link to="/line">Line</router-link> |
      <router-link to="/bar">Bar</router-link> |
      <router-link to="/doughnut">Doughnut</router-link> |
      <router-link to="/pie">Pie</router-link> |
      <router-link to="/radar">Radar</router-link> |
      <router-link to="/polararea">Polar Area</router-link> |
      <router-link to="/bubble">Bubble</router-link> |
      <router-link to="/scatter">Scatter</router-link> |
    </div>
    <router-view />
    <Navbar/>

  </div>
</template>

<script>
import Navbar from '../../assets/Navbar.vue'

export default {
  name: 'App',
  components: {

    Navbar

  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    overflow: hidden;
  }

  #chartnav{
    margin-top:35px;
  }
</style>
