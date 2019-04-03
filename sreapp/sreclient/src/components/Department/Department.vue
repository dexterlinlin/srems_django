<template>
    <div class="Department">
        <h1>{{ msg }}</h1>
        <pre v-text="$attrs"/>
    </div>
</template>

<script>
    export default {
        name:'Department',
        props: {
        },
        data():{
        return {msg:'dept component'}
        }
    };
</script>
