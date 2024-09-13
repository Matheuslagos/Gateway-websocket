import { createRouter, createWebHistory } from 'vue-router';
import Chat from '../components/Chat.vue';

const routes = [
  {
    path: '/chat',
    name: 'Chat',
    component: Chat
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
