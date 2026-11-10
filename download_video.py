# Установка
# -------------------------------------------------
# pip install -U yt-dlp          # последняя версия
# pip install -U tqdm           # (необязательно) красивый индикатор прогресса

import yt_dlp
from pathlib import Path

def download_youtube(url: str):
    """
    Скачивает YouTube‑видео и возвращает путь к полученному файлу.

    Параметры
    ----------
    url: str
        Полный URL ролика.
    out_dir: str
        Папка, куда будет сохранён файл (по умолчанию текущая директория).
    pref_quality: str
        Предпочтительное разрешение (например, "720p", "1080p").
        Если такого качества нет, берётся самое лучшее доступное.
    as_mp4: bool
        Привести итоговый файл к MP4 (перекодировать, если нужно).

    Возврат
    -------
    pathlib.Path
        Полный путь к скачанному файлу.
    """
    as_mp4=True
    pref_quality='720p'
    out_dir='downloads/'

    try:
        out_dir_path = Path(out_dir).expanduser().resolve()
        out_dir_path.mkdir(parents=True, exist_ok=True)

        # шаблон имени: <название>.<расширение>
        outtmpl = str(out_dir_path / "%(title)s.%(ext)s")

        # Формируем запрос к yt-dlp
        ydl_opts = {
            "outtmpl": outtmpl,
            # Формат: сначала пробуем требуемое качество, если нет – best
            "format": f"bestvideo[height<={pref_quality[:-1]}]+bestaudio/best",
            "merge_output_format": "mp4" if as_mp4 else "mkv",
            "progress_hooks": [lambda d: print(f"{d['status'].title()}: {d.get('filename', '')}")],
            "quiet": False,
            "noprogress": False,
            "retries": 10,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        # Путь к итоговому файлу (может отличаться, если mp4‑конверсия выполнилась)
        filename = out_dir_path / f"{info.get('title')}.{'mp4' if as_mp4 else info.get('ext')}"
        return True


    except Exception as e:
        return False