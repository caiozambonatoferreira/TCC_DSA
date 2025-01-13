<template>
  <div id="app">

    <b-steps size="is-small" :has-navigation="false">
      <b-step-item label="Idioma" icon="account-key"></b-step-item>
      <b-step-item label="Interesses" icon="account"></b-step-item>
      <b-step-item label="Conteúdo" icon="account-plus"></b-step-item>
    </b-steps>

    <h2 class="title text-center" v-show="!showArticles">Qual idioma você tem interesse?</h2>

    <div class="columns" v-show="!showArticles">
      <div class="column is-half is-offset-one-quarter">
        <b-field class="justify-center">
          <b-radio-button size="is-large" v-model="language" native-value="english"
            type="is-primary is-light is-outlined">
            <country-flag country='us' size='big' />
            <span class="country-text">Inglês</span>
          </b-radio-button>
          <b-radio-button size="is-large" v-model="language" native-value="spanish"
            type="is-primary is-light is-outlined">
            <country-flag country='es' size='big' />
            <span class="country-text">Espanhol</span>
          </b-radio-button>
          <b-radio-button size="is-large" v-model="language" native-value="italian"
            type="is-primary is-light is-outlined">
            <country-flag country='it' size='big' />
            <span class="country-text">Italiano</span>
          </b-radio-button>
        </b-field>
      </div>
    </div>

    <transition name="fade">
      <div v-if="language" v-show="!showArticles">
        <h2 class="title text-center">Qual assunto você tem interesse?</h2>

        <div class="columns">
          <div class="column is-half is-offset-one-quarter">
            <b-field class="justify-center">
              <b-radio-button size="is-large" v-model="interest" native-value="cinema"
                type="is-primary is-light is-outlined">
                <Icon icon="ic:twotone-local-movies" />
                <span class="country-text">Cinema</span>
              </b-radio-button>
              <b-radio-button size="is-large" v-model="interest" native-value="sports"
                type="is-primary is-light is-outlined">
                <Icon icon="fluent-emoji:soccer-ball" />
                <span class="country-text">Esportes</span>
              </b-radio-button>
              <b-radio-button size="is-large" v-model="interest" native-value="news"
                type="is-primary is-light is-outlined">
                <Icon icon="fluent-color:news-16" />
                <span class="country-text">Notícias</span>
              </b-radio-button>
            </b-field>
          </div>
        </div>
      </div>
    </transition>

    <transition name="fade">
      <articles-component v-if="showArticles" :language="language" :interest="interest" />
    </transition>
  </div>
</template>

<script>
import { Icon } from '@iconify/vue2';
import ArticlesComponent from './components/articles-component.vue';
export default {
  name: 'App',
  

  data() {
    return {
      language: null,
      interest: null,
      showArticles: false
    }
  },

  watch: {
    interest() {
      if(this.language && this.interest) {
        this.showArticles = true
      }
    }
  },

  components: {
    Icon,
    'articles-component': ArticlesComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 100px;
  background: hsl(221 14% 96% / 1);
  width: 100%;
  height: 100vh;
}

.justify-center .field.has-addons {
  justify-content: center;
}

.country-text {
  display: inline-block;
  margin-left: 10px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity .5s;
}

.fade-enter,
.fade-leave-to
  {
  opacity: 0;
}
</style>
