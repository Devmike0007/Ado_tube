import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import yt_dlp

app = Flask(__name__)

# Dossier de téléchargement
DOWNLOAD_FOLDER = os.path.join('adotube', 'videos')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)  # Crée le dossier s’il n’existe pas

def video_info(lien):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(lien, download=False)
        return info

@app.route("/download")
def download_video():
    lien = request.args.get('lien')
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(lien, download=True)
        filename = ydl.prepare_filename(info)
    nom_fichier = os.path.basename(filename)

    # Afficher une page qui lance le téléchargement automatique
    return render_template('resultat.html', filename=nom_fichier)

@app.route('/adotube/video/<filename>')
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

# Tes autres routes ici (index, accueil, apropos, traitement, resultat, etc.)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/accueil.html')
def accueil():
    return render_template('accueil.html')

@app.route('/apropos.html')
def apropos():
    return render_template('apropos.html')

@app.route('/comment_ca_marche.html')
def comment_ca_marche():
    return render_template('comment_ca_marche.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/traitement', methods=['GET'])
def traitement():
    lien = request.args.get('lien')
    info = video_info(lien)
    formats = [f for f in info['formats'] if f.get('vcodec') != 'none' and f.get('format_note')]
    return render_template('traitement.html', lien=lien, info=info, formats=formats)

@app.route('/resultat', methods=['GET'])
def resultat():
    lien = request.args.get('lien')
    info = video_info(lien)
    return render_template('resultat.html', lien=lien, info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
