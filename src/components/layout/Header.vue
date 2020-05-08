<template>
    <header class="header">
        <h1 class="display-4 text-center">
            <i class="fas fa-book-open text-primary"></i> My
            <span class="text-primary">Book</span>List
        </h1>
        <div id="nav">
            <router-link to="/" class="text-primary">Home</router-link>|
            <router-link to="/about" class="text-primary">About</router-link>
        </div>
    </header>
</template>

<script>
export default {
    name: "Header"
};
</script>

<style scoped>
.header {
    text-align: center;
    padding: 10px;
}
.header a {
    padding-right: 5px;
    text-decoration: none;
}
</style>