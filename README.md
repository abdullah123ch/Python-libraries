# Python-libraries: PyWhatKit & PyAutoGUI

This repository contains example scripts and usage guides for two powerful Python libraries: **PyWhatKit** and **PyAutoGUI**. These libraries enable automation of tasks such as messaging, searching, and GUI interactions.

---

## PyWhatKit

**PyWhatKit** is a versatile Python library designed for automating WhatsApp messaging, YouTube, Google searches, text-to-handwriting conversion, ASCII art, and even sending emails.

### Key Features

- **WhatsApp Automation:** Send messages, images, and group messages automatically.
- **YouTube Automation:** Play YouTube videos by topic.
- **Text to Handwriting:** Convert plain text into handwriting-style images.
- **ASCII Art:** Convert text into ASCII art.
- **Google Search:** Automate Google searches and retrieve information.
- **Email Automation:** Send plain text and HTML emails programmatically.

## PyAutoGUI

**PyAutoGUI** is a Python library for automating mouse and keyboard interactions, taking screenshots, and interacting with on-screen elements.

### Key Features

- **Mouse Automation:** Move, click, drag, and scroll the mouse.
- **Keyboard Automation:** Type text, press keys, use hotkeys, and hold keys.
- **Screen Interaction:** Take screenshots, locate images on the screen, and interact with GUI elements.
- **Message Boxes:** Display alerts, confirmations, prompts, and password dialogs.
- **Fail-Safes:** Built-in safety features to abort automation if needed.

## Requirements

- Python 3.x
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [Pillow](https://pypi.org/project/Pillow/) (for screenshots with PyAutoGUI)

Install dependencies using pip:

```sh
pip install pywhatkit pyautogui pillow
```

---

## Notes

- **PyWhatKit:** Some features (like WhatsApp and email automation) may require additional setup or credentials.
- **PyAutoGUI:** Automation scripts can move your mouse and type on your keyboard. Use with caution and always test in a controlled environment.

---

## License

This repository is for educational purposes. Please refer to the respective libraries for their licenses.
