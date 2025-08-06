import yt_dlp

url = "https://youtu.be/sxOiHtpzlsI"

ydl_opts = {
    'cookiesfrombrowser': ('chrome',),
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
