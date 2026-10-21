import { createRouter, createWebHistory, type RouteLocationNormalized } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ProjectView from '../views/ProjectView.vue';
import { projects } from '../data/projects';

const DEFAULT_TITLE = 'Cordova Solutions | Soluciones Digitales B2B';

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

// Centralized here (not in each view) so the title always matches the
// current route, including when navigating back to a route that doesn't
// set its own title.
router.afterEach((to) => {
  if (to.name === 'proyecto') {
    const project = projects.find((p) => p.slug === to.params.slug);
    document.title = project ? `${project.nombre} | Cordova Solutions` : `Proyecto no encontrado | Cordova Solutions`;
  } else {
    document.title = DEFAULT_TITLE;
  }
});

export default router;
