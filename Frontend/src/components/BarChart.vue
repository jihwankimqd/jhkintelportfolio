<script>
import { Bar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Bar,
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
              scaleLabel: {
                display: true,
                labelString: 'Variable'
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [ {
              scaleLabel: {
                display: true,
                labelString: 'Time'
              },
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        }
    }
  }
}
</script>

