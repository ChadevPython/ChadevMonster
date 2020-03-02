import "material-design-icons-iconfont/dist/material-design-icons.css"
import Vue from "vue"
import Vuetify from "vuetify"

Vue.use(Vuetify)

export default new Vuetify({
    icons: {
        iconfont: "md"
    },
    theme: {
        dark: true
    }
})
