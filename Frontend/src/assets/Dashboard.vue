<template>
  <div>
  <!-- <div class="small"> -->
    <div class="row">

        <div class="col-md-4">
            <div class="medium">
                <line-chart :chart-data="datacollection" class="chart"></line-chart>
            </div>
        </div>
        <div class="col-md-4">
            <div class="medium">
                <bar-chart :chart-data="datacollection1" class="chart"></bar-chart>
            </div>
        </div>

        <div class="col-md-4">
            <div class="medium">
                <line-chart :chart-data="datacollection2" class="chart"></line-chart>
            </div>
        </div>       
    </div>

        <div class="dataform">

          <h4> Enter Stock Symbol</h4>
          <!-- <p> Removes Duplicates</p> -->
            <ul>
              <label class="pull-left"> Stock ID </label>
              <input type="text" class="form-control" placeholder="Date" v-model="new_data.x_value">
            </ul>

        <button class="btn btn-large btn-block btn-primary full-width" @click="combined">Process Data</button>
        <button class="btn btn-large btn-block btn-primary full-width" @click="fillData">Update Chart</button>

        </div>

  </div>
</template>

<script>
  import LineChart from '@/components/LineChart.vue'
  import BarChart from '@/components/BarChart.vue'
//   import DoughnutChart from '@/components/DoughnutChart.vue'

  import axios from 'axios'
  import 'bootstrap/dist/css/bootstrap.min.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

  export default {
    components: {
      LineChart,
      BarChart,
    //   DoughnutChart
    },
    data () {
      return {
        datacollection: null,
        datacollection1: null,
        datacollection2: null,

        new_data: { x_value: '051910'},

      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
				let url = "http://localhost:5000/" + 'processed_data';
				axios
					.get(url)
					.then(
						function (response) {
                            let label = [];
                            let dataClose = [];
                            
                            let label1 = [];
                            let dataClose1 = [];

                            let label2 = [];
                            let dataClose2 = [];                

                            for(let i=0;i<response.data.length;i++)
							{
								let result = response.data[i];

                                label.push(result['Date']);
                                dataClose.push(parseInt(result['Close']));

                                label1.push(result['Date']);
                                dataClose1.push(parseInt(result['Volume']));			
                                
                                label2.push(result['Date']);
                                dataClose2.push(parseInt(result['DJI_Close']));								
                            }
                            
							let datacollection = {
								labels: label,
								datasets: [{
										label: "Closing Price by Date",
										fill: false,
                                        data: dataClose,
                                        // backgroundColor: 'rgba(153, 102, 255, 0.2)',   
                                        // borderColor: 'rgba(153, 102, 255, 0.2)',   
                                        // pointBorderColor:'rgba(153, 102, 255, 0.2)',   
                                        borderColor: '#ffb6c1',
                                        backgroundColor: '#ffb6c1',
                                        borderWidth: 1,
                                        pointRadius: 1

									}
								]
                            }
							let datacollection1 = {
								labels: label1,
								datasets: [{
										label: "Volume by Date",
										fill: false,
                                        data: dataClose1,
                                        // backgroundColor: 'rgba(153, 102, 255, 0.2)',   
                                        // borderColor: 'rgba(153, 102, 255, 0.2)',   
                                        // pointBorderColor:'rgba(153, 102, 255, 0.2)',   
                                        borderColor: '#2554FF',
                                        backgroundColor: '#2554FF',
                                        borderWidth: 1,
                                        pointRadius: 1

									}
								]
                            }
                            let datacollection2 = {
								labels: label2,
								datasets: [{
										label: "Dow Jones Index Closing Price by Date",
                                        fill: false,

                                        data: dataClose2,
                                        borderColor: '#90EE90',
                                        backgroundColor:'#90EE90',
                                        borderWidth: 1,
                                        pointRadius: 1
									}
								]
                            }                            
                            this.datacollection = datacollection;
                            this.datacollection1 = datacollection1;
							this.datacollection2 = datacollection2;
                            
                            
							console.log(this.datacollection);
						}.bind(this)
					)
					.catch(function (error) {
                        console.log(error)

                    
					});
      },
    addToAPI() {

      let newData = {
        stock_id: this.new_data.x_value,
      }
      console.log(newData);
      axios.post('http://localhost:5000/processed_data', newData)
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
        // this.fillData()
    }
      
    }
  }
</script>

<style>
  /* .chart-box{
    margin-top: 150px;
    max-width: 900px;
  } */

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

</style>