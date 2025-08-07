self.addEventListener('install', (e) => {
    console.log('Service Worker installé');
    self.skipWaiting();
});

self.addEventListener('activate', (e) => {
    console.log('Service Worker activé');
});

self.addEventListener('fetch', (e) => {
    // Optionnel : intercepter les requêtes pour cache, etc.
});
