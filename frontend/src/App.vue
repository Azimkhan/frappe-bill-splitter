<template>
  <FrappeUIProvider>
    <div class="min-h-screen bg-surface-gray-2">
      <nav class="bg-surface-white border-b border-outline-gray-1 px-4 py-3 flex items-center gap-6">
        <router-link to="/" class="font-semibold text-lg text-ink-gray-9">
          Bill Splitter
        </router-link>
        <router-link
          v-for="link in navLinks"
          :key="link.to"
          :to="link.to"
          class="text-sm text-ink-gray-6 hover:text-ink-gray-9"
        >
          {{ link.label }}
        </router-link>
        <div class="ml-auto">
          <Dropdown :options="userMenuOptions">
            <template #default="{ open }">
              <button
                class="rounded-full focus:outline-none focus:ring-2 focus:ring-outline-gray-3"
                @click="open"
              >
                <Avatar
                  :image="userResource.data?.user_image"
                  :label="userResource.data?.full_name"
                  size="md"
                />
              </button>
            </template>
          </Dropdown>
        </div>
      </nav>
      <main class="max-w-4xl mx-auto p-6">
        <router-view />
      </main>
    </div>
  </FrappeUIProvider>
</template>

<script setup>
import { computed } from "vue";
import {
  FrappeUIProvider,
  Avatar,
  Dropdown,
  useTheme,
  createResource,
  call,
} from "frappe-ui";

const { currentTheme, toggleTheme, setTheme } = useTheme();

const themeMap = { Light: "light", Dark: "dark", Automatic: "system" };
const userId = document.cookie.match(/user_id=([^;]+)/)?.[1];

const userResource = createResource({
  url: "frappe.client.get_value",
  params: {
    doctype: "User",
    filters: userId ? decodeURIComponent(userId) : "Guest",
    fieldname: ["desk_theme", "full_name", "user_image"],
  },
  auto: true,
  onSuccess(data) {
	const theme = data?.desk_theme || "Automatic";
    setTheme(themeMap[theme]);
  },
});

const reverseThemeMap = { light: "Light", dark: "Dark", system: "Automatic" };

const effectiveTheme = computed(() => {
  if (currentTheme.value === "system") {
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }
  return currentTheme.value;
});

async function handleToggleTheme() {
  toggleTheme();
  const newTheme = currentTheme.value;
  await call("frappe.core.doctype.user.user.switch_theme", {
    theme: reverseThemeMap[newTheme] || "Light",
  });
}

async function logout() {
  await call("logout");
  window.location.href = "/login";
}

const userMenuOptions = computed(() => [
  { label: userResource.data?.full_name || "User", disabled: true },
  {
    label: effectiveTheme.value === "dark" ? "Light Mode" : "Dark Mode",
    icon: effectiveTheme.value === "dark" ? "sun" : "moon",
    onClick: handleToggleTheme,
  },
  {
    label: "Desk",
    icon: "layout-grid",
    onClick: () => (window.location.href = "/app"),
  },
  { label: "Logout", icon: "log-out", onClick: logout },
]);

const navLinks = [
  { to: "/", label: "Visits" },
  { to: "/restaurants", label: "Restaurants" },
  { to: "/friends", label: "Friends" },
  { to: "/menu-items", label: "Menu Items" },
];
</script>
