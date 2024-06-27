from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter


def download_video(url, save_path):
    try:
        yt = YouTube(url)

        # Choose best video based on both resolution and file size
        best_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        if best_stream is not None:
            best_stream.download(save_path)
            messagebox.showinfo("Download Complete", f"{yt.title} has been downloaded successfully!")
        else:
            messagebox.showerror("Error", "No suitable video stream found.")

    except Exception as e:  # Catch all other errors
        messagebox.showerror("Error", f"An error occurred: {e}")


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.configure(text=folder_path)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.geometry("400x200")
app.title("Youtube Video Downloader")

url_entry = customtkinter.CTkEntry(app, placeholder_text="Paste YouTube URL")
url_entry.pack(padx=20, pady=20)

folder_label = customtkinter.CTkLabel(app, text="Select Download Folder")
folder_label.pack()

folder_button = customtkinter.CTkButton(app, text="Select Folder", command=select_folder)
folder_button.pack(pady=10)

download_button = customtkinter.CTkButton(app, text="Download",
                                          command=lambda: download_video(url_entry.get(), folder_label.cget("text")))
download_button.pack(pady=10)

app.mainloop()
