<template>
    <tr>
        <td>{{ book.title }}</td>
        <td>{{ book.author }}</td>
        <td>
            <span v-if="book.read">Yes</span>
            <span v-else>No</span>
        </td>
        <td>
            <i style="font-size: 1.3em;" class="btn fas fa-paint-brush btn-sm"></i>
        </td>
        <td @click="$emit('del-book', book.id)">
            <i style="font-size: 1.3em;" class="btn fas fa-trash-alt btn-sm"></i>
        </td>
    </tr>
</template>

<script>
export default {
    name: "Book",
    props: ["book"]
};
</script>

<style scoped>
</style>