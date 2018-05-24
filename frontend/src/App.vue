<template>
  <div id="app">
    <h1> VALUE </h1>
    <p>{{ value }}</p>
  </div>
</template>

<script>
import webSocket from "./websocket/websocket.js";
export default {
  name: "App",
  mounted() {
    webSocket.onmessage = event => {
      this.value = event.data;
    };
  },
  data() {
    return {
      value: 0
    };
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
