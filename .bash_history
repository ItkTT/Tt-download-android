pip install flet
nano main.py
python main.py7
pkg install tur-repo -y
pkg install python-streamlit -y
pkg update
pkg install python-streamlit -y
pkg install python-tkinter x11-repo -y
pip install customtkinter
nano gui_app.py
pip install flask
cat <<EOF > web_app.py
from flask import Flask, render_template_string, request
import yt_dlp
import os

app = Flask(__name__)

# Красивый дизайн в стиле PUBG/Dark Theme
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>TT Downloader</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background-color: #121212; color: white; font-family: sans-serif; text-align: center; padding: 20px; }
        input { width: 80%; padding: 15px; border-radius: 10px; border: none; margin-bottom: 20px; }
        button { background-color: #ffb100; color: black; padding: 15px 30px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; width: 85%; }
        .status { margin-top: 20px; color: #00ff00; }
    </style>
</head>
<body>
    <h1>🎬 TT MP3 Loader</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Вставь ссылку на TikTok" required><br>
        <button type="submit">СКАЧАТЬ MP3</button>
    </form>
    {% if status %}
        <div class="status">{{ status }}</div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    status = ""
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '/data/data/com.termux/files/home/storage/downloads/%(title)s.%(ext)s',
                'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            status = "✅ Готово! Проверь папку Downloads"
        except Exception as e:
            status = f"❌ Ошибка: {e}"
    return render_template_string(HTML, status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

nano web_app.py
python web_app.py
nano web_app.py
python web_app.py
nano web_app.py
python web_app.py
python ~/web_app.py
pkg install termux-services -y
exit
pkg install python ffmpeg
pip install yt-dlp
pkg update
pkg upgrade
pkg install python ffmpeg -y
pip install yt-dlp
termux-setup-storage
python tt.down.py
ls
tt.down.py
python tt.down.py
python tt.py
cat <<EOF > tt.py
import yt_dlp
def download():
    link = input("\n🔗 Встав посилання на TikTok: ")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/data/data/com.termux/files/home/storage/downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("\n✅ Готово! Шукай у завантаженнях телефону.")
download()
EOF

ls
python tt.py
echo "alias d='python ~/tt.py'" >> ~/.bashrc
source ~/.bashrc
d
nano tt.py
python tt.py
exit
