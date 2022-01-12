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
            <h2>{{ title }}</h2>
            {{ text }}
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
import {getArticle} from '../api'

export default {
  name: 'Home',
  components: {
    Header, Footer
  },

  data() {
    return {
      title: '',
      text: ''
    }
  },

  created() {
    this.getData()
  },

  methods: {
    getData() {
      getArticle(this.$route.params.id)
          .then(({title, text}) => {
            this.title = title
            this.text = text
          })
    }
  }
}
</script>