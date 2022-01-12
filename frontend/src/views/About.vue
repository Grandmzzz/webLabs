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
          <h2>About Us</h2>
          <p>This is an example of about page.</p>
        </div>
        <!-- end post -->
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

export default {
  name: 'Home',
  components: {
    Header, Footer
  }
}
</script>