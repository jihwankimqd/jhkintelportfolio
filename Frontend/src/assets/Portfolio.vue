<template>
  <div id="app">

    <!-- <div class="container"> -->

      <section id="home">
          <div class="brand_landing">
            <div id="landing">
              <p>Chartjs</p>
            </div>
          </div>
          <div class="bg"></div> 
      </section>

      <section id="">
        <div class="chartjs">

            <div id="chartnav">
            <router-link to="/line">Line</router-link> |
            <router-link to="/bar">Bar</router-link> |
            <router-link to="/doughnut">Doughnut</router-link> |
            <router-link to="/pie">Pie</router-link> |
            <router-link to="/radar">Radar</router-link> |
            <router-link to="/polararea">Polar Area</router-link> |
            <router-link to="/bubble">Bubble</router-link> |
            <router-link to="/scatter">Scatter</router-link>
            </div>
            <router-view />
        </div>
          
      </section>
      

    <!-- </div> -->

  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
  line-height: 1.6;
  overflow: hidden;
      /* width: 100%;
      height: 100%; */

      /* CSS Smooth Scroll */
      overflow-y: scroll; 
      scroll-behavior: smooth;
      scroll-snap-type: y mandatory;

      /* overflow: hidden; */  
}
    * {
      margin: 0;
      padding: 0;
    }

   .brand_landing {


      font-size:30px;
      font-weight: bolder;
      position: relative;
      /* margin-top: -20%; */
    }


    .bg {
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
      opacity: 0;
      transition: 1s;
      pointer-events: none;
      width: 100%;
      height: 100%;
      overflow: hidden;
      color: black;
      background: black;
      padding-bottom:5%;
    }

    .brand_landing:hover~.bg {
      opacity: 1;
      background: #e2a9e5;
      background: -moz-linear-gradient(-45deg, #FB7BA2 5%, #90D5EC 100%);
      background: -webkit-linear-gradient(-45deg,  #FB7BA2 5%, #90D5EC 100%);
      background: linear-gradient(135deg,  #FB7BA2 5%, #90D5EC 100%);
      filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#FB7BA2', endColorstr='#90D5EC',GradientType=1 );
    }

    .lead {
      font-size: 1.5rem;
    }

    section {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      width: 100%;
      height: 100vh;

      /* Scroll Snap */
      scroll-snap-align: center;
    }


    #about p{
      margin-top: -20%;
    }

  .svg-wrapper {
    margin-top: -45px;
    /* position: relative; */
    width: 150px;
    /*make sure to use same height/width as in the html*/
    height: 40px;
    display: inline-block;
    border-radius: 3px;
    margin-left: 5px;
    margin-right: 5px;
  }

    .chartjs{
        margin-top: 95px;
    }

  #shape {
    
    stroke-width: 6px;
    fill: transparent;
    /* opacity: 0; */
    stroke-dasharray: 85 400;
    stroke-dashoffset: -220;
    transition: 1s all ease;
  }

  #landing{
    /* background-color: green; */

    /* margin-top: 200px; */
  }

  #text {
    margin-top: -42px;
  }

  #text a {
    color: black;
    text-decoration: none;
    font-weight: 100;
    font-size: 1.1em;
  }

  .svg-wrapper:hover #shape {
    stroke-dasharray: 50 0;
    stroke-width: 3px;
    stroke-dashoffset: 0;
    stroke: black;
  }


</style>
