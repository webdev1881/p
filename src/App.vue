<template>
  <div class="app">
    <HelloWorld />
    <h1>{{ product.product_name }}</h1>
    <!-- <a :href="product.product_link" target="_blank">Перейти до продукту</a> -->
    <table>
      <thead>
        <tr>
          <th>Магазин</th>
          <th>Ціна</th>
          <th>Посилання</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="shop in product.shops" :key="shop.shop_link">
          <td>{{ shop.shop_name }}</td>
          <td>{{ shop.price }}</td>
          <td><a :href="shop.shop_link" target="_blank">Перейти</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import { ref } from 'vue';

import data from './../product.json';

import HelloWorld from './components/HelloWorld.vue'

export default {
  components: {
    HelloWorld
  },
  setup() {
    const product = data

    product.shops.sort((a, b) => {
      if (a.price < b.price) {
        return -1;
      }
      if (a.price > b.price) {
        return 1;
      }
      return 0;
    });

    // async function fetchData() {
    //   const response = await fetch('/product.json'); // JSON файл розміщений локально
    //   product.value = await response.json();
    // }

    // fetchData();

    return { product };
  },
};
</script>

<style>
.app {
  font-family: Arial, sans-serif;
  padding: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

table th, table td {
  border: 1px solid #ddd;
  padding: 8px;
}

table th {
  background-color: #f4f4f4;
  text-align: left;
}

a {
  color: #3498db;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
