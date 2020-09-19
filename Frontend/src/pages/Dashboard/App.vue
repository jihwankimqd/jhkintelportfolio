<template>
  <div id="app">
    <Dashboard/>,
    <Navbar/>
  </div>
</template>

<script>
import Navbar from '../../assets/Navbar.vue'
import Dashboard from '../../assets/Dashboard.vue'

export default {
  name: 'App',
  components: {
    Dashboard,
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
  }
</style>
