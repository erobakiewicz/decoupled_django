<template>
  <div id="app">
    <InvoiceCreate />
  </div>
</template>

<script>
import InvoiceCreate from "@/components/InvoiceCreate";

export default {
  name: "App",
  components: {
    InvoiceCreate,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
