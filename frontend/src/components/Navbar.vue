<template>

    <div>
        <label>Search For Movie
            <input type="text" v-model="search" @blur="findMovie">
        </label>

    <ul>
        <li v-for="(movie,index) in result" :key="index" @click="showDetails(index)">
            {{movie}}
        </li>
    </ul>
        <modal name="show-details">
            <div class="modal__details">
                <h1>Name : {{clickedMovie.Title}}</h1>
                <p>Actors: {{clickedMovie.Actors}}</p>
                <p>Director: {{clickedMovie.Director}}</p>
                <p>Director: {{clickedMovie.Genre}}</p>
<!--                <p>Director: {{clickedMovie.Released}}</p>-->
<!--                <p>Director: {{clickedMovie.Runtime}}</p>-->
<!--                <p>Director: {{clickedMovie.BoxOffice}}</p>-->

                <h5>Ratings</h5>
                <ul>
                    <li v-for="r in clickedMovie.Ratings">
                        {{r.Source}} => {{r.Value}}
                    </li>
                </ul>
                <img :src="clickedMovie.Poster">
            </div>

        </modal>
    </div>
</template>

<script>
    import axios  from 'axios';
    import VModal from 'vue-js-modal';

    export default {
        name: "Navbar",
        data() {
            return {
                search: '',
                result: [],
                json_object : [],
                clickedMovie: {},
            }
        },
        methods: {
            findMovie() {
                axios.get('http://www.omdbapi.com/?apikey=b4cf19e0&t='+this.search)
                    .then(res=>{
                        this.result.push(res.data.Title);
                        this.json_object.push(res.data);
                    });

            },
            showDetails (index) {
                this.clickedMovie = this.json_object[index];
                this.$modal.show('show-details', {
                    button: [
                        {
                            title: 'Close'
                         }
                    ]
                });

            },

        },
        watch: {
            search() {

            }
        }
    }
</script>

<style scoped>
    .modal__details {
        display: grid;
        grid-template-columns: 1fr;
        grid-gap: .5rem;
        height: 50vh;
    }
</style>