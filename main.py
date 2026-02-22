import flet as ft
import yt_dlp

def main(page: ft.Page):
    page.title = "TT Downloader"
    page.theme_mode = ft.ThemeMode.DARK # Темна тема, як у справжнього хакера
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Поле для введення посилання
    url_input = ft.TextField(label="Встав посилання на TikTok", width=300)
    
    # Текст статусу
    status_text = ft.Text()

    def download_click(e):
        link = url_input.value
        if not link:
            status_text.value = "❌ Будь ласка, встав посилання!"
            page.update()
            return
        
        status_text.value = "⏳ Завантаження почалося..."
        status_text.color = ft.colors.BLUE_200
        page.update()

        try:
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
            
            status_text.value = "✅ Звук збережено в Downloads!"
            status_text.color = ft.colors.GREEN_400
        except Exception as ex:
            status_text.value = f"❌ Помилка: {ex}"
            status_text.color = ft.colors.RED_400
        
        page.update()

    # Кнопка
    download_btn = ft.ElevatedButton("Скачати MP3", on_click=download_click)

    # Додаємо елементи на екран
    page.add(
        ft.Column(
            [
                ft.Text("TT Audio Downloader", size=30, weight="bold"),
                url_input,
                download_btn,
                status_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
