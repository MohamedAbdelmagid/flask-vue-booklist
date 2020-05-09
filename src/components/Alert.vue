<template>
    <div>
        <br />
        <div
            class="alert"
            role="alert"
            v-bind:class="{'alert-success':!isDanger, 'alert-danger':isDanger}"
        >{{ message }}</div>
    </div>
</template>

<script>
export default {
    props: ["message", "isDanger"]
};
</script>