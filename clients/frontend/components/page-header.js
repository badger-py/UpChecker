export const page_header = {
    template: ` <header class="page-header">
                    <h2 class="logo_type">UpChecker</h2>
                    <h2 class="time position-absolute top-50 start-50 translate-middle">{{getCurrentTime()}}</h2>
                    <a href="settings.html"><img src="img/settings.png" alt="Settings" class="settings-icon"></a>
                    <!-- TODO: pencil -->
                </header>`,
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
}