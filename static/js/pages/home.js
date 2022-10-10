const app = Vue.createApp({
    data() {
        return {
            counter: 0,
            response: '',
        }
    },
    methods: {
        initHomeStatus: async function () {
            this.response = await getInfoFromBackend('hello')
            console.log("finish init")
        },
    },
    mounted() {
        this.initHomeStatus()
    },
})

const vm = app.mount('#app');