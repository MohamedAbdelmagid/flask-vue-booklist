<template>
    <div id="app">
        <div class="content-section">
            <AddBook v-on:add-book="addBook" v-on:fill-in-fields="showAlert" />
            <alert :message="message" :isDanger="isDanger" v-if="showMessage"></alert>
            <Books :books="books" v-on:del-book="deleteBook" v-on:read-status="changeReadStatus" />
        </div>
    </div>
</template>

<script>
import Books from "@/components/Books";
import AddBook from "@/components/AddBook";
import Alert from "@/components/Alert.vue";

import axios from "axios";

export default {
    name: "app",
    components: {
        Books,
        AddBook,
        Alert
    },
    data() {
        return {
            books: [],
            apiEndpoint: "http://localhost:5000/books",
            message: "",
            isDanger: false,
            showMessage: false
        };
    },
    methods: {
        showAlert(message, isDanger = false) {
            this.message = message;
            this.isDanger = isDanger;
            this.showMessage = true;
            setTimeout(() => {
                this.showMessage = false;
            }, 3000);
        },
        deleteBook(id) {
            axios
                .delete(this.apiEndpoint + `/${id}`)
                .then(res => {
                    this.books = this.books.filter(
                        book => book.id !== res.data.id
                    );
                    this.showAlert(
                        `${res.data.title} by ${res.data.author} is deleted !!`,
                        true
                    );
                })
                .catch(err => console.log(err));
        },
        addBook(newBook) {
            axios
                .post(this.apiEndpoint, newBook)
                .then(res => {
                    this.books = [...this.books, res.data];
                    this.showAlert(
                        `${res.data.title} by ${res.data.author} is added !!`
                    );
                })
                .catch(err => console.log(err));
        },
        changeReadStatus(id) {
            axios
                .put(this.apiEndpoint + `/${id}`)
                .then(res => {
                    let bookIndex = this.books.findIndex(
                        book => book.id == res.data.id
                    );
                    let newBooks = [...this.books];
                    newBooks[bookIndex] = {
                        ...newBooks[bookIndex],
                        read: !newBooks[bookIndex].read
                    };
                    this.books = newBooks;
                    if (res.data.read) {
                        this.showAlert(
                            `Did you read ${res.data.title} by ${res.data.author} ? Nice!!`
                        );
                    }
                })
                .catch(err => console.log(err));
        }
    },
    created() {
        axios
            .get(this.apiEndpoint)
            .then(response => (this.books = response.data))
            .catch(err => console.log(err));
    }
};
</script>

<style>
</style>
