import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import CountryFlag from 'vue-country-flag'

Vue.component('country-flag', CountryFlag)
Vue.use(Buefy)

new Vue({
  render: h => h(App),
}).$mount('#app')
