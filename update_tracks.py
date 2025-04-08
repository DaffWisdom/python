import tkinter as tk
import track_library
import font_manager as fonts
import tkinter.scrolledtext as tkst
from  track_library import library


def set_text(text_area, content): #insert content into the test_area
    text_area.delete("1.0", tk.END)  # First, delete the existing content.
    text_area.insert(1.0, content)  # Then, insert the new content.
class Update_Rating():
    """
    a GUI application to update a track's rating and view details.
    """
    def __init__(self, window):
        window.geometry("550x370")  # Set the window size
        window.title("Update Track Rating")  # Set the window title

        # Create label and entry for track number
        tk.Label(window, text="Enter Track Number:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_track = tk.Entry(window)
        self.entry_track.grid(row=0, column=1, padx=5, pady=5)

        # Create label and entry for new rating
        tk.Label(window, text="Enter New Rating(1-5):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_rating = tk.Entry(window)
        self.entry_rating.grid(row=1, column=1, padx=5, pady=5)

        # Create a scrollable text widget to list all track details
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create a label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Create a button to update the rating
        tk.Button(window, text="Update Rating", command=self.update_rating_clicked).grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    def update_rating_clicked(self):
        """
        Handles the update rating button click event.
        Retrieves and updates details for the entered track number.
        """
        key = self.entry_track.get()  # Get the track number from the input field
        name = track_library.get_name(key)  # Get track name
        if name is not None:
            artist = track_library.get_artist(key)  # Get artist name
            rating = track_library.get_rating(key)  # Get track rating
            play_count = track_library.get_play_count(key)  # Get track play count

            # Format track details and display them in the text widget
            track_details = f"{name}\n{artist}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.list_txt, track_details)

            # Update the rating in the track library (if valid)
            new_rating = self.entry_rating.get().strip()
            if new_rating.isdigit() and 1 <= int(new_rating) <= 5:
                track_library.set_rating(key, int(new_rating))  # Update the rating
                updated_rating = track_library.get_rating(key)  # Get the updated rating

                # Show the success message with updated rating in status
                self.status_lbl.configure(text=f"Rating updated to {updated_rating}")

                # Refresh the details in the text widget immediately after updating the rating
                updated_rating = track_library.get_rating(key)
                play_count = track_library.get_play_count(key)
                track_details = f"{name}\n{artist}\nRating: {updated_rating}\nPlays: {play_count}"
                set_text(self.list_txt, track_details)  # Update the text widget with latest details

            else:
                self.status_lbl.configure(text="Please enter a valid rating between 1 and 5.")
        else:
            # Display error if the track is not found
            set_text(self.list_txt, f"Track {key} not found")
            self.status_lbl.configure(text="Track not found. Please check the track number.")

if __name__ == "__main__":
    window = tk.Tk()  # Create a Tk object
    fonts.configure()  # Configure fonts (font_manager.py)
    Update_Rating(window)  # Open the Update Rating GUI
    window.mainloop()  # Run the Tkinter main loop





























