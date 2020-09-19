<template>
  <div class='medium'>
  <!-- <div class="small"> -->
    <bubble-chart :chart-data="datacollection" class='chart'></bubble-chart>

      <div class="dataform">
          <h4> Add/Remove Data</h4>

        <!-- <h4> Add Data</h4> -->
        <!-- <p> Removes Duplicates</p> -->

        <ul>
          <label class="pull-left"> x value </label>
          <input type="text" class="form-control" placeholder="Int x" v-model="new_data.x_value">
        </ul>
        <ul>
          <label class="pull-left"> y value </label>
          <input type="text" class="form-control" placeholder="Int y" v-model="new_data.y_value">
        </ul>
        <ul>

          <label class="pull-left"> z value </label>
          <input type="text" class="form-control" placeholder="Int z" v-model="new_data.z_value">
        </ul>

        <button class="btn btn-primary" @click="combined">Update</button>

      </div>
  </div>
</template>

<script>
  import BubbleChart from '@/components/BubbleChart.vue'
    import axios from 'axios'

  export default {
    components: {
      BubbleChart
    },
    data () {
      return {
        datacollection: null,
        new_data: { x_value: '100', y_value: '200', z_value: '300' },

      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
				let url = "http://localhost:5000/" + 'bubble';
				axios
					.get(url)
					.then(
						function (response) {
                            let label = ["Bubble"];
                            let dataClose = [];

							for(let i=0;i<response.data.length;i++)
							{
								let result = response.data[i];
                                // label.push(result['x']);

                                dataClose.push(result)
                                
                                // let temp_data = []
                                // temp_data.push(parseInt(result['x']));
                                // temp_data.push(parseInt(result['y']));
                                // temp_data.push(parseInt(result['r']));
                                // dataClose.push(temp_data)

                                // dataClose.push(parseInt(result['y']));
                                // dataClose.push(parseInt(result['z']));

								
							}
							let datacollection = {
								labels: label,
								datasets: [{
										label: "Bubble Chart",
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

                    
					});
      },
    addToAPI() {

      let newData = {
        x: this.new_data.x_value,
        y: this.new_data.y_value,
        r: this.new_data.z_value
      }
      console.log(newData);
      axios.post('http://localhost:5000/bubble', newData)
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