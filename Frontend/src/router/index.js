import Vue from 'vue'
import VueRouter from 'vue-router'
import Line from '../views/Line.vue'
import Bar from '../views/Bar.vue'
import Doughnut from '../views/Doughnut.vue'
import Pie from '../views/Pie.vue'
import Radar from '../views/Radar.vue'
import PolarArea from '../views/PolarArea.vue'
import Bubble from '../views/Bubble.vue'
import Scatter from '../views/Scatter.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/line',
    name: 'Line',
    component: Line
  },
  {
    path: '/bar',
    name: 'Bar',
    component: Bar
  }, 
  {
    path: '/doughnut',
    name: 'Doughnut',
    component: Doughnut
  }, 
  {
    path: '/pie',
    name: 'Pie',
    component: Pie
  }, 
  {
    path: '/radar',
    name: 'Radar',
    component: Radar
  }, 
  {
    path: '/polararea',
    name: 'PolarArea',
    component: PolarArea
  }, 
  {
    path: '/bubble',
    name: 'Bubble',
    component: Bubble
  }, 
  {
    path: '/scatter',
    name: 'Scatter',
    component: Scatter
  }, 
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
