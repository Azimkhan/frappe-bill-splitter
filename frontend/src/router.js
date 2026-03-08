import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/Home.vue";
import VisitDetail from "@/pages/VisitDetail.vue";
import Restaurants from "@/pages/Restaurants.vue";
import Friends from "@/pages/Friends.vue";
import MenuItems from "@/pages/MenuItems.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/visits/:id", name: "VisitDetail", component: VisitDetail },
  { path: "/restaurants", name: "Restaurants", component: Restaurants },
  { path: "/friends", name: "Friends", component: Friends },
  { path: "/menu-items", name: "MenuItems", component: MenuItems },
];

const router = createRouter({
  history: createWebHistory("/bill"),
  routes,
});

export default router;
