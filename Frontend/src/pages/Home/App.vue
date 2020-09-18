<template>
  <div id="app">
    <Home/>,
    <Navbar/>
  </div>
</template>

<script>
import Navbar from '../../assets/Navbar.vue'
import Home from '../../assets/Home.vue'

export default {
  name: 'App',
  components: {
    Home,
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
