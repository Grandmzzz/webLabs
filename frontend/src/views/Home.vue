<template>
  <div class="body">
    <!-- BEGIN wrapper -->
    <div id="wrapper">
      <!-- BEGIN Header -->
      <Header/>
      <!-- END Header -->
      <!-- BEGIN content -->
      <div id="content">
        <!-- begin featured -->
        <div id="featured">
          <div class="post">
            <h2>
              <router-link :to="getPageUrl(this.mainArticle.title)">{{ this.mainArticle.title }}</router-link>
            </h2>
            <p class="details">{{ this.mainArticle.date_create }}</p>
            <div class="thumb"><a href="#"><img src="images/_featured.jpg" alt=""/></a></div>
            <p>{{ this.mainArticle.description }}</p>
            <p class="readmore">[
              <router-link :to="getPageUrl(this.mainArticle.id)">read more</router-link>
              ]
            </p>
            <p class="tags">TAGS:
              <a v-for="tag in this.mainArticle.tags" href="#">{{ tag }}</a>,
            </p>
            <div class="break"></div>
          </div>
        </div>
        <!-- end featured -->
        <!-- begin recent posts -->
        <div class="recent">
          <!-- begin post -->
          <div
              v-for="(article, index) in this.feed"
              :class="{
                'e': index % 2,
                'o': !(index % 2),
                'post': true
              }"
          >
            <a href="#"><img src="images/_thumb.jpg" alt=""/></a>
            <h2><router-link :to="getPageUrl(article.id)">{{ article.title }}</router-link></h2>
            <p>{{article.description}}</p>
            <p class="readmore">[ <router-link :to="getPageUrl(article.id)">read more</router-link> ]</p>
            <div class="break"></div>
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
import {getHome, getTags} from "../api";

export default {
  name: 'Home',
  components: {
    Header, Footer
  },

  data() {
    return {
      mainArticle: {
        id: 0,
        title: '',
        description: '',
        date_create: '',
        tags: []
      },
      feed: []
    }
  },

  created() {
    this.getFeed()
  },

  methods: {
    getFeed() {
      const requests = [
        getHome(),
        getTags()
      ]

      Promise
          .all(requests)
          .then(([feed, tags]) => {

            const tagsDict = tags.reduce(
                (prev, {id, description}) => {
                  prev[id] = description
                  return prev
                },
                tags,
                {}
            )

            const feedWithTags = feed.map(article => {
              article.tags = article.tags.map(tag => tagsDict[tag])
              return article
            })

            this.mainArticle = feedWithTags.pop()
            this.feed = feedWithTags
          })
    },

    getPageUrl(id) {
      return `/page/${id}`
    }
  }
}
</script>