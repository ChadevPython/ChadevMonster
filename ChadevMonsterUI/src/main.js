import Vue from "vue"
import App from "./App.vue"
import axios from "axios"
import "vuetify/dist/vuetify.min.css"
import vuetify from "./plugins/vuetify"

Vue.config.productionTip = false

const chadevmonster_api = axios.create({
    baseURL: "http://0.0.0.0:5000/api/"
})

Vue.chadevmonster_api = Vue.prototype.$chadevmonster_api = chadevmonster_api

new Vue({
    vuetify,
    render: h => h(App)
}).$mount("#app")
