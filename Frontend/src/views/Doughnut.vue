<template>
  <!-- <div class="small"> -->
  <div class='size'>
  <div v-if="loading">
      <div class="brand_landing">
        <div id="landing">
          <p>loading...</p>
        </div>
      </div>
      <div class="bg"></div> 
  </div>
  <div v-else>
    <doughnut-chart :chart-data="datacollection" class='chart'></doughnut-chart>

      <div class="dataform">
          <h4> Add/Remove Data</h4>

        <!-- <h4> Add Data</h4> -->
        <!-- <p> Removes Duplicates</p> -->

        <ul>
          <label class="pull-left"> x value </label>
          <input type="text" class="form-control" placeholder="City" v-model="new_data.x_value">
        </ul>
        <ul>
          <label class="pull-left"> y value </label>
          <input type="text" class="form-control" placeholder="Value" v-model="new_data.y_value">
        </ul>

        <button class="btn btn-primary" @click="combined">Update</button>


      </div>
    </div>
  </div>
</template>

<script>
  import DoughnutChart from '@/components/DoughnutChart.vue'
    import axios from 'axios'

  export default {
    components: {
      DoughnutChart
    },
    data () {
      return {
        datacollection: null,
        new_data: { x_value: 'Seoul', y_value: '100'},
        loading: false,
      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        let url = 'https://jhkintel.herokuapp.com/doughnut';
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

                                label.push(result['x']);
                                dataClose.push(parseInt(result['y']));

								
							}
							let datacollection = {
								labels: label,
								datasets: [{
										label: "Doughnut Chart",
                    borderWidth: 1,
                    borderColor: [
                    // 'rgba(255,99,132,1)',
                    // 'rgba(54, 162, 235, 1)',
                    // 'rgba(255, 206, 86, 1)',
                    // 'rgba(75, 192, 192, 1)'                
                    ],
                    backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',         
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',         
                    ],
										fill: false,
										data: dataClose
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
        x: this.new_data.x_value,
        y: this.new_data.y_value,
      }
      console.log(newData);
      this.loading = true
      axios.post('https://jhkintel.herokuapp.com/doughnut', newData)
        .then((response) => {
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
  .size{
    max-width: 500px;
    margin:  150px auto;

  }
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
  .chart{
    margin-top:-100px;
  }

  .dataform {
    margin: 20px;
  }
</style>