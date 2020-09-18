<template>
  <div id="app">
    <About/>
    <Navbar/>

  </div>
</template>

<script>
import About from '../../assets/About.vue'
import Navbar from '../../assets/Navbar.vue'



export default {
  name: 'App',
  components: {
      About,
      Navbar
  }
}
</script>

<style>

</style>
