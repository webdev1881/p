<template>
  <div class="hello">
    <input v-model="search" class="header_search">
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

  data: () => ({
    search: '',
  }),



  watch: {


    search(e) {
      if (e.length > 2) {
        this.isSearch = true
        this.suggest = []
        this.categories = []
        this.brands = []
        this.not_found = ''

        console.log(e)


      } else {
        this.isSearch = false
        this.suggest = []
        this.categories = []
        this.brands = []
        this.not_found = 'не знайдено'
      }
    },

  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header_search {
  width: 100%;
  height: 30px;
  padding: 0 10px;
}
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
