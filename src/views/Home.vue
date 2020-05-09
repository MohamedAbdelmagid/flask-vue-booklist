<template>
    <div id="app">
        <div class="content-section">
            <AddBook v-on:add-book="addBook" />
            <Books :books="books" v-on:del-book="deleteBook" v-on:read-status="changeReadStatus" />
        </div>
    </div>
</template>

<script>
import Books from "@/components/Books";
import AddBook from "@/components/AddBook";
import axios from "axios";

export default {
    name: "app",
    components: {
        Books,
        AddBook
    },
    data() {
        return {
            books: [],
			apiEndpoint: "http://localhost:5000/books"
        };
    },
    methods: {
        deleteBook(id) {
            this.books = this.books.filter(book => book.id !== id);
        },
        addBook(newBook) {
            this.books = [...this.books, newBook];
        },
        changeReadStatus(id) {
            let bookIndex = this.books.findIndex(book => book.id == id);
            let newBooks = [...this.books];
            newBooks[bookIndex] = {
                ...newBooks[bookIndex],
                read: !newBooks[bookIndex].read
            };
            this.books = newBooks;
        }
	},
	created() {
		axios.get(this.apiEndpoint)
			.then(response => this.books = response.data)
			.catch(err => console.log(err))
	}
};
</script>

<style>
</style>
