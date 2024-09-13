<template>
  <div id="app">
    <router-link to="/chat">Go to Chat</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>
