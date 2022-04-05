var app = Vue.createApp({
    data() {
        return {
            message: "Hello World!"
        }
    },
    methods: {
        getCurrentTime() {
            const current = new Date();

            const hours = current.getHours();
            var minutes = current.getMinutes().toString();
            if (minutes.length == 1) {
                var minutes = "0" + minutes
            }
            const time = hours + ":" + minutes;

            return time;
        }
    }
}).mount('#app')

// app.component(
//     'Footer'
// )