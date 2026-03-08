<template>
  <div>
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-2xl font-bold text-ink-gray-9">Menu Items</h1>
      <Button variant="solid" @click="showCreateDialog = true">New Menu Item</Button>
    </div>

    <Dialog v-model="showCreateDialog" :options="{ title: 'New Menu Item' }">
      <template #body-content>
        <div class="space-y-4">
          <FormControl label="Item Name" v-model="newItem.item_name" />
          <FormControl label="Price" type="number" v-model="newItem.price" />
          <FormControl
            label="Restaurant"
            type="select"
            :options="[{ label: 'Select a restaurant', value: '' }, ...restaurantOptions]"
            v-model="newItem.restaurant"
          />
        </div>
      </template>
      <template #actions>
        <Button variant="solid" class="w-full" @click="createMenuItem" :loading="creating">
          Create
        </Button>
      </template>
    </Dialog>

    <div v-if="menuItems.list?.loading" class="text-ink-gray-5">Loading...</div>
    <div v-else-if="menuItems.list?.data?.length === 0" class="text-ink-gray-5">
      No menu items yet.
    </div>
    <div v-else class="bg-surface-white rounded-lg border border-outline-gray-1 divide-y">
      <div
        v-for="item in menuItems.list?.data"
        :key="item.name"
        class="px-4 py-3 flex justify-between items-center"
      >
        <div>
          <span class="font-medium text-ink-gray-9">{{ item.item_name }}</span>
          <span class="text-sm text-ink-gray-5 ml-2">{{ item.restaurant }}</span>
        </div>
        <span class="text-ink-gray-9">{{ formatCurrency(item.price) }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from "vue";
import { createListResource } from "frappe-ui";
import { Button, Dialog, FormControl } from "frappe-ui";

const showCreateDialog = ref(false);
const creating = ref(false);
const newItem = reactive({ item_name: "", price: "", restaurant: "" });

const menuItems = createListResource({
  doctype: "Menu Item",
  fields: ["name", "item_name", "price", "restaurant"],
  orderBy: "item_name asc",
  pageLength: 0,
  auto: true,
});

const restaurants = createListResource({
  doctype: "Restaurant",
  fields: ["name", "restaurant_name"],
  pageLength: 0,
  auto: true,
});

const restaurantOptions = computed(() =>
  (restaurants.list?.data || []).map((r) => ({
    label: r.restaurant_name,
    value: r.name,
  }))
);

function formatCurrency(val) {
  return new Intl.NumberFormat(undefined, { style: "currency", currency: "KZT" }).format(val);
}

async function createMenuItem() {
  creating.value = true;
  try {
    await menuItems.insert.submit({
      item_name: newItem.item_name,
      price: newItem.price,
      restaurant: newItem.restaurant,
    });
    showCreateDialog.value = false;
    newItem.item_name = "";
    newItem.price = "";
    newItem.restaurant = "";
    menuItems.list.reload();
  } finally {
    creating.value = false;
  }
}
</script>
