# AutoSort🔁-Make-Your-Downloads-Smarter


## ✨ Features

- 📂 Organizes files by type into subfolders
- 🔁 Handles all major file types: `.jpg`, `.pdf`, `.mp4`, `.zip`, `.exe`, and more
- 📝 Keeps a clean `organizer_log.txt` for tracking what was moved and when
- 🧼 Cleans clutter in seconds with no user effort
- 🔔 Sends a desktop notification when done
- 🎨 ASCII art banner, color output & spinner animation
- 🧠 Smart fallback — unknown file types go to "Others"

---

## 🛠 Technologies Used

| Tool         | Purpose                           |
|--------------|------------------------------------|
| Python 3     | Core language                     |
| `os`         | Path navigation, folder ops       |
| `shutil`     | File moving operations            |
| `datetime`   | Timestamp for logging             |
| `plyer`      | Cross-platform desktop notification |
| `colorama`   | Colored terminal output           |
| `pyfiglet`   | ASCII art banner                  |

---

## ⚙️ How to Run

1. **Clone or download** the repository
2. **Install required libraries**:
   ```bash
   pip install plyer colorama pyfiglet
Run the script:

bash

Copy

Edit

python Autosort.py
Watch the magic happen 🪄

📦 Folder Structure After Running
Copy
Edit
Downloads/

├── Images/

├── Documents/

├── Videos/

├── Music/

├── Archives/

├── Installers/

├── Others/

└── organizer_log.txt


🔍 Use Cases

Daily or weekly Downloads cleanup

Automate organization for shared systems or work PCsPart of larger automation workflows (combine with file backup, cloud sync, etc.)

🌱 Future Improvements

Add GUI version with progress bar using Tkinter or PyQt

Drag-and-drop folder support

Option to select target folder at runtime

Add support for tagging or renaming files

Scheduled cleanup (cronjob/task scheduler integration)

🧠 Practical Applications

Increases productivity by removing clutter

Saves time in manually searching for files

Great for students, professionals, developers

Helps maintain system hygiene effortlessly
