import yt_dlp
import os

def download_tt():
    link = input("\n🔗 Встав посилання на TikTok: ")
    print("\nОбери формат:")
    print("1. Тільки звук (MP3)")
    print("2. Відео без водяного знака (MP4)")
    choice = input("\nТвій вибір (1 або 2): ")

    # Базовий шлях до завантажень
    base_path = '/data/data/com.termux/files/home/storage/downloads/%(title)s.%(ext)s'

    if choice == '1':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': base_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        msg = "🎵 Завантажую звук..."
    else:
        ydl_opts = {
            'format': 'best',
            'outtmpl': base_path,
        }
        msg = "🎬 Завантажую відео..."

    try:
        print(f"\n🚀 {msg}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"\n✅ Готово! Файл уже в папці Downloads.")
    except Exception as e:
        print(f"\n❌ Помилка: {e}")

if __name__ == "__main__":
    download_tt()


