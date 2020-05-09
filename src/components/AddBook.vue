<template>
    <form @submit.prevent="addBook">
        <div class="form-group">
            <label for="title">Title</label>
            <input type="text" v-model="title" class="form-control" placeholder="Book name here.." />
        </div>
        <div class="form-group">
            <label for="author">Author</label>
            <input
                type="text"
                v-model="author"
                class="form-control"
                placeholder="Author name here.."
            />
        </div>

        <input type="submit" value="Add Book" class="btn btn-primary" />
    </form>
</template>

<script>
export default {
    name: "AddBook",
    data() {
        return {
            title: "",
            author: "",
        };
    },
    methods: {
        addBook() {
            if (this.title === "" || this.author === "") {
                this.$emit("fill-in-fields", 'Please fill in all fields !', true)
                return
            }

            // Build a book object and send it with the event
            const newBook = {
                title: this.title,
                author: this.author
            };
            this.$emit("add-book", newBook);

            this.title = "";
            this.author = "";
        }
    }
};
</script>

<style scoped>
</style>