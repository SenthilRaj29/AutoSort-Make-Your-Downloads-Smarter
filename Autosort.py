import os
import shutil
from datetime import datetime
from plyer import notification

DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Installers': ['.exe', '.msi'],
    'Others': []
}

LOG_FILE = os.path.join(DOWNLOADS_FOLDER, "organizer_log.txt")

def log_action(message):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def organize_downloads():
    files_moved = 0
    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)
            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(DOWNLOADS_FOLDER, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file_name))
                    log_action(f"Moved {file_name} -> {category}/")
                    files_moved += 1
                    moved = True
                    break

            if not moved:
                dest_folder = os.path.join(DOWNLOADS_FOLDER, "Others")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file_name))
                log_action(f"Moved {file_name} -> Others/")
                files_moved += 1

    return files_moved

if __name__ == "__main__":
    print("🧹 Organizing your Downloads folder...")
    moved_count = organize_downloads()
    print(f"✅ Done! {moved_count} files organized.")

    notification.notify(
        title="Downloads Folder Organized ✅",
        message=f"{moved_count} files were sorted!",
        timeout=5
    )
