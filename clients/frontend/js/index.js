import { page_header } from '../components/page-header.js';


var app = Vue.createApp({
    data() {
        return {
            message: "Hello World!"
        }
    }
})
app.component(
    'page-header',
    page_header
)
app.mount('#app')