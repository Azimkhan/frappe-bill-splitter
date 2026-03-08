<template>
	<div>
		<router-link
			to="/"
			class="text-sm text-ink-gray-5 hover:text-ink-gray-7 mb-4 inline-block"
		>
			&larr; Back to Visits
		</router-link>

		<div v-if="visitDoc" class="space-y-6">
			<div>
				<h1 class="text-2xl font-bold text-ink-gray-9">Visit #{{ visitDoc.name }}</h1>
				<p class="text-ink-gray-6 mt-1">
					<span class="font-medium">{{ visitDoc.restaurant }}</span>
					&middot; {{ formatDate(visitDoc.date) }}
				</p>
			</div>

			<!-- Items List -->
			<div>
				<h2 class="text-lg font-semibold text-ink-gray-9 mb-3">Items</h2>
				<div
					v-if="visitDoc.items?.length"
					class="bg-surface-white rounded-lg border border-outline-gray-1 divide-y"
				>
					<div
						v-for="(item, idx) in visitDoc.items"
						:key="item.name || idx"
						class="px-4 py-3"
					>
						<div class="flex justify-between items-start">
							<div>
								<span class="font-medium text-ink-gray-9">{{
									menuItemName(item.menu_item)
								}}</span>
								<span class="text-ink-gray-5 ml-2">x{{ item.quantity }}</span>
							</div>
							<div class="flex items-center gap-3">
								<span class="font-medium text-ink-gray-9">{{
									formatCurrency(item.price * item.quantity)
								}}</span>
								<button
									@click="removeItem(idx)"
									class="text-ink-gray-4 hover:text-ink-red-3 text-sm"
									title="Remove item"
								>
									&times;
								</button>
							</div>
						</div>
						<div v-if="item.friends?.length" class="mt-1 flex gap-1 flex-wrap">
							<span
								v-for="f in item.friends"
								:key="f.friend"
								class="inline-block text-xs bg-surface-blue-2 text-ink-blue-2 rounded px-2 py-0.5"
							>
								{{ friendName(f.friend) }}
							</span>
						</div>
					</div>
				</div>
				<p v-else class="text-ink-gray-5">No items added yet.</p>
			</div>

			<!-- Add Item Form -->
			<div class="bg-surface-white rounded-lg border border-outline-gray-1 p-4 space-y-4">
				<h3 class="font-semibold text-ink-gray-9">Add Item</h3>

				<div class="flex gap-2 justify-between">
					<div class="flex-grow">
						<label class="block text-sm font-medium text-ink-gray-7 mb-1"
							>Menu Item</label
						>
						<Select v-model="selectedMenuItem" :options="menuItemOptions"> </Select>
					</div>

					<div class="flex-grow">
						<label class="block text-sm font-medium text-ink-gray-7 mb-1"
							>Quantity</label
						>
						<TextInput v-model.number="quantity" type="number" min="1" />
					</div>
				</div>

				<div>
					<label class="block text-sm font-medium text-ink-gray-7 mb-1"
						>Friends sharing this item</label
					>
					<MultiSelect
						v-model="selectedFriends"
						:options="friendOptions"
						doctype="Friend"
					/>

					<p v-if="!friendOptions.length" class="text-ink-gray-4 text-sm">
						No friends found.
					</p>
				</div>

				<Button
					@click="addItem"
					:disabled="!selectedMenuItem || selectedFriends.length === 0"
				>
					Add
				</Button>
			</div>

			<!-- Total -->
			<div
				v-if="visitDoc.items?.length"
				class="bg-surface-white rounded-lg border border-outline-gray-1 p-4"
			>
				<div class="flex justify-between font-semibold text-ink-gray-9">
					<span>Total</span>
					<span>{{ formatCurrency(total) }}</span>
				</div>
			</div>

			<!-- Bill Split -->
			<div
				v-if="visitDoc.items?.length && billSplitEntries.length"
				class="bg-surface-white rounded-lg border border-outline-gray-1 p-4 space-y-3"
			>
				<div class="flex justify-between gap-2">
					<h2 class="text-lg font-semibold text-ink-gray-9">Bill Split {{ serviceFeeLabel }}</h2>
					<div class="flex items-center gap-2">
						<label class="block text-sm font-medium text-ink-gray-7 mb-1">Add service fee</label>
						<Checkbox v-model="addServiceFee" />
					</div>
				</div>
				<div class="divide-y">
					<div
						v-for="entry in billSplitEntries"
						:key="entry.friendId"
						class="flex justify-between py-2"
					>
						<span class="text-ink-gray-9">{{ entry.friendName }}</span>
						<span class="text-ink-gray-9 font-medium">
							{{ formatCurrency(entry.total) }}
							<span class="text-ink-gray-5 text-xs ml-1"  v-if="addServiceFee">
								({{ formatCurrency(entry.subtotal) }} +
								{{ formatCurrency(entry.service) }} service)
							</span>
						</span>
					</div>
				</div>
				<div
					class="border-t border-outline-gray-1 pt-2 flex justify-between font-semibold text-ink-gray-9"
				>
					<span>Total</span>
					<span>{{ formatCurrency(billSplitTotal) }}</span>
				</div>
			</div>
		</div>
		<div v-else class="text-ink-gray-5">Loading...</div>
	</div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useRoute } from "vue-router";
import { createResource, createListResource } from "frappe-ui";
import { Button, Checkbox, Select, MultiSelect, TextInput } from "frappe-ui";

const route = useRoute();

// Fetch visit with nested friends via custom API
const visitResource = createResource({
	url: "bill_splitter.bill_splitter.api.get_visit",
	params: { name: route.params.id },
	auto: true,
});

const visitDoc = computed(() => visitResource.data);
/**
 * {
    label: 'Pistachio Baklava',
    value: 'pistachio-baklava',
  },
 */
const menuItemOptions = computed(
	() =>
		menuItems.data?.map((mi) => ({
			label: mi.item_name + " - " + formatCurrency(mi.price),
			value: mi.name,
		})) || [],
);
// Save visit via custom API
const saveResource = createResource({
	url: "bill_splitter.bill_splitter.api.save_visit",
});

async function saveVisit() {
	const doc = JSON.parse(JSON.stringify(visitDoc.value));
	await saveResource.submit({ doc });
	visitResource.reload();
}

const serviceFee = computed(() => {
	return addServiceFee.value ? 0.1 : 0;
});
const serviceFeeLabel = computed(() => {
	return addServiceFee.value ? `(+${(serviceFee.value * 100).toFixed(0)}% service)` : "";
});
// Form state
const selectedMenuItem = ref(null);
const quantity = ref(1);
const selectedFriends = ref([]);
const addServiceFee = ref(false);

// Friends list
const friends = createListResource({
	doctype: "Friend",
	fields: ["name", "friend_name"],
	pageLength: 0,
	auto: true,
});

const friendOptions = computed(
	() => friends.data?.map((f) => ({ value: f.name, label: f.friend_name })) || [],
);

const updateSelectedFriends = (friend) => {
	console.log(friend);
	if (selectedFriends.value.includes(friend)) {
		console.log("removing", selectedFriends.value);
		selectedFriends.value = selectedFriends.value.filter((f) => f !== friend);
	} else {
		console.log("adding", selectedFriends.value);
		selectedFriends.value = [...selectedFriends.value, friend];
	}
};
// Menu items list (filtered by restaurant)
const menuItems = createListResource({
	doctype: "Menu Item",
	fields: ["name", "item_name", "price"],
	pageLength: 0,
});

watch(
	() => visitDoc.value?.restaurant,
	(restaurant) => {
		if (restaurant) {
			menuItems.update({
				filters: { restaurant },
			});
			menuItems.list.fetch();
		}
	},
	{ immediate: true },
);

// Lookup maps
const menuItemMap = computed(() => {
	const map = {};
	if (!menuItems.data) return map;
	for (const mi of menuItems.data) {
		map[mi.name] = mi.item_name;
	}
	return map;
});

const friendMap = computed(() => {
	const map = {};
	if (!friends.data) return map;
	for (const f of friends.data) {
		map[f.name] = f.friend_name;
	}
	return map;
});

function menuItemName(id) {
	return menuItemMap.value[id] || id;
}

function friendName(id) {
	return friendMap.value[id] || id;
}

// Total
const total = computed(() => {
	if (!visitDoc.value?.items) return 0;
	return visitDoc.value.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
});

// Bill split
const billSplit = computed(() => {
	if (!visitDoc.value?.items) return {};
	const perFriend = {};
	for (const item of visitDoc.value.items) {
		if (!item.friends?.length) continue;
		const itemTotal = item.price * item.quantity;
		const share = itemTotal / item.friends.length;
		for (const f of item.friends) {
			perFriend[f.friend] = (perFriend[f.friend] || 0) + share;
		}
	}
	return perFriend;
});

const billSplitEntries = computed(() => {
	return Object.entries(billSplit.value).map(([friendId, subtotal]) => ({
		friendId,
		friendName: friendName(friendId),
		subtotal,
		service: subtotal * serviceFee.value,
		total: subtotal * (1 + serviceFee.value),
	}));
});

const billSplitTotal = computed(() => {
	return billSplitEntries.value.reduce((sum, e) => sum + e.total, 0);
});

// Add item
function addItem() {
	console.log(selectedMenuItem.value);
	const menuItem = menuItems.data.find((mi) => mi.name === selectedMenuItem.value);
	if (!menuItem || selectedFriends.value.length === 0) return;
	const item = {
		menu_item: menuItem.name,
		price: menuItem.price,
		quantity: quantity.value,
		friends: selectedFriends.value.map((f) => ({ friend: f })),
	};
	console.log(item);
	visitDoc.value.items.push(item);
	saveVisit();
	selectedMenuItem.value = null;
	quantity.value = 1;
	selectedFriends.value = [];
}

// Remove item
function removeItem(idx) {
	visitDoc.value.items.splice(idx, 1);
	saveVisit();
}

function formatDate(dt) {
	if (!dt) return "";
	return new Date(dt).toLocaleDateString();
}

function formatCurrency(val) {
	return new Intl.NumberFormat("kk-KZ", {
		style: "currency",
		currency: "KZT",
		maximumFractionDigits: 0,
	}).format(val);
}
</script>
