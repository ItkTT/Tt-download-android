import customtkinter as ctk
import yt_dlp
import threading

def download():
    url = entry.get()
    if not url:
        label.configure(text="❌ Встав посилання!", text_color="red")
        return
    
    label.configure(text="⏳ Завантаження...", text_color="yellow")
    
    # Запускаємо в окремому потоці, щоб програма не зависала
    def run():
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '/data/data/com.termux/files/home/storage/downloads/%(title)s.%(ext)s',
                'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            label.configure(text="✅ Готово в Downloads!", text_color="green")
        except Exception as e:
            label.configure(text=f"❌ Помилка", text_color="red")

    threading.Thread(target=run).start()

# Налаштування вікна
app = ctk.CTk()
app.geometry("400x240")
app.title("TT Downloader")

label = ctk.CTkLabel(app, text="TikTok MP3 Downloader", font=("Arial", 20))
label.pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text="Посилання на відео", width=300)
entry.pack(pady=10)

btn = ctk.CTkButton(app, text="Скачати Звук", command=download)
btn.pack(pady=20)

app.mainloop()
