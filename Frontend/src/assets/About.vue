<template>
  <div id="app">

    <!-- <div class="container"> -->

        <section id="intro">
                <div id="text">
                <!-- <a href="about.html">about</a> -->
                <h3>Ji Hwan KIM</h3>
                <br>
                <p>I am pursuing a BSc in Physics at HKUST.<br/>
                I develop, analyze, and study all types of data. <br>
                I have a particular interest in data with value. <br>
                </p>
                </div> 
            
        </section>

        <section id="programming">
                <div id="text">
                    <h3>Programmer</h3>
                    <br>
                    <p>I believe programming has a lot of potential<br>
                    Being motivated in learning, I have taught myself: 
                    <br/>
                    <br/>
                        Python Numpy Matplotlib Pandas Sklearn, C++ (Primary) <br>
                        JavaScript HTML CSS, Vue.js, Flask, Git (Secondary)
                    <br>
                    </p>
                </div> 
        
        </section>

        <section id="Interpersonal">

                <div id="text">
                    <h3>Communicator and Leader</h3>
                    <br>
                    <p>
                        I have spent 21 months with US Forces Korea interpreting and translating <br>
                        military language and documents for high ranking US/ROK officers under <br>
                        intense training environments. I am trained to perform under pressure.<br>
                        Furthermore, as a former band leader, I have organised and performed <br>
                        concerts in front of hundreds while leading and managing the members.   
                    </p>
                </div> 

        </section>

        <section id="background">

                <div id="text">
                    <h3>International</h3>
                    <br>
                    <p>
                        I have lived in 6 different countries- Korea, Malaysia, China,<br>
                        Indonesia, Hong Kong, Philippines. I speak Korean (Native), <br> 
                        English (Fluent), Mandarin (Basic), Indonesian (Basic). I really <br>
                        get along with everyone from any background and culture.
                        
                    </p>
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
    /* width: 100%; */
    /* height: 100%; */
    /* CSS Smooth Scroll */
    overflow-y: scroll; 
    scroll-behavior: smooth;
    scroll-snap-type: y mandatory;
}
    * {
      margin: 0;
      padding: 0;
    }


    .container {

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


  #text {
    /* margin-top: -250px; */
    text-align: center;
  }

  

</style>
