import tkinter as tk #import the tkinter module for GUI
import tkinter.scrolledtext as tkst #import ScrolledText widget for text display

#import external libraries
import track_library as lib #handles track-related operations
import font_manager as fonts #handles font-related operations



def set_text(text_area, content): #insert content into the test_area
    text_area.delete("1.0", tk.END) #first the exiting content is deleted
    text_area.insert(1.0, content) #then the new content is inserted


class TrackViewer():
    """
    a GUI application to view and list music tracks
    """
    def __init__(self, window): #initializes the GUI window and all widgets
        window.geometry("750x350") # set window size
        window.title("View Tracks") #set window title

    #button to list all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) # positioning with padding

    #label for track number input
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

    #entry widget to input track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

    #button to view a specific track
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

    #scrollable text widget to list all tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    #text widget to display track details
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

    #label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    #populate track list on startup
        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        """
        handles the View Track Button click event.
        retrieves and displays details for the entered track number
        """
        key = self.input_txt.get() #get the track number from input field
        name = lib.get_name(key) #get track name
        if name is not None:
            artist = lib.get_artist(key) #get artist name
            rating = lib.get_rating(key) #get track rating
            play_count = lib.get_play_count(key) #get play count

            #format track details and display
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
        else:
            #display error message if track not found
            set_text(self.track_txt, f"Track {key} not found")
        #update status label
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        """
        handles the list all tracks button click event.
        retrieves and displays a list of all available tracks.
        """
        track_list = lib.list_all() #get all tracks from the library
        set_text(self.list_txt, track_list) #display track list in the text area
        self.status_lbl.configure(text="List All Tracks button was clicked!") #update status label

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
