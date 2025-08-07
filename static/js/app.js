let deferredPrompt;
const installBtn = document.getElementById('installBtn');

// Écoute l'événement avant-installation
window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault(); // Empêche Chrome de montrer le prompt par défaut
    deferredPrompt = e;
    installBtn.style.display = 'block';

    installBtn.addEventListener('click', () => {
        installBtn.style.display = 'none';
        deferredPrompt.prompt();

        deferredPrompt.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('Installation acceptée');
            } else {
                console.log('Installation refusée');
            }
            deferredPrompt = null;
        });
    });
});

// Enregistre le Service Worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/static/js/service-worker.js')
        .then(() => console.log('Service Worker enregistré !'))
        .catch(err => console.error('Erreur SW :', err));
}
