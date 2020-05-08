<template>
    <div id="app">
        <Header />
        <router-view />
    </div>
</template>

<script>
import Header from "@/components/layout/Header";

export default {
    name: "app",
    components: {
        Header
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
.content-section {
    -webkit-border-radius: 10px 10px 10px 10px;
    border-radius: 10px 10px 10px 10px;
    border: 1px solid #dddddd;
    background: #ffffff;
    padding: 30px;
    width: 90%;
    max-width: 550px;
    position: relative;
}
</style>
