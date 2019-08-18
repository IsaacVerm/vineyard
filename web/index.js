var vm = new Vue({
  el: '#app',
  data: {
    predictionPercentageThreshold: 20,
    daysNotSprayedThreshold: 200,
    spray: '',
  },
  mounted() {
    this.response = axios
      .get(
        'http://127.0.0.1:5000/spray?predictionPercentageThreshold=20&daysNotSprayedThreshold=200',
      )
      .then(response => {
        this.spray = response['data'];
      });
  },
});
