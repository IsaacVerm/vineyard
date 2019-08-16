var vm = new Vue({
  el: '#app',
  data: {
    spray: '',
  },
  mounted() {
      this.spray = axios.get('http://127.0.0.1:5000/spray?predictionPercentageThreshold=20&daysNotSprayedThreshold=200')['spray'];
  },
});
