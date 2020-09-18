<template>
  <!-- <div id="app"> -->
    
    <Slide right id='my-component'>
      <a id="home" href="index.html">
        <span>HOME</span>
      </a>
<!-- 
      <a id="about" href="about.html">
        <span>ABOUT</span>
      </a>    

      <a id="projects" href="projects.html">
        <span>PROJECTS</span>
      </a>      
      
      <a id="contact" href="contact.html">
        <span>CONTACT</span>
      </a>      -->
    </Slide>

  <!-- </div> -->
</template>

<script>
import { Slide } from 'vue-burger-menu'

export default {
  name: 'App',
  components: {
    Slide
  }
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
}
    #my-component .bm-burger-button {
      position: fixed;
      width: 15px;
      height: 13px;
      left: 25px;
      top: 35px;
      cursor: pointer;
    }

    #my-component .bm-burger-bars {
      background-color: #373a47;
    }

    #my-component .line-style {
      position: absolute;
      height: 15%;
      left: 0;
      right: 0;
    }
    #my-component .cross-style {
      position: absolute;
      top: 12px;
      right: 2px;
      cursor: pointer;
    }
    #my-component .bm-cross {
      background: #bdc3c7;
    }
    #my-component .bm-cross-button {
      height: 24px;
      width: 24px;
    }
    #my-component .bm-menu {


      position: fixed; /* Stay in place */
      z-index: 1000; /* Stay on top */

      background-color: rgb(63, 63, 65); /* Black*/


      transition: 0.5s; /*0.5 second transition effect to slide in the sidenav*/
    }
 
    #my-component .bm-overlay {
      background: rgba(0, 0, 0, 0.3);
      
    }
    #my-component .bm-item-list {
      color: #b8b7ad;
      direction: rtl;
      font-size: 20px;
      padding-top: 2em;
    }
    #my-component .bm-item-list > * {
      display: flex;
      text-decoration: none;
      padding: 0.7em;
    }
    #my-component .bm-item-list > * > span {
        
      font-weight: 100;
      font-size: 15px;
      color: white;
    }
  
</style>
