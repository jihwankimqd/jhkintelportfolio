<script>
import { Bubble, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Bubble,
  mixins: [reactiveProp],
 props: [],
  mounted () {
    this.renderChart(this.chartData, this.options)
  },
  data(){
    return{
    options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [ {
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: false
          },
          title:{
              display: true,
              text: 'Bubble Chart'
          },
          responsive: true,
          maintainAspectRatio: false
        }
    }
  }
}
</script>

