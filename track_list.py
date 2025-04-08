import tkinter as tk
import track_library
import tkinter.scrolledtext as tkst
import font_manager as fonts

class CreateTrackList():
    def __init__(self,window):
        self.window=window
        self.window.title("Create Track List")
        self.playlist = [] # global playlist to store track numbers

        #create label and entry for track number
        tk.Label(window, text="Enter Track Number:").grid(row=0,column=0,padx=5,pady=5)
        self.entry_track = tk.Entry(window)
        self.entry_track.grid(row=0,column=1,padx=5,pady=5)
        #create button to add track
        tk.Button(window, text="Add Track",command=self.add_track).grid(row=0,column=2,padx=5,pady=5)
        #create label for the playlist display
        tk.Label(text="Playlist:").grid(row=1,column=0,columnspan=3,padx=5,pady=5)
        #create scrollable text widget to display the playlist
        self.text_playlist = tkst.ScrolledText(window,width=40,height=10,wrap="none")
        self.text_playlist.grid(row=2,column=0,columnspan=3,padx=5,pady=5)
        self.text_playlist.config(state=tk.DISABLED)
        #create a label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 11))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        #create button to play playlist
        tk.Button(window, text="Play Playlist",command=self.play_playlist).grid(row=4,column=0,padx=5,pady=5)
        #create button to reset playlist
        tk.Button(window, text="Reset Playlist",command=self.reset_playlist).grid(row=4,column=2,padx=5,pady=5)

    def add_track(self):
        """Add a track number to the playlist if the entered track number is valid"""
        track_number = self.entry_track.get().strip() #get the text from the entry and strip any whitespaces
        if not track_number.isdigit():
            self.status_lbl.configure(text="Invalid track number. Please enter a numeric value.")
            return # do not proceed if the track number is invalid
        track_name = track_library.get_name(track_number)
        if track_name is None:
            self.status_lbl.configure(text="Track not found. Please check the track number.")
            return #if track not found, just return without any message box

        self.playlist.append(track_number) #add track number to playlist
        self.display_playlist() #update the playlist display with the new track
        self.entry_track.delete(0,tk.END)

    def display_playlist(self):
        """update text widget with track names and play counts"""
        names=[]
        for num in self.playlist:
            track_name = track_library.get_name(num)
            play_count = track_library.get_play_count(num)
            names.append(f"{track_name} (Play Count:{play_count})")
        self.set_text(self.text_playlist, "\n".join(names)) #update the display

    def play_playlist(self):
        """increment play count for each track and refresh display"""
        if not self.playlist:
            return #do not proceed if the playlist is empty
        for num in self.playlist:
            track_library.increment_play_count(num)
        self.display_playlist()

    def reset_playlist(self):
        """clear and reset playlist"""
        self.playlist = []
        self.text_playlist.delete("1.0", tk.END) # clear text widget
        self.entry_track.delete("0",tk.END) #clear entry field
        self.status_lbl.configure(text="Playlist reset.")
        self.display_playlist() #update the text widget to reflect the empty playlist


    def set_text(self, text_area, content):
        """Inserts content into the text_area widget."""
        text_area.config(state=tk.NORMAL)  # Enable editing to insert content
        text_area.delete("1.0", tk.END)  # First, delete the existing content
        text_area.insert(1.0, content)  # Then, insert the new content
        text_area.config(state=tk.DISABLED)  # Make the text widget read-only again


if __name__ == "__main__":
    window = tk.Tk()  # Create a Tk object
    fonts.configure()
    CreateTrackList(window)  # Open the Track List GUI
    window.mainloop()  # Run the Tkinter main loop












