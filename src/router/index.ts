import { createRouter, createWebHistory, type RouteLocationNormalized } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ProjectView from '../views/ProjectView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/proyectos/:slug', name: 'proyecto', component: ProjectView },
  ],
  scrollBehavior(to: RouteLocationNormalized, _from: RouteLocationNormalized, savedPosition) {
    if (savedPosition) return savedPosition;
    if (to.hash) return { el: to.hash, behavior: 'smooth' };
    return { top: 0 };
  },
});

export default router;
