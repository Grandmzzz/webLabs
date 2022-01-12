<template>
  <div class="body">
    <!-- BEGIN wrapper -->
    <div id="wrapper">
      <!-- BEGIN Header -->
      <Header/>
      <!-- END Header -->
      <!-- BEGIN content -->
      <div id="content">
        <!-- begin recent posts -->
        <div class="recent">
          <!-- begin post -->
          <div class="single">
            <h2>Registration</h2>
            <p>Please enter your registration data</p>
          </div>
          <!-- end post -->
          <div id="enter-data">
            <div id="respond">
              <form @submit.pe.prevent="handleRegistration" id="commentform">
                <p>
                  <input type="email" name="email" id="email" value="" size="22" tabindex="1"
                         v-model="userData.username"/>
                  <label for="email"><small>E-Mail (required)</small></label>
                </p>
                <p>
                  <input type="password" name="password" id="password" value="" size="22" tabindex="2"
                         v-model="userData.password"/>
                  <label for="password"><small>Password (required)</small></label>
                </p>
                <p>
                  <button name="submit" type="submit" id="submit">Submit</button>
                </p>
              </form>
            </div>
          </div>
        </div>
        <!-- end recent posts -->
      </div>
      <!-- END content -->
    </div>
    <!-- END wrapper -->
    <!-- BEGIN footer -->
    <Footer/>
    <!-- END footer -->
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import {register} from "../api"


export default {
  name: 'Home',
  components: {
    Header, Footer
  },

  data() {
    return {
      userData: {
        username: '',
        password: ''
      }
    }
  },

  methods: {
    handleRegistration() {
      register(this.userData)
          .then(() => this.$router.push('/'))
    }
  }
}
</script>