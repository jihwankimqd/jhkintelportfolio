<template>
  <div class="small">
    <polar-area-chart :chart-data="datacollection" class='chart'></polar-area-chart>

      <div class="dataform">

        <h4> Add Data</h4>
        <p> Removes Duplicates</p>

        <ul>
          <label class="pull-left"> x value </label>
          <input type="text" class="form-control" placeholder="City" v-model="new_data.x_value">
        </ul>
        <ul>
          <label class="pull-left"> y value </label>
          <input type="text" class="form-control" placeholder="Value" v-model="new_data.y_value">
        </ul>

      <button class="btn btn-large btn-block btn-primary full-width" @click="combined">Submit</button>

      <!-- <button class="btn btn-large btn-block btn-primary full-width" @click="RemoveFromAPI">Remove</button> -->
    </div>

  </div>
</template>

<script>
  import PolarAreaChart from '@/components/PolarAreaChart.vue'
    import axios from 'axios'

  export default {
    components: {
      PolarAreaChart
    },
    data () {
      return {
        datacollection: null,
        new_data: { x_value: 'Seoul', y_value: '100'},

      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
				let url = "http://localhost:5000/" + 'polararea';
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
										label: "PolarArea Chart",
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
							// console.log(this.datacollection);
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
      }
      // console.log(newData);
      axios.post('http://localhost:5000/polararea', newData)
        .then((response) => {
          this.response = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // RemoveFromAPI() {
    //   let newData = {
    //     x: this.new_data.x_value,
    //     y: this.new_data.y_value,
    //   }
    //   // console.log(newData);
    //   axios.post('http://localhost:5000/polararea', newData)
    //   // axios.delete('http://localhost:5000/polararea', {data: newData})
    //   // axios.delete('http://localhost:5000/polararea', {data: {'x':'New York', 'y':'150'}})
    //     .then((response) => {
    //       this.response = response.data;
    //       console.log(response);
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    // },

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