<template>
  <div class ="medium">
    <div v-if="loading">
      <div class="brand_landing">
        <div id="landing">
          <p>loading...</p>
        </div>
      </div>
      <div class="bg"></div> 
  </div>
  <div v-else>
  <!-- <div class="small"> -->
    <line-chart :chart-data="datacollection" class="chart"></line-chart>
        <div class="dataform">

          <h4> Add/Remove Data</h4>
          <!-- <p> Removes Duplicates</p> -->
            <ul>
              <label> x value </label>
              <input type="text" class="form-control" placeholder="Date" v-model="new_data.x_value">
            </ul>
            <ul>
              <label> y value </label>
              <input type="text" class="form-control " placeholder="Close" v-model="new_data.y_value">
            </ul>
        <button class="btn btn-primary" @click="combined">Update</button>
        </div>
    </div>
  </div>
</template>

<script>
  import LineChart from '@/components/LineChart.vue'
    import axios from 'axios'

  export default {
    components: {
      LineChart
    },
    data () {
      return {
        datacollection: null,
        new_data: { x_value: '2020-09-21', y_value: '65000'},
        loading: false,

      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        let url ='https://jhkintel.herokuapp.com/line';
        this.loading = true
        
				axios
					.get(url)
					.then(
						function (response) {
                            let label = [];
                            let dataClose = [];

							for(let i=0;i<response.data.length;i++)
							{
								let result = response.data[i];

                                label.push(result['Date']);
                                dataClose.push(parseInt(result['Close']));
								
							}
							let datacollection = {
								labels: label,
								datasets: [{
										label: "Line Chart",
										fill: false,
                    data: dataClose,
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',   
                    borderColor: 'rgba(153, 102, 255, 0.2)',   
                    pointBorderColor:'rgba(153, 102, 255, 0.2)',         

                    pointRadius: 1,

									}
								]
							}
							this.datacollection = datacollection;
							console.log(this.datacollection);
						}.bind(this)
					)
					.catch(function (error) {
                        console.log(error)
        }).finally(() => (this.loading = false))
        ;
      },
    addToAPI() {

      let newData = {
        Date: this.new_data.x_value,
        Close: this.new_data.y_value,
      }
      console.log(newData);
      this.loading = true
      axios.post('https://jhkintel.herokuapp.com/line', newData)
        .then((response) => {
          alert("Complete!")
          this.response = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        }).finally(() => (this.loading = false))
        ;
    },

    combined(){
        // this.fillData()
        this.addToAPI()
        this.fillData()
    }
      
    }
  }
</script>

<style>
  .medium {
    max-width: 1200px;
    margin:  150px auto;
  }
  .chart{
    margin-top:-100px;
  }

    .dataform {
    margin: 20px;
  }
</style>