var vm = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!',
  },
  mounted() {
      axios.get('http://127.0.0.1:5000/spray?predictionPercentageThreshold=20&daysNotSprayedThreshold=200');
  },
});
