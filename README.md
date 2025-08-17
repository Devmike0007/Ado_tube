# Adotube

**Adotube** est une plateforme simple et intuitive pour **télécharger des vidéos** depuis différentes sources, avec contrôle sur la résolution et une interface facile à utiliser.

---

## 🖥️ Technologies utilisées

* **Frontend :** HTML, CSS, JavaScript
* **Backend :** Python Flask
* **Modules Python :**

  * `Flask` – pour le serveur web
  * `os` – gestion des fichiers et dossiers
  * `yt_dlp` – téléchargement de vidéos depuis diverses plateformes

---

## ⚙️ Installation

1. **Cloner le dépôt :**

```bash
git clone https://github.com/ton-utilisateur/adotube.git
cd adotube
```

2. **Créer un environnement virtuel :**

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

3. **Installer les dépendances :**

```bash
pip install -r requirements.txt
```

4. **Lancer le serveur Flask :**

```bash
python app.py
```

5. **Accéder à l’application :**

* Ouvrir le navigateur à `http://localhost:5000`
* Ou utiliser LocalTunnel pour un accès externe :

```bash
lt --port 5000 --subdomain adotube
```

---

## 🚀 Fonctionnement

1. L’utilisateur copie le **lien d’une vidéo** qu’il souhaite télécharger.
2. Il colle ce lien dans Adotube et clique sur **Télécharger**.
3. Un panneau permet de choisir la **résolution de la vidéo**.
4. Le téléchargement se lance et la vidéo est enregistrée localement.

> ⚠️ Le temps de téléchargement dépend de la taille et de la durée de la vidéo.

---

## 🔧 Gestion des cookies

Certaines vidéos nécessitent des cookies pour être téléchargées :

1. Copier les cookies depuis le navigateur.
2. Les sauvegarder dans un fichier JSON ou TXT dans le dossier parent du projet.
3. Au lancement, Adotube récupère ces cookies pour faciliter le téléchargement.

---

## 💡 Difficultés rencontrées

* **Pytube** était limité à YouTube, ce qui ne correspondait pas à l’objectif multi-plateformes.
* La gestion des cookies a été un défi pour certaines vidéos nécessitant une connexion.
* Après quelques ajustements, le projet fonctionne correctement avec `yt_dlp`.

---

## 📝 Notes

* Projet en développement : certaines fonctionnalités comme l’hébergement complet ou le frontend amélioré sont à venir.
* Actuellement, le projet peut être testé en local ou via LocalTunnel.
