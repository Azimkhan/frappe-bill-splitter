<template>
  <div>
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-2xl font-bold text-ink-gray-9">Visits</h1>
      <Button variant="solid" @click="showCreateDialog = true">New Visit</Button>
    </div>

    <Dialog v-model="showCreateDialog" :options="{ title: 'New Visit' }">
      <template #body-content>
        <div class="space-y-4">
          <FormControl
            label="Restaurant"
            type="select"
            :options="[{ label: 'Select a restaurant', value: '' }, ...restaurantOptions]"
            v-model="newVisit.restaurant"
          />
          <FormControl
            label="Date"
            type="datetime-local"
            v-model="newVisit.date"
          />
        </div>
      </template>
      <template #actions>
        <Button variant="solid" class="w-full" @click="createVisit" :loading="creating">
          Create
        </Button>
      </template>
    </Dialog>

    <div v-if="visits.list?.loading" class="text-ink-gray-5">Loading...</div>
    <div v-else-if="visits.list?.data?.length === 0" class="text-ink-gray-5">
      No visits yet. Create one to get started.
    </div>
    <div v-else class="bg-surface-white rounded-lg border border-outline-gray-1 divide-y">
      <router-link
        v-for="visit in visits.list?.data"
        :key="visit.name"
        :to="`/visits/${visit.name}`"
        class="block px-4 py-3 hover:bg-surface-gray-2"
      >
        <div class="flex justify-between items-center">
          <div>
            <span class="font-medium text-ink-gray-9">{{ visit.restaurant }}</span>
			<span class="text-sm text-ink-gray-5 ml-2">{{ formatDate(visit.date) }}</span>

          </div>
		  <span class="text-ink-gray-4 ml-2">#{{ visit.name }}</span>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from "vue";
import { useRouter } from "vue-router";
import { createListResource } from "frappe-ui";
import { Button, Dialog, FormControl } from "frappe-ui";

const router = useRouter();
const showCreateDialog = ref(false);
const creating = ref(false);
const newVisit = reactive({ restaurant: "", date: "" });

const visits = createListResource({
  doctype: "Visit",
  fields: ["name", "restaurant", "date"],
  orderBy: "date desc",
  pageLength: 50,
  auto: true,
});

const restaurants = createListResource({
  doctype: "Restaurant",
  fields: ["name", "restaurant_name"],
  pageLength: 0,
  auto: true,
});

const restaurantOptions = computed(() =>
  (restaurants.data || []).map((r) => ({
    label: r.restaurant_name,
    value: r.name,
  }))
);

function formatDate(dt) {
  if (!dt) return "";
  return new Date(dt).toLocaleString("en-US", { year: "numeric", month: "long", day: "numeric", hour: "2-digit", minute: "2-digit" });
}

async function createVisit() {
  creating.value = true;
  try {
    const doc = await visits.insert.submit({
      restaurant: newVisit.restaurant,
      date: newVisit.date,
    });
    showCreateDialog.value = false;
    newVisit.restaurant = "";
    newVisit.date = "";
    router.push(`/visits/${doc.name}`);
  } finally {
    creating.value = false;
  }
}
</script>
