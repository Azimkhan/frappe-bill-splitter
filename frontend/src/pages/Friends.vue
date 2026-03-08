<template>
  <div>
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-2xl font-bold text-ink-gray-9">Friends</h1>
      <Button variant="solid" @click="showCreateDialog = true">New Friend</Button>
    </div>

    <Dialog v-model="showCreateDialog" :options="{ title: 'New Friend' }">
      <template #body-content>
        <FormControl label="Friend Name" v-model="newName" />
      </template>
      <template #actions>
        <Button variant="solid" class="w-full" @click="createFriend" :loading="creating">
          Create
        </Button>
      </template>
    </Dialog>

    <div v-if="friends.list?.loading" class="text-ink-gray-5">Loading...</div>
    <div v-else-if="friends.list?.data?.length === 0" class="text-ink-gray-5">
      No friends yet.
    </div>
    <div v-else class="bg-surface-white rounded-lg border border-outline-gray-1 divide-y">
      <div
        v-for="f in friends.list?.data"
        :key="f.name"
        class="px-4 py-3 text-ink-gray-9"
      >
        {{ f.friend_name }}
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

const friends = createListResource({
  doctype: "Friend",
  fields: ["name", "friend_name"],
  orderBy: "friend_name asc",
  pageLength: 0,
  auto: true,
});

async function createFriend() {
  creating.value = true;
  try {
    await friends.insert.submit({ friend_name: newName.value });
    showCreateDialog.value = false;
    newName.value = "";
    friends.list.reload();
  } finally {
    creating.value = false;
  }
}
</script>
