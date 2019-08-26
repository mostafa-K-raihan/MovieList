<template>
  <div>
    <p v-if="loginStatus.length">{{this.loginStatus}}</p>
    <div class="login" v-if="!hideLogin">
    <h2>Login</h2>
    <form @submit.prevent="submitForm">

      <label>User Name</label>
      <input placeholder="Please Enter user name" v-model="username" type="text">
      <label>Password</label>
      <input placeholder="Please Enter password" v-model="password" type="password">
      <input type="submit">
    </form>
  </div>
  </div>

</template>

<script>
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
const API_URL = 'http://localhost:8000/app/';
export default {

  name: "Login",
  props: {},
  data() {
    return {
      username: '',
      password: '',
      hideLogin : false,
      loginStatus: ''
    }
  },
  methods: {
    submitForm () {

      axios.post(API_URL +'login', {
        username : this.username,
        password : this.password,
      })
              .then(res=> {
                  if(res.data.Status === 'OK') {
                    this.hideLogin = true;
                    this.loginStatus = "Successfully Logged in";
                    this.$emit("auth")
                  }else if(res.data.Status === 'ERROR') {
                    this.loginStatus = "Authentication Failed";
                  }
              }).catch(err=> {

      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .login{
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr;
  }

  form {
    display: grid;
    grid-template-rows: repeat(3, 1fr);
    grid-template-columns: 1fr;
    max-width: 400px;
    grid-gap: 1.2rem;

  }
</style>
