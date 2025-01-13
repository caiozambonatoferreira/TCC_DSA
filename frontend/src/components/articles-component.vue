<template>
    <div>
        <p v-if="loading">Carregando...</p>

        <div v-else>
            <div class="cards" v-if="articles.length">
                <div class="card" v-for="(article, index) in articles" :key="index">
                    <div class="card-image">
                        <figure class="image is-4by3">
                            <img :src="article.image" :alt="article.title"/>
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
        </div>
    </div>
</template>

<script>
import axios from 'axios';

const apiPath = 'http://127.0.0.1:8000/api/articles/'

export default {
    name: 'articles-component',
    props: ['language', 'interest'],

    data() {
        return {
            loading: false,
            articles: []
        }
    },

    created() {
        this.loading = true
        axios.get(`${apiPath}?language=${this.language}&interest=${this.interest}`)
            .then(response => {
                console.log(response);

                response.data.forEach(res => this.articles.push(res));
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
    }
</style>