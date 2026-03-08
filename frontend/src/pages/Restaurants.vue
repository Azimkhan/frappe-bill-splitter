<template>
  <div>
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-2xl font-bold text-ink-gray-9">Restaurants</h1>
      <Button variant="solid" @click="showCreateDialog = true">New Restaurant</Button>
    </div>

    <Dialog v-model="showCreateDialog" :options="{ title: 'New Restaurant' }">
      <template #body-content>
        <FormControl label="Restaurant Name" v-model="newName" />
      </template>
      <template #actions>
        <Button variant="solid" class="w-full" @click="createRestaurant" :loading="creating">
          Create
        </Button>
      </template>
    </Dialog>

    <div v-if="restaurants.list?.loading" class="text-ink-gray-5">Loading...</div>
    <div v-else-if="restaurants.list?.data?.length === 0" class="text-ink-gray-5">
      No restaurants yet.
    </div>
    <div v-else class="bg-surface-white rounded-lg border border-outline-gray-1 divide-y">
      <div
        v-for="r in restaurants.list?.data"
        :key="r.name"
        class="px-4 py-3 text-ink-gray-9"
      >
        {{ r.restaurant_name }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { createListResource } from "frappe-ui";
import { Button, Dialog, FormControl } from "frappe-ui";

const showCreateDialog = ref(false);
const creating = ref(false);
const newName = ref("");

const restaurants = createListResource({
  doctype: "Restaurant",
  fields: ["name", "restaurant_name"],
  orderBy: "restaurant_name asc",
  pageLength: 0,
  auto: true,
});

async function createRestaurant() {
  creating.value = true;
  try {
    await restaurants.insert.submit({ restaurant_name: newName.value });
    showCreateDialog.value = false;
    newName.value = "";
    restaurants.list.reload();
  } finally {
    creating.value = false;
  }
}
</script>
