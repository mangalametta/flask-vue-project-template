const app = Vue.createApp({
    data() {
        return {
            counter:0,
        }
    },
    methods: {
        initHomeStatus: function () {
            console.log("finish init")
        },
    },
    mounted() {
        this.initHomeStatus()
    },
})

const vm = app.mount('#app');