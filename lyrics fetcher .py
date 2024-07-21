#importing neccessary libraries 
import tkinter as tk
from tkinter import messagebox
from lyrics_extractor import SongLyrics

class LyricsExtractorApp:
    def __init__(self, master):
        self.master = master
        master.title("Lyrics Extractor")

        # Create labels and entry fields
        self.song_label = tk.Label(master, text="Enter Song Name:")
        self.song_label.grid(row=0, column=0)

        self.song_entry = tk.Entry(master, width=50)
        self.song_entry.grid(row=0, column=1)

        self.artist_label = tk.Label(master, text="Enter Artist Name:")
        self.artist_label.grid(row=1, column=0)

        self.artist_entry = tk.Entry(master, width=50)
        self.artist_entry.grid(row=1, column=1)

        # Create a button to fetch lyrics
        self.fetch_button = tk.Button(master, text="Get Lyrics", command=self.get_lyrics)
        self.fetch_button.grid(row=2, column=0, columnspan=2)

        # Create a text area to display the lyrics
        self.lyrics_text = tk.Text(master, height=15, width=60)
        self.lyrics_text.grid(row=3, column=0, columnspan=2)

    def get_lyrics(self):
        song_name = self.song_entry.get()
        artist_name = self.artist_entry.get()

        # Initialize the lyrics extractor
        extractor = SongLyrics("AIzaSyCCzQnUDsVAbt6RnLjw4lkgzd-efnhcjeo", "92dcc574603dc4625")
        
        try:
            # Fetch the lyrics
            lyrics = extractor.get_lyrics(f"{song_name} {artist_name}")
            self.lyrics_text.delete(1.0, tk.END)  # Clear previous lyrics
            self.lyrics_text.insert(tk.END, lyrics['lyrics'])  # Insert new lyrics
        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch lyrics: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LyricsExtractorApp(root)
    root.mainloop()
