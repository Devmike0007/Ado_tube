from flask import Flask, render_template,request,redirect,url_for
import yt_dlp
# Initialisation de l'application Flask

app = Flask(__name__)



def video_info(lien):
    ydl_opts = {
        'quiet': True,          # Ne pas afficher les logs
        'skip_download': True,  # Ne pas télécharger la vidéo
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(lien, download=False)
        return info
    
@app.route("/download")
def download_video():
    lien = request.args.get('lien')
    ydl_opts = {
        'format': 'best',  # Télécharger la meilleure qualité
        'outtmpl': '%(title)s.%(ext)s',  # Nom du fichier de sortie
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([lien])
    return redirect(url_for('traitement', lien=lien))

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
    return render_template('traitement.html', lien=lien, info=info)



app.run(debug=True)