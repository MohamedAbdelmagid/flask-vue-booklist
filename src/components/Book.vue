<template>
    <div>
        <p>{{ book.title }}</p>
    </div>
</template>

<script>
export default {
    name: "Book",
    props: ["book"]
};
</script>

<style scoped>
</style>