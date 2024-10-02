import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
import pyttsx3

# Function to extract text from PDF in paragraph chunks using PyMuPDF
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text_chunks = []
        for page in doc:
            text = page.get_text("text")
            paragraphs = text.split("\n\n")  # Split text into paragraphs
            text_chunks.extend(paragraphs)
        return text_chunks
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from PDF: {e}")
        return None

# Function to convert a list of text chunks to speech
def convert_text_to_speech(text_chunks, output_path):
    try:
        engine = pyttsx3.init()
        for chunk in text_chunks:
            # engine.say(chunk)  # Speak the chunk
            engine.runAndWait()  # Process the speech
        # Optionally save the spoken content to a file
        engine.save_to_file(' '.join(text_chunks), output_path)
        engine.runAndWait()
        messagebox.showinfo("Success", f"Audio file saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert text to speech: {e}")

# Function to generate audiobook
def generate_audiobook():
    # Disable the button and set the cursor to "wait"
    root.config(cursor="wait")
    select_button.config(state="disabled")
    root.update()  # Update the UI to reflect the changes

    # Select PDF file
    pdf_file = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not pdf_file:
        reset_ui()
        return

    # Extract text from PDF
    text_chunks = extract_text_from_pdf(pdf_file)
    if not text_chunks:
        reset_ui()
        return

    # Select output path for audio file
    audio_file = filedialog.asksaveasfilename(
        title="Save Audio File",
        defaultextension=".mp3",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    if not audio_file:
        reset_ui()
        return

    # Convert text to speech and save as audio file
    convert_text_to_speech(text_chunks, audio_file)

    # Reset the UI once the task is done
    reset_ui()

# Function to reset the UI to its normal state
def reset_ui():
    root.config(cursor="")  # Reset the cursor
    select_button.config(state="normal")  # Re-enable the button
    root.update()  # Ensure UI updates properly

# Setting up tkinter window
root = tk.Tk()
root.title("PDF to Audiobook Converter")

# Add button to select and generate audiobook
select_button = tk.Button(root, text="Select PDF and Generate Audiobook", command=generate_audiobook)
select_button.pack(pady=20)

# Start the tkinter loop
root.geometry("400x200")
root.mainloop()
