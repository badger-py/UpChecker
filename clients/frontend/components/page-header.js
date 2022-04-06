export const page_header = {
    template: ` <header class="page-header">
                    <h2 class="logo_type">UpChecker</h2>
                    <h2 class="time position-absolute top-50 start-50 translate-middle">{{time}}</h2>
                    <a href="settings.html"><img src="img/settings.png" alt="Settings" class="settings-icon"></a>
                    <!-- TODO: pencil -->
                </header>`,
    data() {
        return {
            time: "00:00"
        }
    },
    mounted() {
        setInterval(() => this.setTime(), 1000)
    },
    methods: {
        setTime() {
            const current = new Date();

            const hours = current.getHours();
            var minutes = current.getMinutes().toString();
            if (minutes.length == 1) {
                var minutes = "0" + minutes
            }
            this.time = hours + ":" + minutes;
        }
    }
}