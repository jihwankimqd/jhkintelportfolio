<template>
  <div class="small">
  <!-- <div class="chart"> -->
    <line-chart :chart-data="datacollection"></line-chart>

        <h4> Add Data</h4>
        <p> Removes Duplicates</p>

        <ul>
          <label class="pull-left"> x value </label>
          <input type="text" class="form-control" placeholder="Date" v-model="new_data.x_value">
        </ul>
        <ul>
          <label class="pull-left"> y value </label>
          <input type="text" class="form-control" placeholder="Close" v-model="new_data.y_value">
        </ul>

      <button class="btn btn-large btn-block btn-primary full-width" @click="combined">Submit</button>

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

      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
				let url = "http://localhost:5000/" + 'line';
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
                    backgroundColor: '#2554FF',
                    borderColor: '#2554FF',
                    pointBorderColor: '#2554FF',
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

                    
					});
      },
    addToAPI() {

      let newData = {
        Date: this.new_data.x_value,
        Close: this.new_data.y_value,
      }
      console.log(newData);
      axios.post('http://localhost:5000/line', newData)
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
</style>