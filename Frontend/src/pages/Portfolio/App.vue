<template>
  <div id="app">
    <div id="nav">
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

  </div>
</template>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>
