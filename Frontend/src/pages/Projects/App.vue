<template>
  <div id="app">

    <Projects/>
    <Navbar/>

  </div>
</template>

<script>

import Navbar from '../../assets/Navbar.vue'
import Projects from '../../assets/Projects.vue'


export default {
  name: 'App',
  components: {
    Projects,
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
    /* overflow: hidden; */
  }

  #chartnav{
    margin-top:35px;
  }
</style>
