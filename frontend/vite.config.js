import path from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import frappeui from "frappe-ui/vite";

export default defineConfig({
  plugins: [
    frappeui({
      frappeProxy: true,
      lucideIcons: true,
      jinjaBootData: true,
      buildConfig: {
        indexHtmlPath: "../bill_splitter/www/_bill.html",
      },
    }),
    vue(),
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
  build: {
    outDir: "../bill_splitter/public/frontend",
    emptyOutDir: true,
  },
  optimizeDeps: {
    include: [
      "feather-icons",
      "engine.io-client",
      "interactjs",
      "socket.io-client",
    ],
    exclude: ["frappe-ui"],
  },
});
