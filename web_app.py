from flask import Flask, render_template_string, request, send_from_directory
from flask_socketio import SocketIO, emit
import yt_dlp
import os
import threading

app = Flask(__name__)
socketio = SocketIO(app)

# Шлях до папки завантажень
DL_FOLDER = '/data/data/com.termux/files/home/storage/downloads/'

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>TT ULTIMATE PRO v3.5</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <style>
        body { background: #0f0f0f; color: #e0e0e0; font-family: sans-serif; text-align: center; padding: 20px; }
        .card { max-width: 450px; margin: auto; background: #1a1a1a; padding: 25px; border-radius: 20px; border: 1px solid #333; }
        h1 { color: #ffb100; text-transform: uppercase; letter-spacing: 2px; }
        input { width: 100%; padding: 15px; border-radius: 10px; border: 1px solid #444; background: #121212; color: white; margin-bottom: 20px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; background: #ffb100; color: #000; margin-bottom: 10px; }
        .progress-container { width: 100%; background: #333; border-radius: 10px; margin: 20px 0; display: none; }
        .progress-bar { width: 0%; height: 10px; background: #ffb100; border-radius: 10px; transition: 0.3s; }
        .history { text-align: left; margin-top: 30px; border-top: 1px solid #333; padding-top: 20px; }
        .file-item { font-size: 13px; margin-bottom: 15px; background: #252525; padding: 10px; border-radius: 8px; }
        audio { width: 100%; height: 30px; margin-top: 5px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🎬 TT ULTIMATE PRO</h1>
        <input type="text" id="url" placeholder="Встав посилання тут..." autofocus>
        <button onclick="startDownload('mp3')">ЗАВАНТАЖИТИ MP3</button>
        <button style="background:#444; color:white" onclick="startDownload('mp4')">ЗАВАНТАЖИТИ MP4</button>
        
        <div class="progress-container" id="p-cont"><div class="progress-bar" id="p-bar"></div></div>
        <div id="status-text" style="color:#ffb100">Готовий</div>

        <div class="history">
            <h3>Останні файли:</h3>
            <div id="file-list">
                {% for file in files %}
                <div class="file-item">
                    <div>🎵 {{ file }}</div>
                    {% if file.endswith('.mp3') %}
                    <audio controls><source src="/download/{{ file }}" type="audio/mpeg"></audio>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>
    </div>

    <script>
        var socket = io();
        function startDownload(type) {
            var url = document.getElementById('url').value;
            if(!url) return;
            document.getElementById('p-cont').style.display = 'block';
            socket.emit('download_request', {url: url, type: type});
            document.getElementById('url').value = ''; 
        }
        socket.on('progress', function(data) {
            document.getElementById('p-bar').style.width = data.percent + '%';
            document.getElementById('status-text').innerText = 'Завантаження: ' + data.percent + '%';
        });
        socket.on('done', function(data) {
            document.getElementById('status-text').innerText = '✅ Готово!';
            location.reload(); // Оновлюємо список файлів
        });
    </script>
</body>
</html>
'''

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(DL_FOLDER, filename)

def progress_hook(d):
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0%').replace('%','')
        socketio.emit('progress', {'percent': p})

@socketio.on('download_request')
def handle_download(data):
    url, fmt = data['url'], data['type']
    opts = {'outtmpl': DL_FOLDER + '%(title)s.%(ext)s', 'progress_hooks': [progress_hook], 'quiet': True}
    if fmt == 'mp3':
        opts.update({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]})
    
    def run():
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        socketio.emit('done')
    threading.Thread(target=run).start()

@app.route('/')
def index():
    try:
        files = sorted(os.listdir(DL_FOLDER), key=lambda x: os.path.getmtime(os.path.join(DL_FOLDER, x)), reverse=True)[:5]
    except: files = []
    return render_template_string(HTML, files=files)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
