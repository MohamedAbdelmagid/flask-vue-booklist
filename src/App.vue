<template>
    <div id="app">
        <Books :books="books" />
    </div>
</template>

<script>
import Books from "@/components/Books";
export default {
    name: "app",
    components: {
        Books
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
            ]
        };
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
</style>
