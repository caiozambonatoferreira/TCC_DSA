<template>
    <div>
        <p v-if="loading">Carregando...</p>

        <div v-else>
            {{ articles }}
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