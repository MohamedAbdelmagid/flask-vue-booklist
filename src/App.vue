<template>
    <div id="app">
        <div class="content-section">
            <Header />
			<AddBook />
            <Books :books="books" v-on:del-book="deleteBook" />
        </div>
    </div>
</template>

<script>
import Books from "@/components/Books";
import Header from "@/components/layout/Header";

export default {
    name: "app",
    components: {
        Books,
        Header,
    },
    data() {
        return {
            books: [
                {
                    id: 1,
                    title: "The Art Of Seduction",
                    author: "Robert Green",
                    read: false
                },
                {
                    id: 2,
                    title: "David Copperfield",
                    author: "Charles Dickens",
                    read: true
                },
                {
                    id: 3,
                    title: "One Night at Call Centre",
                    author: "Chetan Bhagat",
                    read: false
                },
                {
                    id: 4,
                    title: "Half Girlfriend",
                    author: "Chetan Bhagat",
                    read: false
                }
            ],
        };
    },
    methods: {
        deleteBook(id) {
            this.books = this.books.filter(book => book.id !== id);
        }
    }
};
</script>

<style>
#app {
    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
}
.content-section {
    -webkit-border-radius: 10px 10px 10px 10px;
    border-radius: 10px 10px 10px 10px;
    border: 1px solid #dddddd;
    background: #ffffff;
    padding: 30px;
    width: 90%;
    max-width: 550px;
    position: relative;
}
</style>
