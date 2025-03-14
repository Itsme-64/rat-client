import sys
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
import webbrowser
import os

# Load image from bundled resources
def get_resource_path(relative_path):
    """ Get the absolute path to a resource, works for development and PyInstaller. """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

IMAGE_PATH = get_resource_path("image.png")

class ImagePopup(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rat Client")
        self.geometry("400x400")
        self.resizable(False, False)

        # Load image
        image = Image.open(IMAGE_PATH)
        image = image.resize((400, 300), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        # Display image
        self.label = tk.Label(self, image=self.photo)
        self.label.pack()

        # Add button in center
        self.button = Button(self, text="Inject", command=self.open_videos, width=12, height=2, font=("Arial", 14))
        self.button.pack()

    def open_videos(self):
        urls = [
            "https://youtu.be/xKwjoXJqKt4",
            "https://youtu.be/jAcR6uSRuTo",
            "https://youtu.be/rrp7qBhnxbg",
            "https://youtu.be/1rh1_f_kO-I",
            "https://youtu.be/-5Yo5cnpuUA",
            "https://youtu.be/2TjUuPul3LE",
            "https://youtu.be/X0V6Z4hYsIU",
            "https://youtu.be/n3eFSpcsSnQ",
            "https://youtu.be/B8oXNF7NEYE",
            "https://youtu.be/5PBHegS94_Y",
            "https://youtu.be/3GvTXPcvPB4",
            "https://www.youtube.com/@Itsme64?sub_confirmation=1"
        ]
        for url in urls:
            webbrowser.open(url)
        self.destroy()

if __name__ == "__main__":
    app = ImagePopup()
    app.mainloop()