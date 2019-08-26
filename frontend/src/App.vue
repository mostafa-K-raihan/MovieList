<template>
  <div id="app">
    <Login/>
    <Navbar/>
  </div>
</template>

<script>
import Login from "./components/Login";
import Navbar  from "./components/Navbar";
export default {
  name: "app",
  components: {
    Navbar,
    Login
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 60px;
}
</style>
