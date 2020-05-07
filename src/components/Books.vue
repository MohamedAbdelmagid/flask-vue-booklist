<template>
    <div>
        <div v-for="book in books" :key="book.id">
            <Book :book="book" />
        </div>
    </div>
</template>

<script>
import Book from '@/components/Book'

export default {
    name: "Books",
    components: {
        Book,
    },
    props: ["books"]
};
</script>

<style scoped>
</style>