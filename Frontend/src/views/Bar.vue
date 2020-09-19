<template>
  <div class ="medium">
  <!-- <div class="small"> -->
    <bar-chart :chart-data="datacollection" class="chart"></bar-chart>
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
</template>

<script>
  import BarChart from '@/components/BarChart.vue'
  // import 'bootstrap/dist/css/bootstrap.min.css'
  // import 'bootstrap-vue/dist/bootstrap-vue.css'
    import axios from 'axios'

  export default {
    components: {
      BarChart
    },
    data () {
      return {
        datacollection: null,
        new_data: { x_value: '2020-09-21', y_value: '65000'},

      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
				let url = "http://localhost:5000/" + 'bar';
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
										label: "Bar Chart",
										fill: false,
                    data: dataClose,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(255,99,132,1)',
                    pointBorderColor: '#2554FF',
									}
								]
							}
							this.datacollection = datacollection;
							console.log(this.datacollection);
						}.bind(this)
					)
					.catch(function (error) {
                        console.log(error)

                    
					});
      },
    addToAPI() {

      let newData = {
        Date: this.new_data.x_value,
        Close: this.new_data.y_value,
      }
      console.log(newData);
      axios.post('http://localhost:5000/bar', newData)
        .then((response) => {
          this.response = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
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
  .chart{
    margin-top:-100px;
  }

  /* .small {
    max-width: 600px;
    margin:  150px auto;
  } */

    .dataform {
      margin: 20px;
    }
  .form-control {
      margin-left:10px;
      min-width: 0;
      width: auto;
      display: inline;
  }
</style>