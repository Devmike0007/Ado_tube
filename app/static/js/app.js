if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('sw.js')
    .then(() => console.log('✅ Service Worker enregistré'))
    .catch(e => console.log('❌ Erreur SW :', e));
}
