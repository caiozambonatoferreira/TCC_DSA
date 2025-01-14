<template>
    <div>
        <p v-if="loading">
            <pulse-loader :loading="loading"></pulse-loader>
        </p>

        <div v-else>
            <b-tabs v-model="activeTab">
                <b-tab-item label="Articles">
                    <div class="cards" v-if="articles.length">
                        <div class="card" v-for="(article, index) in articles" :key="index">
                            <div class="card-image">
                                <figure class="image is-4by3">
                                    <img :src="article.image" :alt="article.title" />
                                </figure>
                            </div>
                            <div class="card-content">
                                <div class="content">
                                    {{ article.title }}
                                </div>
                            </div>
                            <footer class="card-footer">
                                <a :href="article.url" target="_blank" class="card-footer-item">Ver artigo</a>
                            </footer>
                        </div>
                    </div>
                </b-tab-item>

                <b-tab-item label="Flashcards">
                    <div class="cards">
                        <flaschard-component v-for="(flashcard, index) in flashcards"
                            :key="index"
                            :front="flashcard.word"
                            :back="flashcard.translation"
                        ></flaschard-component>
                    </div>
                </b-tab-item>
            </b-tabs>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import FlaschardComponent from './flaschard-component.vue';
const apiPath = 'http://127.0.0.1:8000/api/articles/'

export default {
    name: 'articles-component',
    props: ['language', 'interest'],

    data() {
        return {
            loading: false,
            articles: [],
            flashcards: null,
            activeTab: 0
        }
    },

    components: {
        PulseLoader,
        FlaschardComponent
    },

    created() {
        this.loading = true
        axios.get(`${apiPath}?language=${this.language}&interest=${this.interest}`)
            .then(response => {
                console.log(response);

                response.data.articles.forEach(res => this.articles.push(res));
                this.flashcards = response.data.flashcards
             })
             .catch(err => console.warn(err))
             .finally(()=> this.loading = false)
    }
}
</script>


<style>
    .cards {
        max-width: 1280px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-gap: 3rem;
        padding: 10px;
    }

    .card .image img{
        object-fit: cover;
    }
</style>