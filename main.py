import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import pyttsx3

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from PDF: {e}")
        return None

# Function to convert text to speech
def convert_text_to_speech(text, output_path):
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        messagebox.showinfo("Success", f"Audio file saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert text to speech: {e}")

# Function to generate audiobook
def generate_audiobook():
    # Select PDF file
    pdf_file = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not pdf_file:
        return

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_file)
    if not text:
        return

    # Select output path for audio file
    audio_file = filedialog.asksaveasfilename(
        title="Save Audio File",
        defaultextension=".mp3",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    if not audio_file:
        return

    # Convert text to speech and save as audio file
    convert_text_to_speech(text, audio_file)

# Setting up tkinter window
root = tk.Tk()
root.title("PDF to Audiobook Converter")

# Add button to select and generate audiobook
select_button = tk.Button(root, text="Select PDF and Generate Audiobook", command=generate_audiobook)
select_button.pack(pady=20)

# Start the tkinter loop
root.geometry("400x200")
root.mainloop()
