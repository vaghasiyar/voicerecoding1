import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
import wavio as wv

def Record():
    try:
        freq = 44100  
        duration_value = int(duration.get())  
        recording = sd.rec(int(duration_value * freq), samplerate=freq, channels=2)
        sd.wait() 
        filename = "recording.wav"
        wv.write(filename, recording, freq, sampwidth=2)
        messagebox.showinfo("Recording Complete", f"Recording saved as {filename}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid duration in seconds")
    except Exception as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.geometry("800x500")
root.resizable(False, False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

tk.Label(root, text="Voice Recorder", font="Arial 30 bold", background="#4a4a4a", fg="white").pack()

duration = tk.StringVar()
tk.Entry(root, textvariable=duration, font="Arial 30", width=15).pack(pady=10)

tk.Label(root, text="Enter time in seconds", font="Arial 15", background="#4a4a4a", fg="white").pack()

tk.Button(root, font="Arial 20", text="Record", bg="#111111", fg="white", border=0, command=Record).pack(pady=30)

root.mainloop()
