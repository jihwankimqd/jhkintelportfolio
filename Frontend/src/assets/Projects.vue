<template>
  <div id="app">
      <div class="row">

        <div class="col-md-4">
          <div class="img-hover-zoom">
            <a href="https://github.com/jihwankimqd/Stock_Analysis">
              <img src="https://raw.githubusercontent.com/jihwankimqd/Stock_Analysis/master/stock_analysis.gif">
            </a>
          </div>
          <p>Stock Scraping,Cleaning,EDA,Model Training</p>
          <p>-Python, Numpy, Pandas, BeautifulSoup, sklearn-</p>
        </div>

        <div class="col-md-4">
          <div class="img-hover-zoom">
            <a href="https://github.com/jihwankimqd/Bitcoin_Heist_Classification">
              <img src="https://raw.githubusercontent.com/jihwankimqd/Bitcoin_Heist_Classification/master/bitcoin_classification.gif">
            </a>
          </div>
          <p>Bitcoin Heist Classification</p>
          <p>-Python, Numpy, Pandas, sklearn-</p>
        </div>

        <div class="col-md-4">
          <div class="img-hover-zoom">
            <a href="https://github.com/jihwankimqd/MCMC_Cipher">
              <img src="https://raw.githubusercontent.com/jihwankimqd/MCMC_Cipher/master/mcmccipher.gif">
            </a>
          </div>
          <p>Cipher Decryption and Text Mining</p>
          <p>-Python Numpy-</p>
        </div>

        <div class="col-md-4">
          <div class="img-hover-zoom">
            <a href="https://kospi-stocks.herokuapp.com/">
              <img src="https://raw.githubusercontent.com/jihwankimqd/stocks_scraped/master/kospi.gif">
            </a>
          </div>
          <p>Live KOSPI Stock Scraper/Cleaner/Predictor</p>
          <p>-Python Pandas Dash Sklearn-</p>
        </div>

        <div class="col-md-4">
          <div class="img-hover-zoom">
             <a href="https://github.com/jihwankimqd/sentiment_analysis/tree/master">
              <img src="https://raw.githubusercontent.com/jihwankimqd/sentiment_analysis/master/sentiment_analysis.gif">
            </a>
          </div>
          <p>Sentiment Analysis for Stock Analysis</p>
          <p>-Python Pandas Dash Sklearn Numpy-</p>
        </div>

        <div class="col-md-4">
          <div class="img-hover-zoom">
            <a href="https://jihwankimqd.github.io/vue_sorting_vis_/">
              <img src="https://raw.githubusercontent.com/jihwankimqd/vue_sorting_vis_/master/vuesorting.gif">
            </a>
          </div>
          <p>Vue Sorting Algorithms Visualizer</p>
          <p>-Javascript Vue.js, HTML, CSS-</p>
        </div>

        <div class="col-md-4">
          <div class="img-hover-zoom">
            <a href="https://jihwankimqd.github.io/vue_portfolio_/">
              <img src="https://raw.githubusercontent.com/jihwankimqd/vue_portfolio_/master/vuespa.gif">
            </a>
          </div>
          <p>Vue SPA</p>
          <p>-Javascript Vue.js, HTML, CSS-</p>
        </div>

      </div>
  </div>

  <!-- </div> -->
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

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
  /* height: 100vh; */
  /* line-height: 1.6; */
  overflow: hidden;
  margin-top:50px;
}

body {
  margin:30px;

  }

    * {
      margin: 0;
      padding: 0;
    }


    .container {
      width: 100%;
      height: 100%;
      /* CSS Smooth Scroll */
      overflow-y: scroll; 
      scroll-behavior: smooth;
      scroll-snap-type: y mandatory;
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


  p {
    /* margin-top: -250px; */
    text-align: center;
  }

  #text a{
    color: black;
    text-decoration: none;
    font-weight: 100;
    font-size: 1.1em;
  }

  .contact-list li {
    list-style-type: none;
    
}

  img{
    width: auto;
    height: 240px;

  }

  .img-hover-zoom {
    overflow: hidden; /* [1.2] Hide the overflowing of child elements */

    /* object-fit:cover; */
    /* object-position:50% 50%; */
  }

  /* [2] Transition property for smooth transformation of images */
  .img-hover-zoom img {
    transition: transform .5s ease;

  }

  /* [3] Finally, transforming the image when container gets hovered */
  .img-hover-zoom:hover img {
    transform: scale(1.1);
  }

  .col-md-4 {
    margin-bottom: 30px;
    /* padding:25px; */
  }

  .col-md-4 p {
    margin-top: 3px;
    margin-bottom: -3px;
  }

</style>
