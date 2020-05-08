<template>
    <div>
        <table class="table table-striped mt-4">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Author</th>
                    <th>Read?</th>
                    <th></th>   <!-- space for edit button    -->
                    <th></th>   <!-- space for delete button    -->
                </tr>
            </thead>

            <tbody v-for="book in books" :key="book.id">
                <Book :book="book" v-on:del-book="$emit('del-book', book.id)" v-on:read-status="$emit('read-status', book.id)"/>
            </tbody>
        </table>
    </div>
</template>

<script>
import Book from "@/components/Book";

export default {
    name: "Books",
    components: {
        Book
    },
    props: ["books"]
};
</script>

<style scoped>
</style>